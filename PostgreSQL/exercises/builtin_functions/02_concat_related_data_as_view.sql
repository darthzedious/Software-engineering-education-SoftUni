CREATE OR REPLACE VIEW view_continents_countries_currencies_details AS
SELECT
	CONCAT_WS(': ', c.continent_name, c.continent_code) AS "continent_details",
	CONCAT_WS(' - ', cou.country_name, cou.capital, cou.area_in_sq_km, 'km2') AS "country_information",
	CONCAT(curr.description, ' (', curr.currency_code, ') ') as "currencies"
	
FROM continents as c, countries as cou, currencies as curr
	
WHERE c.continent_code = cou.continent_code and cou.currency_code = curr.currency_code
	
ORDER BY "country_information", "currencies";


SELECT * FROM view_continents_countries_currencies_details