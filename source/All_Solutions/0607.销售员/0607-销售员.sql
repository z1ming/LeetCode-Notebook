select s.name
from salesperson s
left outer join
orders o
on s.sales_id=o.sales_id
left outer join 
company c
on o.com_id=c.com_id and c.name='RED'
group by s.name
having count(c.name)=0;