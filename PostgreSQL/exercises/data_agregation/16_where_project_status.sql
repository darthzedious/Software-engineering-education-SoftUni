SELECT
	project_name,
	CASE
		WHEN start_date is null and end_date is null THEN 'Ready for development'
		WHEN start_date is not null and end_date is null THEN 'In Progress'
		ELSE 'Done'
	END as project_status
FROM projects

WHERE project_name LIKE '%Mountain%'
