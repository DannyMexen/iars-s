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
    id bigserial PRIMARY KEY,
    name text NOT NULL UNIQUE,
    description text NOT NULL
);

-- B.   USERS
CREATE TABLE IF NOT EXISTS simple.user_role (
    id bigserial PRIMARY KEY,
    name text DEFAULT 'STANDARD' UNIQUE,
    description text NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS simple.user_department (
    id bigserial PRIMARY KEY,
    name text NOT NULL UNIQUE,
    description NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS simple.user_account_status (
    id bigserial PRIMARY KEY,
    name text DEFAULT 'ACTIVE' UNIQUE,
    description NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS simple.user_account (
    id bigserial PRIMARY KEY,
    user_name text NOT NULL 
);

-- C.   LOG AND EVENTS
CREATE TABLE IF NOT EXISTS simple.event (
    id bigserial PRIMARY KEY,
    name text,
    description text
);

-- TODO: Uncomment after user_person table is created
/*
CREATE TABLE IF NOT EXISTS simple.log (
    id bigserial PRIMARY KEY,
    event_id bigint REFERENCES simple.event (id),
    user_person_id bigint REFEENCES simple.user_person (id),
    date timestamp DEFAULT CURRENT_TIMESTAMP,
    details text
);
*/

-- E.   Invoices and Receipts
CREATE TABLE IF NOT EXISTS simple.invoice (
    id bigserial,
    invoice_number text,
    total_amount money NOT NULL,
    payment_condition_id bigserial NOT NULL,
    bank_id bigint NOT NULL,
    issue_date timestamp NOT NULL,
    due_date timestamp NOT NULL,
    client_id bigint NOT NULL,
    amws_id bigint NOT NULL,
    generated_by_user_id bigserial NOT NULL,
    generated_on timestamp NOT NULL,
    last_change_made_id bigint NULL,
    last_changed_by_user_id bigint NULL,
    last_changed_on timestamp NULL,

    PRIMARY KEY (id, invoice_number)


);