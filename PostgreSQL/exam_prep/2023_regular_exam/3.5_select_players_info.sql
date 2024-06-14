SELECT 
	CONCAT_WS(' ', first_name, last_name) as full_name,
	age,
	hire_date
	
FROM players
WHERE first_name LIKE 'M%'
order by age DESC, full_name ASC;
