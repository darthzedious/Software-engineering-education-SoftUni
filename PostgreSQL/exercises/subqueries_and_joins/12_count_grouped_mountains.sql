SELECT
	moc.country_code,
	COUNT(m.mountain_range) as mountain_range_count

FROM mountains as m
JOIN mountains_countries as moc
ON moc.mountain_id = m.id
	WHERE moc.country_code = 'BG'
	OR moc.country_code = 'RU'
	OR moc.country_code = 'US'
GROUP BY moc.country_code
ORDER BY mountain_range_count DESC;