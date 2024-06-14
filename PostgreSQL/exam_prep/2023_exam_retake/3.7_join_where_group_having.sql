SELECT
	p.name as product_name,
	round(AVG(p.price), 2) as average_price,
	COUNT(f.product_id) AS total_feedbacks

FROM products as p
JOIN feedbacks as f
ON p.id = f.product_id

WHERE p.price > 15
GROUP BY p.name
	
HAVING COUNT(f.product_id) > 1 
ORDER BY total_feedbacks ASC, average_price DESC;