select min(t.log_id) start_id, max(t.log_id) end_id
from(
    select log_id, if(@prev=log_id-1, @count, @count:=@count+1) num, @prev:=log_id
    from Logs, (select @prev:=null, @count:=0)i
)t
group by t.num;