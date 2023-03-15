SELECT id
FROM (
    SELECT id, recordDate, temperature, 
        DATEDIFF(recordDate, LAG(recordDate) OVER (ORDER BY recordDate ASC)) as day_diff,
        LAG(temperature) OVER(ORDER BY recordDate ASC) as prev_temperature
    FROM Weather
) as t
WHERE temperature > prev_temperature AND day_diff = 1;