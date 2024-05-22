SELECT "id",
	CONCAT(number, ' ', street) as adress,
	"city_id"
FROM addresses
WHERE id >= 20;