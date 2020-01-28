# Write your MySQL query statement below
select
    Id
from
    (select w.*,
     @curd := w.RecordDate,
     @curt := w.Temperature,
     @isH := if(datediff(@curd,@pred) = 1 and @curt > @pret,1,0) as r,
     @pret := @curt,
     @pred := @curd
     from
        Weather w,
        (select 
            @curd := null,
            @pred := null,
            @curt := 0,
            @pret := 0,
            @isH := 0
        ) init
     order by w.RecordDate
    ) t

where
    t.r = 1