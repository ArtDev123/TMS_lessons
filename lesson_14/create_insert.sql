-- 1. Создаем таблицу, SERIAL для автоинкремента
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    faculty TEXT,
    gpa REAL
);

-- 2. Заполняем таблицу данными
INSERT INTO students (name, age, faculty, gpa) VALUES 
('Алексей', 20, 'Информатика', 4.8),
('Мария', 21, 'Дизайн', 4.5),
('Иван', 19, 'Информатика', 3.9),
('Елена', 22, 'Экономика', 4.2),
('Пётр', 20, 'Экономика', 3.6);

-- 3. Смотрим, что получилось
SELECT * FROM students;