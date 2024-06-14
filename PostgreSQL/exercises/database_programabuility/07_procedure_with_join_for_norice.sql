CREATE OR REPLACE PROCEDURE sp_retrieving_holders_with_balance_higher_than(
	searched_balance NUMERIC
) AS
$$
	DECLARE holder_info RECORD;
	begin
		FOR holder_info in 
			select
				CONCAT_WS(' ', ah.first_name, ah.last_name) as full_name,
				SUM(balance) as total_balance
			from account_holders as ah
			join accounts as a
			on a.account_holder_id = ah.id
	GROUP BY full_name
	HAVING sum(balance) > searched_balance
	ORDER BY full_name

	LOOP 
		RAISE NOTICE '% - %', holder_info.full_name, holder_info.total_balance;
	END LOOP;
	end;
$$
LANGUAGE plpgsql;

CALL sp_retrieving_holders_with_balance_higher_than(200000);