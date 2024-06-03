SELECT 
	job_title,
	CASE
		WHEN avg(salary) > 45800 THEN 'Good'
		WHEN avg(salary) BETWEEN 27000 and 45800 then 'Medium'
		ELSE 'Need Improvement'
	END as category
FROM employees
GROUP BY job_title
ORDER by category, job_title