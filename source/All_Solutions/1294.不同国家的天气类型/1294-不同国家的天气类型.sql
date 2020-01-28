select country_name, 
(case 
    when avg <= 15 then "Cold"
    when avg >= 25 then "Hot"
    else "Warm"
end) as weather_type
from (
select c.country_name, avg(w.weather_state) as avg
from Countries as c, Weather as w
where c.country_id = w.country_id and month(w.day)=11
group by c.country_name
order by c.country_id
) as new;