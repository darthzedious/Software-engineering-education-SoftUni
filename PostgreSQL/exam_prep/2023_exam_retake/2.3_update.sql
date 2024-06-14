UPDATE products

SET price = price + price * 0.1
WHERE id in (
	select 
		product_id
	from feedbacks
	WHERE rate > 8
);