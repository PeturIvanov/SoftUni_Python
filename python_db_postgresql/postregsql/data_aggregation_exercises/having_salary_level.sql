SELECT
	department_id,
	COUNT(department_id) AS num_employees,
	CASE AVG(salary) > 50000
		WHEN TRUE THEN 'Above average'
		ELSE 'Below average'
	END AS salary_level
FROM
	employees
GROUP BY
	department_id
HAVING
	AVG(salary) > 30000
ORDER BY
	department_id
;