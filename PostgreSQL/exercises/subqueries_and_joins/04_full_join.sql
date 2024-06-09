SELECT
	b.booking_id,
	a.name as apartment_owner,
	a.apartment_id,
	CONCAT_WS(' ', c.first_name, c.last_name) as customer_name
	
FROM bookings as b
	
FULL JOIN apartments as a
USING (booking_id)

FULL JOIN customers as c
USING (customer_id)

ORDER BY 
	booking_id,
	apartment_owner,
	customer_name;