SELECT 
	last_name,
	COUNT(notes) as "notes_with_dumbledore"
	
FROM wizard_deposits
where notes LIKE '%Dumbledore%'
GROUP BY last_name

