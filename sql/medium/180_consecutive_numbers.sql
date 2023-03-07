SELECT DISTINCT num as ConsecutiveNums
FROM (
    SELECT num, 
        LAG(num, 1) OVER(order by id) as lag_1,
        LAG(num, 2) OVER(order by id) as lag_2
    FROM Logs
) as t
WHERE t.num = t.lag_1 and t.num = t.lag_2;