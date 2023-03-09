/*
Author: Daniel M. Mwale
Email: danny@arcariusmexen.com
Date: 2023-03-09 Thursday
Description: Build script for IaRS-SE. It contains CREATE statements for a fully
             relational schema to store invoicing and receipting data
VERSION: 0.1.0
*/
CREATE TABLE invoice (
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