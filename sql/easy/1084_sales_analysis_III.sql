SELECT s.product_id, p.product_name
FROM (
    SELECT product_id
    FROM Sales
    GROUP BY product_id
    HAVING MAX(sale_date) >= '2019-01-01' 
    	AND MAX(sale_date) <= '2019-03-31' 
    	AND MIN(sale_date) >= '2019-01-01' 
    	AND MIN(sale_date) <= '2019-03-31'
) as s
JOIN Product as p
ON s.product_id = p.product_id;