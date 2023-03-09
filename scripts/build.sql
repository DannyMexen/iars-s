/*
Author: Daniel M. Mwale
Email: danny@arcariusmexen.com
Date: 2023-03-09 Thursday
Description: Build script for IaRS-SE. It contains CREATE statements for a fully
             relational schema to store invoicing and receipting data
VERSION: 0.1.0
*/
CREATE TABLE invoice (
    id,
    invoice_number,
    total_amount,
    payment_condition_id,
    bank_id,
    issue_date,
    due_date,
    client_id,
    amws_id,
    generated_by_user_id,
    generated_on,
    last_change_made_id,
    last_changed_by_user_id,
    last_changed_on



)