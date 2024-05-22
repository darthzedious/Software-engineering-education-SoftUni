SELECT 
	DISTINCT name,
CONCAT(area) AS "area_km2"
FROM cities
ORDER BY name DESC;
