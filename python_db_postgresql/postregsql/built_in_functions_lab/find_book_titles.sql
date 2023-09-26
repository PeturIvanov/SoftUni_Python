SELECT
	title
FROM
	books
WHERE
	LEFT(title, 4) = 'The '
ORDER BY id;