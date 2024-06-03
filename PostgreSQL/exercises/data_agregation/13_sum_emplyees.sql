SELECT
	count(CASE department_id WHEN 1 THEN 1 end) as "Engineering",
	count(CASE department_id WHEN 2 THEN 1 end) as "Tool Design",
	count(CASE department_id WHEN 3 THEN 1 end) as "Sales",
	count(CASE department_id WHEN 4 THEN 1 end) as "Marketing",
	count(CASE department_id WHEN 5 THEN 1 end) as "Purchasing",
	count(CASE department_id WHEN 6 THEN 1 end) as "Research and Development",
	count(CASE department_id WHEN 7 THEN 1 end) as "Production"
FROM employees


