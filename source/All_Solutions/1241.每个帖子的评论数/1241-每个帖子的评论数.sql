# Write your MySQL query statement below
SELECT p.post_id, COUNT(DISTINCT(s.sub_id)) AS number_of_comments 
FROM Submissions AS s
RIGHT JOIN(
    SELECT DISTINCT(sub_id) as post_id 
    FROM Submissions
    WHERE parent_id IS NULL
)AS p
ON p.post_id =  s.parent_id
GROUP BY p.post_id
