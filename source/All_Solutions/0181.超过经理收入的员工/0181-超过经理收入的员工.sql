# Write your MySQL query statement below
SELECT 
    Name Employee
FROM
    Employee AS a
WHERE
    Salary > (SELECT 
            Salary
        FROM
            Employee
        WHERE
            Id = a.Managerid)