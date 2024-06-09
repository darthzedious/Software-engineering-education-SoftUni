SELECT 
	b.booking_id,
	b.starts_at :: DATE,
	b.apartment_id,
	CONCAT_WS(' ', c.first_name, c.last_name) AS "Customer Name"

FROM bookings as b

RIGHT JOIN customers as c
USING (customer_id)
ORDER BY "Customer Name"
LIMIT 10;