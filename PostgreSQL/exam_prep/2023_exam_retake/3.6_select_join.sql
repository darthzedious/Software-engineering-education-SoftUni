SELECT 
	f.product_id,
	f.rate,
	f.description,
	f.customer_id,
	c.age,
	c.gender

FROM feedbacks as f
JOIN customers as c
ON c.id = f.customer_id

WHERE f.rate < 5 AND c.gender = 'F' and c.age > 30
ORDER BY f.product_id DESC;