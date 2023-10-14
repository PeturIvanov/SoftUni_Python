CREATE OR REPLACE FUNCTION fn_full_name(first_name VARCHAR, last_name VARCHAR)
RETURNS VARCHAR
AS
$$
    DECLARE
        full_name VARCHAR;
    BEGIN
        IF first_name IS NULL AND last_name IS NULL THEN
            RETURN full_name;
        END IF;

        IF first_name IS NULL THEN SELECT INITCAP(last_name) INTO full_name;

        ELSIF last_name IS NULL THEN SELECT INITCAP(first_name) INTO full_name;

        ELSE SELECT concat(INITCAP(first_name), ' ', INITCAP(last_name)) INTO full_name;

        END IF;
        RETURN full_name;
    END
$$
LANGUAGE plpgsql
;

-- SECOND SOLUTION

-- CREATE OR REPLACE FUNCTION fn_full_name
-- (
--     first_name VARCHAR(50),
--     last_name VARCHAR(50)
-- )
-- RETURNS VARCHAR(101)
-- AS
-- $$
--     DECLARE
--         full_name VARCHAR(101);
--     BEGIN
--         full_name := CONCAT(INITCAP(first_name), ' ', INITCAP(last_name));
--         RETURN full_name;
--     END
-- $$
-- LANGUAGE plpgsql;
