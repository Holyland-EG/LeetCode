SELECT res.Department, res.Employee, res.Salary
FROM (
    SELECT e1.name as 'Employee', e1.salary as 'Salary', d1.name as 'Department',  
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) as salary_rank 
    FROM Employee as e1
    JOIN Department as d1
    ON e1.departmentId = d1.id
) as res
WHERE res.salary_rank <= 3;