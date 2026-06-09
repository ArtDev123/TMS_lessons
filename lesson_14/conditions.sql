-- Ищем студентов Информатики или Экономики, чье имя начинается на 'А' или 'М'
SELECT name, faculty, gpa 
FROM students 
WHERE faculty IN ('Информатика', 'Экономика') 
  AND (name LIKE 'А%' OR name LIKE 'М%');