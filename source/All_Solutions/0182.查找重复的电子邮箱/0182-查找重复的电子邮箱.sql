# Write your MySQL query statement below
select distinct 
       a.email as Email 
from 
       person a 
group by  
       a.email 
having
       count(a.email)>1;