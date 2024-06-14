UPDATE coaches
SET salary = salary * coach_level
WHERE id IN (
    SELECT DISTINCT coach_id
    FROM players_coaches
    WHERE coach_id IS NOT NULL
)
AND first_name LIKE 'C%';