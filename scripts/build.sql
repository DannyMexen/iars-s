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
    total_amount money,
    payment_condition_id bigserial,
    bank_id bigserial,
    issue_date timestamp,
    due_date timestamp,
    client_id bigserial,
    amws_id bigserial,
    generated_by_user_id bigserial,
    generated_on timestamp,
    last_change_made_id bigserial,
    last_changed_by_user_id bigserial,
    last_changed_on timestamp



)