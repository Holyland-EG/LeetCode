SELECT u.name, IF(r.travelled_distance IS NULL, 0, r.travelled_distance) as travelled_distance
FROM Users u
LEFT JOIN (
    SELECT user_id, SUM(distance) as travelled_distance
    FROM Rides
    GROUP BY user_id
) r
ON u.id = r.user_id
ORDER BY r.travelled_distance DESC, u.name ASC;