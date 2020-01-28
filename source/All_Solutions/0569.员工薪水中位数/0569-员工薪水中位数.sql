SELECT t1.Id, t1.Company, t1.Salary
FROM Employee t1
	LEFT JOIN Employee t2 ON t1.Company = t2.Company
GROUP BY t1.Company, t1.Salary
HAVING SUM(CASE 
	WHEN t1.Salary = t2.Salary THEN 1
	ELSE 0
END) >= abs(SUM(sign(t1.Salary - t2.Salary)))
ORDER BY t1.Id;