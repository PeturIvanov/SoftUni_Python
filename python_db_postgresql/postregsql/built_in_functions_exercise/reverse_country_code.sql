UPDATE
	countries
SET
	country_code = LOWER(REVERSE(country_code))
RETURNING
	country_code;