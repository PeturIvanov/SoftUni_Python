SELECT
	town_id,
	name AS town_name,
	address_text
FROM
	towns
JOIN
	addresses
USING
	(town_id)
WHERE
	name IN ('Sofia', 'San Francisco', 'Carnation')
ORDER BY
	town_id, address_id
;