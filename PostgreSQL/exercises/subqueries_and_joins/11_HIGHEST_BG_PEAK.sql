SELECT 
	moc.country_code,
	m.mountain_range,
	p.peak_name,
	p.elevation

FROM mountains as m
	
JOIN peaks as p
ON m.id = p.mountain_id

join mountains_countries as moc
ON moc.mountain_id = m.id

WHERE p.elevation > 2835 and moc.country_code = 'BG'
ORDER BY p.elevation DESC;