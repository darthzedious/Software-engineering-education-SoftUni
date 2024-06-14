SELECT
	i.name as ingredient_name,
	p.name as product_name,
	d.name as distributor_name


FROM ingredients as i
	
JOIN products_ingredients as pi
ON pi.ingredient_id = i.id

JOIN products as p
ON p.id = pi.product_id


JOIN distributors AS d
ON d.id = i.distributor_id

WHERE i.name = 'Mustard' and d.country_id = 16  --i."name" ILIKE '%mustard%'
ORDER BY product_name;