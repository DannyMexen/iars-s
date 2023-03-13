/*
Author: Daniel M. Mwale
Email: danny@arcariusmexen.com
Date: 2023-03-09 Thursday
Description: Build script for IaRS-SE. It contains CREATE statements for a fully
             relational schema to store invoicing and receipting data
VERSION: 0.1.0
*/

/*
    Creation Order (attempts to address relationships)
    -- A. Stand-alone
    1. notification
    2. change_reason
    -- B. Logs
    1. event
    2. log
    -- C. Users
    1. role
    2. user_department
    3. user_account_status
    4. user_account
    5. user_person
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

-- Uncomment this section to start with new database, schema and tables.
/*
   Place the code below here 
*/
DROP TABLE IF EXISTS simple.notification, simple.change_reason, simple.invoice;
DROP SCHEMA IF EXISTS simple;
\connect postgres -- connect to any other database of your choice
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