SELECT t.request_at as 'Day', ROUND(SUM(cancelled) / COUNT(*), 2) as 'Cancellation Rate' 
FROM (
    SELECT request_at, IF(status != "completed", 1, 0) as cancelled
    FROM Trips 
    WHERE request_at BETWEEN "2013-10-01" AND "2013-10-03" 
        AND client_id IN (SELECT users_id FROM Users WHERE banned = "No") 
        AND driver_id IN (SELECT users_id FROM Users WHERE banned = "No")
) as t
GROUP BY t.request_at;