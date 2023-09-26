CREATE VIEW view_continents_countries_currencies_details
AS
SELECT
	concat(con.continent_name, ': ', con.continent_code) AS "Continent Details",
	concat_ws(' - ', coun.country_name, coun.capital, coun.area_in_sq_km, 'km2') AS "Country Information",
	concat(cur.description, ' ','(', coun.currency_code, ')') AS "Currencies"
FROM
	countries AS coun
JOIN
	continents AS con
			ON
	con.continent_code = coun.continent_code
JOIN
	currencies AS cur
			ON
	coun.currency_code = cur.currency_code
ORDER BY
	"Country Information", "Currencies";