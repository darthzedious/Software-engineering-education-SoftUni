SELECT 
	department_id,
	SUM(salary) as "Total Salary"
	
FROM employees
GROUP BY department_id
HAVING SUM(salary) < 4200
ORDER by department_id