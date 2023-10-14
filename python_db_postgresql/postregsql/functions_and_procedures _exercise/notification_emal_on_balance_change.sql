CREATE TABLE notification_emails(
    id SERIAL PRIMARY KEY ,
    recipient_id INT,
    subject TEXT,
    body TEXT
)
;

CREATE OR REPLACE FUNCTION trigger_fn_send_email_on_balance_change()
RETURNS TRIGGER
AS
$$
    BEGIN
        INSERT INTO notification_emails(
                                        recipient_id,
                                        subject,
                                        body
                                        )
        VALUES (
                old.account_id,
                concat_ws(' ', 'Balance', 'change', 'for', 'account:', old.account_id),
                concat_ws(' ', 'On', DATE(now()), 'your', 'balance', 'was', 'changed', 'from', old.old_sum, 'to', new.new_sum)
               );
        RETURN new;
    END
$$
LANGUAGE plpgsql
;

CREATE OR REPLACE TRIGGER tr_send_email_on_balance_change
AFTER UPDATE ON logs
FOR EACH ROW
EXECUTE FUNCTION trigger_fn_send_email_on_balance_change()
;
