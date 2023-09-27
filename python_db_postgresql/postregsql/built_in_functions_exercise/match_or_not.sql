SELECT
	companion_full_name,
	email
FROM
	users
WHERE
	email NOT LIKE '%@gmail'
			AND
	companion_full_name ILIKE '%and%';
