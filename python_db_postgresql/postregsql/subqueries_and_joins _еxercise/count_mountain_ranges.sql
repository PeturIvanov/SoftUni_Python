SELECT
	mc.country_code,
	COUNT(m.mountain_range) AS mountain_range_count
FROM
	mountains AS m
		JOIN mountains_countries AS mc
			ON m.id = mc.mountain_id
GROUP BY
	mc.country_code
HAVING
	mc.country_code IN ('US', 'RU', 'BG')
ORDER BY
	COUNT(m.mountain_range) DESC
;