CREATE VIEW view_addresses AS
SELECT
	concat(em.first_name, ' ', em.last_name) AS "Full Name",
	em.department_id,
	concat(ad.number, ' ', ad.street) AS "Address"
FROM
	employees AS em,
	addresses AS ad
WHERE
	em.address_id = ad.id
ORDER BY "Address";