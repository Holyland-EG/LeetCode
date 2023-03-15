SELECT res.name
FROM (
    SELECT DISTINCT t1.name as name, t3.name as company
    FROM SalesPerson t1
    LEFT JOIN Orders t2
        ON t1.sales_id = t2.sales_id
    LEFT JOIN Company t3
        ON t2.com_id = t3.com_id
) res
GROUP BY res.name
HAVING MAX(IF(res.company = 'RED', 1, 0)) = 0;