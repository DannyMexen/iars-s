/*
Author: Daniel M. Mwale
Email: danny@arcariusmexen.com
Date: 2023-03-09 Thursday
Description: Build script for IaRS-SE. It contains CREATE statements for a fully
             relational schema to store invoicing and receipting data
VERSION: 0.1.0
Notes:  For best results
        1.  Run this in psql environment
        2.  postgres (default database) is a convenience (see DROP statements below)
        3.  Permissions and privileges are left to you. Please review the link below
            https://www.postgresql.org/docs/15/index.html
        4.  If you're using VSCode, consider using Better Comments extension (no affiliation to project)
            It highlights certain sections of interest
*/

/*
    Creation Order (attempts to address relationships)
    -- A. Stand-alone
    1. notification
    2. change_reason
    -- B. Users
    1. role
    2. user_department
    3. user_account_status
    4. user_account
    5. user_person
    -- C. Logs
    1. event
    2. log
    -- D. Organizations
    1. province
    2. city
    3. client
    4. amws
    -- E. Invoices and Receipts
    1. bank
    2. condition
    3. invoice
    4. service
    5. invoice_item
    6. receipt_item
    7. receipt
*/

-- ! Uncomment this section to start with new database, schema and tables.
/*
   <Place the code below here to prevent execution>
*/
\connect postgres
DROP DATABASE IF EXISTS iars_test;

/*
    Database creation and connection
*/
CREATE DATABASE iars_test;
\connect iars_test

/*
    Schema search path - see PostgreSQL documentation for details
    https://www.postgresql.org/docs/current/ddl-schemas.html#DDL-SCHEMAS-CREATE  
*/
CREATE SCHEMA IF NOT EXISTS simple;
SET search_path  TO simple;


-- A. STANDALONE TABLES (No relationships)
/*  1.  notification
        messages sent to users at key moments
    2.  change_reason
        reasons for altering records
*/
CREATE TABLE IF NOT EXISTS simple.notification (
    id bigserial PRIMARY KEY,
    name text NOT NULL UNIQUE,
    description text NOT NULL
);

CREATE TABLE IF NOT EXISTS simple.change_reason (
    id bigserial PRIMARY KEY ,
    name text NOT NULL UNIQUE,
    description text NOT NULL
);

-- B.   USERS
CREATE TABLE IF NOT EXISTS simple.user_role (
    id bigserial PRIMARY KEY,
    name text DEFAULT 'STANDARD' NOT NULL UNIQUE,
    description text NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS simple.user_account_status (
    id bigserial PRIMARY KEY,
    name text DEFAULT 'ACTIVE' NOT NULL UNIQUE,
    description text NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS simple.user (
    id bigserial,
    login_name text, 
    password_hash text NOT NULL,
    user_account_status_id bigint NOT NULL REFERENCES simple.user_account_status (id),
    user_role_id bigint NOT NULL REFERENCES simple.user_role (id),
    first_name text NOT NULL,
    last_name text NOT NULL,
    phone_number text NOT NULL UNIQUE,

    PRIMARY KEY (id, login_name)
);

-- C.   LOG AND EVENTS
CREATE TABLE IF NOT EXISTS simple.event (
    id bigserial PRIMARY KEY,
    name text NOT NULL UNIQUE,
    description text NOT NULL
);

CREATE TABLE IF NOT EXISTS simple.log (
    id bigserial PRIMARY KEY,
    event_id bigint NOT NULL REFERENCES simple.event (id),
    user_id bigint NOT NULL,
    user_login_name text NOT NULL,
    date timestamp DEFAULT CURRENT_TIMESTAMP,
    details text,

    FOREIGN KEY (user_id, user_login_name) REFERENCES simple.user (id, login_name)
);

-- D.   ORGANIZATIONS
CREATE TABLE IF NOT EXISTS simple.province (
    id bigserial PRIMARY KEY,
    name text NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS simple.city (
    id bigserial PRIMARY KEY,
    name text NOT NULL UNIQUE,
    province_id bigint NOT NULL REFERENCES simple.province (id)
);

CREATE TABLE IF NOT EXISTS simple.client (
    id bigserial PRIMARY KEY,
    name text NOT NULL,
    street text NOT NULL,
    area text NOT NULL,
    city_id bigint NOT NULL REFERENCES simple.city (id),
    contact_first_name text NOT NULL,
    contact_last_name text NOT NULL,
    contact_email text NOT NULL UNIQUE,
    contact_phone_number text NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS simple.amws (
    id bigserial PRIMARY KEY,
    name text NOT NULL,
    tpin text NOT NULL,
    street text NOT NULL,
    area text NOT NULL,
    city_id bigint NOT NULL REFERENCES simple.city (id),
    contact_first_name text NOT NULL,
    contact_last_name text NOT NULL,
    contact_email text NOT NULL UNIQUE,
    contact_phone_number text NOT NULL UNIQUE
);

-- E.   INVOICES AND RECEIPTS
CREATE TABLE IF NOT EXISTS simple.bank_account_type (
    id bigserial PRIMARY KEY,
    name text NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS simple.bank (
    id bigserial PRIMARY KEY,
    name text NOT NULL,
    account_type_id bigint NOT NULL REFERENCES simple.bank_account_type (id),
    swift_code text NOT NULL UNIQUE,
    branch_name text NOT NULL
);

CREATE TABLE IF NOT EXISTS simple.payment_condition (
    id bigserial PRIMARY KEY,
    name text NOT NULL UNIQUE,
    description text NOT NULL
);


CREATE TABLE IF NOT EXISTS simple.service (
    id bigserial PRIMARY KEY,
    name text NOT NULL UNIQUE,
    description text NOT NULL,
    cost money NOT NULL
);

CREATE TABLE IF NOT EXISTS simple.invoice (
    id bigserial,
    invoice_number text,
    total_amount money NOT NULL,
    payment_condition_id bigserial NOT NULL REFERENCES simple.payment_condition (id),
    bank_id bigint NOT NULL REFERENCES simple.bank (id),
    issue_date timestamp NOT NULL,
    due_date timestamp NOT NULL,
    client_id bigint NOT NULL REFERENCES simple.client (id),
    amws_id bigint NOT NULL REFERENCES simple.amws (id),

    PRIMARY KEY (id, invoice_number)
);
<<<<<<< HEAD
=======

CREATE TABLE IF NOT EXISTS simple.invoice_item (
    id bigserial,
    item_number text,
    invoice_number text NOT NULL REFERENCES simple.invoice (invoice_number),
    service_id bigint NOT NULL REFERENCES simple.service (id),
    quantity int NOT NULL,
    total_amount money NOT NULL,
    due_date date NOT NULL,
<<<<<<< HEAD
    issue_date date DEFAULT CURRENT_DATE NOT NULL
);
>>>>>>> 90c30f2 (added invoice item table)
=======
    issue_date date DEFAULT CURRENT_DATE NOT NULL,

    PRIMARY KEY (id, item_number)
);
>>>>>>> 4fff747 (added PK)
