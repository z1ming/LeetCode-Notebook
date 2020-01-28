select Name 
from Employee
where Id in(
select distinct ManagerId
from Employee
group by ManagerID
having count(ManagerID)>=5
)