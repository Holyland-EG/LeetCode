SELECT id,
    MAX(IF(month = 'Jan', revenue, NULL)) as Jan_Revenue,
    MAX(IF(month = 'Feb', revenue, NULL)) as Feb_Revenue,
    MAX(IF(month = 'Mar', revenue, NULL)) as Mar_Revenue,
    MAX(IF(month = 'Apr', revenue, NULL)) as Apr_Revenue,
    MAX(IF(month = 'May', revenue, NULL)) as May_Revenue,
    MAX(IF(month = 'Jun', revenue, NULL)) as Jun_Revenue,
    MAX(IF(month = 'Jul', revenue, NULL)) as Jul_Revenue,
    MAX(IF(month = 'Aug', revenue, NULL)) as Aug_Revenue,
    MAX(IF(month = 'Sep', revenue, NULL)) as Sep_Revenue,
    MAX(IF(month = 'Oct', revenue, NULL)) as Oct_Revenue,
    MAX(IF(month = 'Nov', revenue, NULL)) as Nov_Revenue,
    MAX(IF(month = 'Dec', revenue, NULL)) as Dec_Revenue
FROM Department
GROUP BY id;