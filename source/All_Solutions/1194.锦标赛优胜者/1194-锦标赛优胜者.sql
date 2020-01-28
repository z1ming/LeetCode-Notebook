select group_id, p as player_id
from (
         select group_id, s, p, @r := (case when @s = n.group_id then @r + 1 else 1 end) as rn, @s := group_id
         from (
                  select t.group_id, s, p
                  from (
                           select sum(s) as s, p
                           from (
                                    select first_player as p, first_score as s
                                    from Matches
                                    union all
                                    select second_player, second_score
                                    from Matches
                                ) t
                           group by p
                       ) x
                           left join Players t on x.p = t.player_id
                  order by group_id, s desc, p
              ) n,
              (select @r := 0, @s := 0) m) f
where rn = 1