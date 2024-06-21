CREATE OR REPLACE PROCEDURE udp_modify_account(
    IN address_street VARCHAR(30),
    IN address_town VARCHAR(30)
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_account_id INT;
    v_current_job_title VARCHAR(100);
BEGIN

    SELECT a.account_id
    INTO v_account_id
    FROM addresses AS a
    WHERE a.street = address_street
    AND a.town = address_town;


    IF FOUND THEN

        SELECT acc.job_title
        INTO STRICT v_current_job_title
        FROM accounts AS acc
        WHERE acc.id = v_account_id;

        IF v_current_job_title NOT ILIKE '(Remote)%' THEN
            UPDATE accounts
            SET job_title = CONCAT('(Remote) ', v_current_job_title)
            WHERE id = v_account_id;
        END IF;
    END IF;
END;
$$;


CALL udp_modify_account('97 Valley Edge Parkway', 'Divinópolis');
SELECT a.username, a.gender, a.job_title FROM accounts AS a
WHERE a.job_title ILIKE '(Remote)%';

CALL udp_modify_account('97 Valley Edge Parkway', 'Nonexistent');
SELECT a.username, a.gender, a.job_title FROM accounts AS a
WHERE a.job_title ILIKE '(Remote)%';
