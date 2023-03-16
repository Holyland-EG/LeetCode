SELECT res.buyer_id, res.join_date, 
	SUM(IF(EXTRACT(YEAR FROM res.order_date) = '2019', 1, 0)) as orders_in_2019
FROM (
    SELECT u.user_id as buyer_id, u.join_date, o.order_date
    FROM Users as u
    LEFT JOIN Orders as o
    ON u.user_id = o.buyer_id
) as res
GROUP BY res.buyer_id, res.join_date;