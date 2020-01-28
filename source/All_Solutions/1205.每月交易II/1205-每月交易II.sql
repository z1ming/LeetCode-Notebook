select date_format(a.trans_date,"%Y-%m") month,
a.country,
sum(a.sta="approved") approved_count,
sum((a.sta="approved")*a.amount) approved_amount,
sum(a.sta="backs") chargeback_count,
sum((a.sta="backs")*a.amount) chargeback_amount
from
(select *,"approved" as sta
from Transactions
where state="approved"
union all
select c.trans_id,t.country,t.state,t.amount,c.trans_date,"backs" as sta
from Chargebacks c
left join transactions t
on t.id=c.trans_id
) as a
group by date_format(a.trans_date,"%Y-%m"),a.country
having sum(a.sta="approved")+sum(a.sta="backs")<>0
order by date_format(a.trans_date,"%Y-%m")
