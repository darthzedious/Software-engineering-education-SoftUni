SELECT
	c.country_name,
	r.river_name

FROM countries as c
	
LEFT JOIN countries_rivers as cor
USING (country_code)

LEFT JOIN rivers  AS r
ON r.id = cor.river_id

WHERE 
	c.continent_code = 'AF'
ORDER BY 
	c.country_name
LIMIT 5;