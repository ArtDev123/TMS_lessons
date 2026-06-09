-- 1. Добавляем новый столбец для телефона с дефолтным значением
ALTER TABLE students ADD COLUMN phone TEXT DEFAULT 'Не указан';

-- 2. Обновляем данные: повышаем GPA Алексею
UPDATE students 
SET gpa = 5.0 
WHERE name = 'Алексей';

-- 3. Удаляем строки: отчисляем тех, у кого GPA ниже 4.0
DELETE FROM students 
WHERE gpa < 4.0;

-- Смотрим на итоговую таблицу после изменений
SELECT * FROM students;