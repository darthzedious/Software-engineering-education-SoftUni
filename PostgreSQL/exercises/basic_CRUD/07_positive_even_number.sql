SELECT
	CONCAT("number", ' ', "street") AS adress,
	"city_id"
FROM addresses
WHERE city_id > 0 and city_id % 2 = 0
ORDER BY city_id;