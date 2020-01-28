select e.name,b.bonus
from employee e left join bonus b
on e.empid=b.empid
where
ifnull(bonus,0)<1000 ;