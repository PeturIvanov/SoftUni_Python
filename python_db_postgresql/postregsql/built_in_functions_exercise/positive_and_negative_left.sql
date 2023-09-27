SELECT
	peak_name,
	LEFT(peak_name, 4),
	LEFT(peak_name, -4)
FROM
	peaks;