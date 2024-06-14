CREATE OR REPLACE FUNCTION fn_full_name(
	first_name VARCHAR(50),
	last_name VARCHAR(50)
) RETURNS VARCHAR(101) AS 
$$
	DECLARE full_name VARCHAR(101);
	BEGIN
		full_name := concat_ws(' ', INITCAP(lower(first_name)), INITCAP(lower(last_name)));
		RETURN full_name;
	END;
$$
LANGUAGE plpgsql;

select fn_full_name(country_name, country_name) from countries
