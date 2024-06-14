SELECT
	t.id as team_id,
	t.name as team_name,
	count(p.id) as player_count,
	t.fan_base as fan_base

FROM teams as t
	
LEFT JOIN players as p
ON p.team_id = t.id

GROUP BY
  t."id",
  t."name",
  t.fan_base

HAVING t.fan_base > 30000

ORDER BY player_count desc, t.fan_base desc;