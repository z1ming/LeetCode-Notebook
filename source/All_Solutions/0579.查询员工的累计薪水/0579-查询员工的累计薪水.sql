SELECT
  a.Id AS id, a.Month AS month,SUM(b.Salary) AS Salary
FROM
  Employee a, Employee b
WHERE a.Id = b.Id 
AND a.Month >= b.Month
AND a.Month < b.Month+3
AND (a.Id, a.Month) NOT IN (SELECT Id, MAX(Month) FROM Employee GROUP BY Id)
GROUP BY a.Id, a.Month
ORDER BY a.Id, a.Month DESC