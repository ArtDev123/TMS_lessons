-- Задания на INNER JOIN и LEFT JOIN

CREATE TABLE departments (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL
);

CREATE TABLE staff (
    id SERIAL PRIMARY KEY,
    fullname TEXT NOT NULL,
    department_id INTEGER REFERENCES departments(id),
    salary REAL
);

INSERT INTO departments (title) VALUES ('Разработка'), ('Маркетинг'), ('HR');
INSERT INTO staff (fullname, department_id, salary) VALUES
('Иванов Иван', 1, 150000),
('Петрова Анна', 1, 165000),
('Сидоров Антон', 2, 90000),
('Кузнецова Елена', 3, 85000);
-- Отдел «Маркетинг» (id=2) имеет только одного сотрудника; отделов без сотрудников нет,
-- но сотрудник без отдела добавим для LEFT JOIN:

INSERT INTO staff (fullname, department_id, salary) VALUES ('Новиков Павел', NULL, 70000);


-- Задание 1: Выведите имя сотрудника, название отдела и зарплату для всех, кто привязан к отделу.
-- Используйте INNER JOIN.
SELECT s.fullname, d.title AS department, s.salary
FROM staff s
INNER JOIN departments d ON d.id = s.department_id;


-- Задание 2: Выведите всех сотрудников, включая тех, у кого department_id = NULL.
-- Для сотрудников без отдела вместо названия выведите 'Без отдела' (через COALESCE).
SELECT s.fullname,
       COALESCE(d.title, 'Без отдела') AS department,
       s.salary
FROM staff s
LEFT JOIN departments d ON d.id = s.department_id;


-- Задание 3: Посчитайте количество сотрудников и среднюю зарплату по каждому отделу.
-- Отделы без сотрудников тоже должны попасть в результат (LEFT JOIN + GROUP BY).
SELECT d.title AS department,
       COUNT(s.id) AS employee_count,
       ROUND(AVG(s.salary)::numeric, 2) AS avg_salary
FROM departments d
LEFT JOIN staff s ON s.department_id = d.id
GROUP BY d.id, d.title;
