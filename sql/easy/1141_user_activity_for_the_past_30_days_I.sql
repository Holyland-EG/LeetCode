SELECT activity_date as day, COUNT(DISTINCT user_id) as active_users
FROM Activity
GROUP BY activity_date
HAVING activity_date BETWEEN DATE_SUB('2019-07-27', interval 29 day) AND '2019-07-27';