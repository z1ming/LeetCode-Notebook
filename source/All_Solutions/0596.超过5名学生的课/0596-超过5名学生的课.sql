select class
from (
    select distinct *
    from courses
) temp
group by class
having count(student)>=5