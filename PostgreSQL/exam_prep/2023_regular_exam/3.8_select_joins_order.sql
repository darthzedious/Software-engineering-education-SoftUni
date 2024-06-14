SELECT
	CONCAT_WS(' ', c.first_name, c.last_name) AS coach_full_name,
	CONCAT_WS(' ', p.first_name, p.last_name) AS player_full_name,
	t.name as team_name,
	s.passing,
	s.shooting,
	s.speed

FROM coaches as c
	
JOIN players_coaches as pc
	ON pc.coach_id = c.id

JOIN players as p
	ON p.id = pc.player_id

JOIN skills_data as s
	ON s.id = p.skills_data_id

JOIN teams AS t 
	ON  p.team_id = t.id

ORDER BY coach_full_name ASC, player_full_name DESC;
