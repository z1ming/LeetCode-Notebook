select 
    * ,
    (
    case
        when x+y>z and x+z>y and y+z>x then 'Yes'
        else 'No'
    end
    )triangle
from
    triangle