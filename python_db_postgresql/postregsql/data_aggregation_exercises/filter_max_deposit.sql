SELECT
	magic_wand_creator,
	MAX(deposit_amount) AS max_deposit_amount
FROM
	wizard_deposits
WHERE
	deposit_amount <= 20000
				OR
	deposit_amount >= 40000
GROUP BY
	magic_wand_creator
ORDER BY
	max_deposit_amount DESC
LIMIT 3
;

