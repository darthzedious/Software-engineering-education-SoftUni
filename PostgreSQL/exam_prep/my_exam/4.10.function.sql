CREATE OR REPLACE FUNCTION udf_accounts_photos_count(
	account_username VARCHAR(30)
) RETURNS INT AS
$$
	BEGIN
		RETURN (SELECT
		 			COUNT(a.id)
				FROM accounts AS a
	
				JOIN accounts_photos AS ap
				ON a.id = ap.account_id
	
				WHERE username = account_username);
	END;
$$
LANGUAGE plpgsql;

SELECT udf_accounts_photos_count('ssantryd') AS photos_count;