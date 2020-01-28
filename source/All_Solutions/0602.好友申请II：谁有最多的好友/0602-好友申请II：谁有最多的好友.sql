#查询拥有好友最多的人和它拥有的好友数目
select temp1.all_peo id , count(*) num from request_accepted right join
    (select requester_id all_peo from 
        (select requester_id from request_accepted
        union
        select accepter_id from request_accepted) as temp) as temp1
    on request_accepted.requester_id = all_peo or request_accepted.accepter_id = all_peo group by temp1.all_peo order by count(*) desc limit 1;