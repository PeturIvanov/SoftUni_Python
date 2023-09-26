SELECT
	concat_ws(' ', m.mountain_range, p.peak_name) AS "Mountain Information",
	LENGTH(concat_ws(' ', m.mountain_range, p.peak_name)) AS "Characters Length",
	BIT_LENGTH(concat_ws(' ', m.mountain_range, p.peak_name)) AS "Bits of a String"
FROM
	mountains AS m
JOIN
	peaks as p
			ON
	p.mountain_id = m.id