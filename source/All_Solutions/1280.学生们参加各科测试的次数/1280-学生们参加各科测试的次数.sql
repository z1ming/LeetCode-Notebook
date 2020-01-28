select s1.student_id, s1.student_name, s2.subject_name, count(e.subject_name) attended_exams
from Students s1
join Subjects s2
left join 
Examinations e
on s1.student_id=e.student_id and s2.subject_name=e.subject_name
group by s1.student_id, s2.subject_name;