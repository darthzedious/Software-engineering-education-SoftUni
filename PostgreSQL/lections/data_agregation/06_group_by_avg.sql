SELECT 
	department_id,
	AVG(salary) as "avg_salary"
	
FROM employees
GROUP BY department_id
ORDER by department_id