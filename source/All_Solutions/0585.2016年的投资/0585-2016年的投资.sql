SELECT SUM(insurance.TIV_2016) AS TIV_2016
FROM
insurance
where insurance.TIV_2015 IN
    #2015年投资不唯一并维度唯一
	(SELECT TIV_2015 FROM insurance t GROUP BY TIV_2015 HAVING COUNT(*)>1)
	AND
	CONCAT(LAT,CONCAT(',',LON)) IN(
	SELECT CONCAT(LAT,CONCAT(',',LON))
	FROM insurance
	GROUP BY LAT,LON
	HAVING COUNT(*)=1
	)