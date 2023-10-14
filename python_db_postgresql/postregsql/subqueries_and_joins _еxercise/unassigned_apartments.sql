SELECT
	b.booking_id,
	b.apartment_id,
	c.companion_full_name
FROM
	customers AS c
		JOIN bookings AS b
			USING(customer_id)
WHERE
	apartment_id IS NULL
;