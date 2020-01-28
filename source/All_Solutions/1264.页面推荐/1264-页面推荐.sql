select 
    distinct page_id as recommended_page 
from Likes  
where  user_id  in (select 
                        if(user1_id=1,user2_id,user1_id) as friend
                    from  Friendship  where user1_id =1 or user2_id =1
                    ) 
and  page_id  not in (select page_id from Likes where user_id= 1)