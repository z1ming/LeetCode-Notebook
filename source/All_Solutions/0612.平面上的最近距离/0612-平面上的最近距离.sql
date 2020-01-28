select 
round(min(sqrt(pow(t1.x-t2.x,2)+pow(t1.y-t2.y,2))),2) shortest
from point_2d as t1,point_2d as t2
where (t1.x,t1.y) != (t2.x,t2.y)