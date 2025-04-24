WITH LaggedLogs AS (
    SELECT
        num,
        LAG(num, 1) OVER (ORDER BY id) as prev1_num,
        LAG(num, 2) OVER (ORDER BY id) as prev2_num
    FROM
        Logs
)
SELECT DISTINCT
    num AS ConsecutiveNums
FROM
    LaggedLogs
WHERE
    num = prev1_num AND num = prev2_num;