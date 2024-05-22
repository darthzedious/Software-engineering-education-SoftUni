CREATE VIEW view_addresses AS 
SELECT 
	
	CONCAT(e.first_name, ' ', e.last_name) as "full_name",
	e.department_id,	
	CONCAT(a.number, ' ', a.street) AS "address"
	
FROM employees as e, addresses as a
	
WHERE e.address_id = a.id
ORDER BY address;
	