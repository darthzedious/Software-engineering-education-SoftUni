SELECT
	title,
	trunc(cost, 3)  AS "modified_price"
FROM books
order by id;