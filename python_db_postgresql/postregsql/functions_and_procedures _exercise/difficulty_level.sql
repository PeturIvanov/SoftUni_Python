CREATE OR REPLACE FUNCTION fn_difficulty_level(
    level INT
)
RETURNS VARCHAR(25)
AS
$$
    DECLARE
        difficulty VARCHAR(25);
    BEGIN
        IF level <= 40 THEN difficulty := 'Normal Difficulty';

        ELSIF level BETWEEN 41 AND 60 THEN difficulty := 'Nightmare Difficulty';

        ELSE difficulty := 'Hell Difficulty';

        END IF;
        RETURN difficulty;
    END
$$
LANGUAGE plpgsql
;

SELECT
    user_id,
    level,
    cash,
    fn_difficulty_level(level)
FROM
    users_games
ORDER BY
    user_id
;
