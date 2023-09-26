SELECT
	last_name AS "Last Name",
	TO_CHAR(born, 'DD (Dy) Mon YYYY') AS date
FROM
	authors;