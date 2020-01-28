select * from 
((select 'succeeded' period_state, min(success_date)start_date, max(success_date)end_date
from (select success_date, if(datediff(success_date, @prev)=1, @count, @count:=@count+1) num, @prev:=success_date
from Succeeded, (select @prev:=null, @count:=0)i
where year(success_date)='2019') t
group by t.num)

union all

(select 'failed' period_state, min(fail_date)start_date, max(fail_date)end_date
from (select fail_date, if(datediff(fail_date, @prev)=1, @count, @count:=@count+1) num, @prev:=fail_date
from Failed, (select @prev:=null, @count:=0)i
where year(fail_date)='2019') t
group by t.num)) t
order by start_date;
