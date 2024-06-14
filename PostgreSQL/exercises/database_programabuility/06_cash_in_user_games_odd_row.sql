CREATE OR REPLACE FUNCTION fn_cash_in_users_games(
	game_name VARCHAR(50)
) RETURNS TABLE (
	total_cash NUMERIC
) AS 
$$
	BEGIN
	
	RETURN QUERY
		WITH ranked_games AS (
		SELECT 
			cash,
			ROW_NUMBER() OVER(ORDER BY cash DESC) AS row_num
		FROM users_games as ug
		JOIN games as g
		on ug.game_id = g.id
		WHERE g.name = game_name
		)
	

		SELECT
			ROUND(SUM(cash), 2) as total_cash
		FROM ranked_games as rg
		WHERE rg.row_num <> 0;
	
	END;
$$
LANGUAGE plpgsql;