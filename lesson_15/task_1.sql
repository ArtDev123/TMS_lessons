-- Задания на ключи и внешние связи

CREATE TABLE publishers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT
);

CREATE TABLE library_books (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    isbn TEXT UNIQUE,
    publisher_id INTEGER REFERENCES publishers(id),
    pages INTEGER
);

INSERT INTO publishers (name, city) VALUES
('Эксмо', 'Москва'),
('АСТ', 'Москва'),
('Питер', 'Санкт-Петербург');

INSERT INTO library_books (title, isbn, publisher_id, pages) VALUES
('Чистый код', '978-5-496-00461-5', 3, 464),
('Изучаем Python', '978-5-97060-336-0', 3, 1280),
('Дюна', '978-5-17-087885-0', 1, 800);


-- Задание 1: Напишите запрос, который выведет название книги, ISBN и название издательства.
-- Используйте INNER JOIN между library_books и publishers.
SELECT b.title, b.isbn, p.name AS publisher
FROM library_books b
INNER JOIN publishers p ON p.id = b.publisher_id;


-- Задание 2: Добавьте в таблицу library_books ограничение NOT NULL для столбца publisher_id
-- через ALTER TABLE (сначала убедитесь, что NULL-значений нет).
ALTER TABLE library_books ALTER COLUMN publisher_id SET NOT NULL;


-- Задание 3: Создайте таблицу authors_books со связью M:N между авторами и книгами:
-- author_id ссылается на новую таблицу authors, book_id — на library_books.
-- Составной PRIMARY KEY (author_id, book_id). Добавьте по 2 автора и свяжите их с книгами.
CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

INSERT INTO authors (name) VALUES ('Роберт Мартин'), ('Марк Лутц'), ('Фрэнк Герберт');

CREATE TABLE authors_books (
    author_id INTEGER REFERENCES authors(id),
    book_id INTEGER REFERENCES library_books(id),
    PRIMARY KEY (author_id, book_id)
);

INSERT INTO authors_books (author_id, book_id) VALUES
(1, 1), (2, 2), (3, 3);

SELECT a.name AS author, b.title AS book
FROM authors a
JOIN authors_books ab ON ab.author_id = a.id
JOIN library_books b ON b.id = ab.book_id;
