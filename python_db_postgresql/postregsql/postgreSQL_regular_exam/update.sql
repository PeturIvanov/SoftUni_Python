UPDATE coaches
SET salary = salary * coach_level
WHERE
    first_name LIKE 'C%'
            AND
    (SELECT
    COUNT(player_id)
FROM
    players_coaches
WHERE
    coach_id = id
GROUP BY
    coach_id
ORDER BY
    coach_id) > 1
;