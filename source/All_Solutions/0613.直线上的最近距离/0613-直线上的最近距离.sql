SELECT min(abs(p1.x - p2.x)) shortest
FROM  point p1 inner join point p2 
ON p1.x != p2.x