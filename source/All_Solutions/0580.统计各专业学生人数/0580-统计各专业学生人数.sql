select d.dept_name , count(s.dept_id) 'student_number'
from department d left join student s
on s.dept_id=d.dept_id
group by d.dept_id
order by student_number desc,dept_name;