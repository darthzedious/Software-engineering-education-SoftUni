SELECT
	d.name as distributor_name,
	i.name as ingredient_name,
	p.name as product_name,
	AVG(f.rate) as average_rate

FROM distributors as d
	
JOIN ingredients as i
ON d.id = i.distributor_id

JOIN products_ingredients as pi
ON pi.ingredient_id = i.id

JOIN products as p
ON p.id = pi.product_id

JOIN feedbacks as f
ON p.id = f.product_id

GROUP BY d.name, i.name, p.name

HAVING AVG(f.rate) BETWEEN 5 AND 8

ORDER BY d.name, i.name, p.name;