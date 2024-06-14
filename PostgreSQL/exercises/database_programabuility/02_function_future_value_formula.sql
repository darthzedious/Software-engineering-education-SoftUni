CREATE OR REPLACE FUNCTION fn_calculate_future_value(
	initial_sum DECIMAL,
	yearly_interest_rate DECIMAL,
	number_of_years INT
) RETURNS DECIMAL AS 
	
$$
	DECLARE
		futur_value decimal;
	BEGIN
		futur_value := TRUNC(initial_sum * (power(1 + yearly_interest_rate, number_of_years)), 4);
		RETURN futur_value;
	END;
$$
language plpgsql;

SELECT * FROM fn_calculate_future_value(1000, 0.1, 5);