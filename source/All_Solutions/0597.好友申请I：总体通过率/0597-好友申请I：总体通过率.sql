select round(
    ifnull(
    (select count(distinct requester_id ,accepter_id) from request_accepted) / 
    (select count(distinct sender_id ,send_to_id) from friend_request)
    ,0)
    ,2) as accept_rate ;