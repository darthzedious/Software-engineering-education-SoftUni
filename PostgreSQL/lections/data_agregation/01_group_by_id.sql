SELECT 
	department_id,
	COUNT(id) as "employee_count"
	
FROM employees
GROUP BY department_id
ORDER BY department_id;