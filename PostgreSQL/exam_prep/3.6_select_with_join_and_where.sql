SELECT
	p.id,
	CONCAT_WS(' ', p.first_name, p.last_name) as full_name,
	p.age,
	p.position,
	p.salary,
	sd.pace,
	sd.shooting

FROM players as p
	
JOIN skills_data as sd
	on p.skills_data_id = sd.id
	
WHERE
  p.position = 'A'
  AND p.team_id IS NULL
  AND sd.pace + sd.shooting > 130;