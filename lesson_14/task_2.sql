CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title TEXT,
    author TEXT,
    year INTEGER,
    rating REAL
);

INSERT INTO books (title, author, year, rating) VALUES 
('Мастер и Маргарита', 'Михаил Булгаков', 1967, 4.9),
('Преступление и наказание', 'Фёдор Достоевский', 1866, 4.7),
('Дюна', 'Фрэнк Герберт', 1965, 4.5),
('Понедельник начинается в субботу', 'Братья Стругацкие', 1965, 4.8);


-- Используя оператор LIKE, напишите запрос, выводящий книги авторов, чья фамилия/имя заканчивается на 'ские' или 'ский'.
SELECT * FROM books
WHERE author LIKE '%ские' OR author LIKE '%ский';

-- Напишите запрос, который находит минимальный (самый старый) год издания книги и максимальный рейтинг среди всех книг.
SELECT MIN(year), MAX(rating) FROM books;

-- Добавьте в таблицу новое текстовое поле genre со значением по умолчанию 'Классика', используя команду ALTER TABLE.
ALTER TABLE books ADD COLUMN genre TEXT DEFAULT 'Классика';