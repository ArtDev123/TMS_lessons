-- Задания повышенной сложности: связи M:N, несколько JOIN, агрегация

CREATE TABLE cinemas (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT
);

CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    genre TEXT,
    duration_min INTEGER
);

-- Связь M:N: фильм показывается в нескольких кинотеатрах, в кинотеатре — несколько фильмов
CREATE TABLE screenings (
    cinema_id INTEGER REFERENCES cinemas(id),
    movie_id INTEGER REFERENCES movies(id),
    show_time TIME,
    ticket_price REAL,
    PRIMARY KEY (cinema_id, movie_id, show_time)
);

INSERT INTO cinemas (name, city) VALUES
('Салют', 'Минск'),
('Победа', 'Минск'),
('Мир', 'Гомель');

INSERT INTO movies (title, genre, duration_min) VALUES
('Дюна: Часть вторая', 'Фантастика', 166),
('Головоломка 2', 'Анимация', 96),
('Дедпул 3', 'Боевик', 128);

INSERT INTO screenings (cinema_id, movie_id, show_time, ticket_price) VALUES
(1, 1, '18:00', 15.00),
(1, 2, '20:30', 12.00),
(2, 1, '19:00', 14.00),
(2, 3, '21:00', 16.00),
(3, 2, '17:00', 10.00);


-- Задание 1: Выведите полное расписание: название кинотеатра, город, фильм, время сеанса и цену.
-- Используйте JOIN трёх таблиц.
SELECT c.name AS cinema,
       c.city,
       m.title AS movie,
       s.show_time,
       s.ticket_price
FROM screenings s
JOIN cinemas c ON c.id = s.cinema_id
JOIN movies m ON m.id = s.movie_id
ORDER BY c.name, s.show_time;


-- Задание 2: Найдите кинотеатры, в которых НЕ показывают фильмы жанра «Боевик».
-- Подсказка: LEFT JOIN + WHERE ... IS NULL или подзапрос с NOT IN / NOT EXISTS.
SELECT c.name, c.city
FROM cinemas c
WHERE c.id NOT IN (
    SELECT s.cinema_id
    FROM screenings s
    JOIN movies m ON m.id = s.movie_id
    WHERE m.genre = 'Боевик'
);


-- Задание 3: Для каждого города выведите количество уникальных фильмов и среднюю цену билета.
-- Учитывайте только кинотеатры, где есть хотя бы один сеанс.
-- Отсортируйте по средней цене по убыванию.
SELECT c.city,
       COUNT(DISTINCT s.movie_id) AS unique_movies,
       ROUND(AVG(s.ticket_price)::numeric, 2) AS avg_ticket_price
FROM cinemas c
JOIN screenings s ON s.cinema_id = c.id
GROUP BY c.city
ORDER BY avg_ticket_price DESC;
