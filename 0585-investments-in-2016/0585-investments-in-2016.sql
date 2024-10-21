# Write your MySQL query statement below
WITH SameTiv2015 AS (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
),
UniqueCity AS (
    SELECT pid, tiv_2016
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
)
SELECT ROUND(SUM(I.tiv_2016), 2) AS tiv_2016
FROM Insurance I
JOIN SameTiv2015 ST
ON I.tiv_2015 = ST.tiv_2015
JOIN UniqueCity UC
ON I.pid = UC.pid;
