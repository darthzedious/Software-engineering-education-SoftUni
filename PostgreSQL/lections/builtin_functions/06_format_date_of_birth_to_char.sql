SELECT
	last_name as "Last Name",
	to_char(born, 'DD (Dy) Mon YYYY') as "Date of Birth"
FROM authors