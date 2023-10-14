CREATE OR REPLACE PROCEDURE sp_players_team_name(
    IN player_name VARCHAR(50),
    OUT team_name VARCHAR (45)
)
AS
$$
    DECLARE
        team_name_var VARCHAR(45);
    BEGIN

        SELECT t.name INTO team_name_var
            FROM players AS p
                LEFT JOIN teams AS t
                    ON p.team_id = t.id
                          WHERE concat(p.first_name, ' ', p.last_name) = player_name;

        IF team_name_var IS NULL THEN team_name := 'The player currently has no team';
        ELSE team_name := team_name_var;
        END IF;
    END
$$
LANGUAGE plpgsql
;