SELECT t.id,
    IF(mod(t.id, 2) <> 0, IF(t.next_s IS NULL, t.student, t.next_s), t.prev_s) as student
FROM (
    SELECT id, student, 
        LAG(student) OVER () as prev_s,
        LEAD(student) OVER () as next_s
    FROM Seat
) as t;