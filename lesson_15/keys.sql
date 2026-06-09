-- Ключи в базах данных: PRIMARY KEY, FOREIGN KEY, UNIQUE
-- Ключ — поле (или набор полей), по которому строку можно однозначно найти или связать с другой таблицей.

-- 1. PRIMARY KEY — уникальный идентификатор строки (не может повторяться и не может быть NULL)
CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    country TEXT
);

-- 2. UNIQUE — значение должно быть уникальным, но строк может быть много (в отличие от PK)
CREATE TABLE readers (
    id SERIAL PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,  -- два читателя с одним email нельзя
    fullname TEXT
);

-- 3. FOREIGN KEY — ссылка на PRIMARY KEY другой таблицы (связь «многие к одному»)
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    year INTEGER,
    author_id INTEGER REFERENCES authors(id)  -- каждая книга принадлежит одному автору
);

INSERT INTO authors (name, country) VALUES
('Михаил Булгаков', 'Россия'),
('Фёдор Достоевский', 'Россия');

INSERT INTO readers (email, fullname) VALUES
('anna@mail.ru', 'Анна Иванова'),
('petr@mail.ru', 'Пётр Сидоров');

INSERT INTO books (title, year, author_id) VALUES
('Мастер и Маргарита', 1967, 1),
('Преступление и наказание', 1866, 2);

-- Попытка вставить книгу с несуществующим author_id = 99 вызовет ошибку:
-- INSERT INTO books (title, year, author_id) VALUES ('Тест', 2020, 99);

-- 4. Составной PRIMARY KEY — уникальность по комбинации полей
CREATE TABLE book_ratings (
    book_id INTEGER REFERENCES books(id),
    reader_id INTEGER REFERENCES readers(id),
    score INTEGER CHECK (score BETWEEN 1 AND 5),
    PRIMARY KEY (book_id, reader_id)  -- один читатель может оценить книгу только один раз
);

INSERT INTO book_ratings (book_id, reader_id, score) VALUES
(1, 1, 5),
(2, 2, 4);

SELECT * FROM authors;
SELECT * FROM books;
SELECT * FROM book_ratings;
