SELECT e.name as Employee
FROM Employee as e
LEFT JOIN (
    SELECT id, salary
    FROM Employee
) as m
ON m.id = e.managerId
WHERE e.salary > m.salary;