SELECT 
	department_id,
	sum(salary) as "total_salaries"
	
FROM employees
GROUP BY department_id
ORDER by department_id