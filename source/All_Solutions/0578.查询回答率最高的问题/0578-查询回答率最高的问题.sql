# Write your MySQL query statement below
SELECT question_id survey_log FROM survey_log 
WHERE answer_id IS NOT NULL
GROUP BY question_id
ORDER BY COUNT(answer_id) DESC
LIMIT 1
