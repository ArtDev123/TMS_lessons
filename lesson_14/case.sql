-- Присваиваем категорию стипендии в зависимости от успеваемости
SELECT name, 
       gpa,
       CASE 
           WHEN gpa >= 4.7 THEN 'Повышенная стипендия'
           WHEN gpa >= 4.0 THEN 'Базовая стипендия'
           ELSE 'Без стипендии'
       END AS scholarship_status
FROM students;