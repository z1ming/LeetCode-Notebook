select avg(t.minnum) median from
(select min(a1.number) minnum
 from
(select n1.number,sum(n2.frequency) cumsum from numbers n1,numbers n2
where n1.number>=n2.number group by n1.number) a1,
(select sum(frequency) cnt from numbers)a2
where a1.cumsum>=floor((a2.cnt+1)/2)

union all


select min(a3.number) minnum
from
(select n3.number,sum(n4.frequency) cumsum
from numbers n3,numbers n4
where
n3.number>=n4.number
group by n3.number) a3,(select sum(frequency) cnt from numbers)a4
where a3.cumsum>=ceil((a4.cnt+1)/2)) t