SELECT
	p.id as photo_id,
	p.capture_date,
	p.description, 
	COUNT(c.photo_id) AS comments_count

FROM photos as p

JOIN comments as c
ON c.photo_id = p.id

WHERE p.description IS NOT NULL
GROUP BY p.id
ORDER BY COUNT(c.photo_id) DESC, p.id ASC
LIMIT 3;