SELECT DISTINCT ON ("name")
	"name",
	area AS "Area (km2)"
FROM
	cities
ORDER BY "name" DESC;