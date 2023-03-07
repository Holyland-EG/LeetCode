SELECT d.name as Department, e.name as Employee, e.salary as Salary
FROM (
    SELECT departmentId, name, salary
    FROM Employee
    WHERE (departmentId, salary) IN (SELECT departmentId, max(salary) as maxSalary
                                     FROM Employee
                                     GROUP BY departmentId)
) as e
LEFT JOIN Department as d ON d.id = e.departmentId;