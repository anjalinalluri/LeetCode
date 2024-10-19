# Write your MySQL query statement below
WITH FirstLogin AS (
    -- Find the first login date for each player
    SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
),
ConsecutiveLogin AS (
    -- Find players who logged in the day after their first login
    SELECT DISTINCT A.player_id
    FROM Activity A
    JOIN FirstLogin F
    ON A.player_id = F.player_id
    WHERE A.event_date = DATE_ADD(F.first_login, INTERVAL 1 DAY)
)
-- Calculate the fraction of players who logged in on consecutive days
SELECT ROUND(COUNT(DISTINCT C.player_id) / COUNT(DISTINCT F.player_id), 2) AS fraction
FROM FirstLogin F
LEFT JOIN ConsecutiveLogin C
ON F.player_id = C.player_id;
