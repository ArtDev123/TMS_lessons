-- Считаем количество студентов (COUNT) и средний балл (AVG) для каждого факультета
-- В Postgres функция AVG для типа REAL может вернуть много знаков после запятой, 
-- поэтому мы можем использовать ROUND(..., 2) для красоты.
SELECT faculty, 
       COUNT(id) AS total_students, 
       ROUND(AVG(gpa)::numeric, 2) AS average_gpa
FROM students
GROUP BY faculty;