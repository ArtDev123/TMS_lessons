-- Подзапрос — SELECT внутри другого запроса (в WHERE, FROM, SELECT)

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    fullname TEXT,
    department TEXT,
    salary REAL
);

INSERT INTO employees (fullname, department, salary) VALUES
('Иванов', 'Разработка', 150000),
('Петрова', 'Разработка', 165000),
('Сидоров', 'Маркетинг', 90000),
('Кузнецова', 'HR', 85000),
('Смирнов', 'Маркетинг', 95000);

-- 1. Скалярный подзапрос — возвращает одно значение (в SELECT или WHERE)
SELECT fullname, salary,
       salary - (SELECT AVG(salary) FROM employees) AS diff_from_avg
FROM employees;

-- 2. Подзапрос с IN — «значение входит в набор»
SELECT fullname, department, salary
FROM employees
WHERE department IN (
    SELECT department
    FROM employees
    GROUP BY department
    HAVING AVG(salary) > 100000
);

-- 3. Подзапрос с EXISTS — проверка «существует ли хотя бы одна строка»
CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    name TEXT,
    lead_id INTEGER REFERENCES employees(id)
);

INSERT INTO projects (name, lead_id) VALUES
('Сайт компании', 1),
('Мобильное приложение', 2);

SELECT e.fullname
FROM employees e
WHERE EXISTS (
    SELECT 1 FROM projects p WHERE p.lead_id = e.id
);

-- 4. Подзапрос в FROM (производная таблица) — результат подзапроса как временная таблица
SELECT department, avg_salary
FROM (
    SELECT department, ROUND(AVG(salary)::numeric, 2) AS avg_salary
    FROM employees
    GROUP BY department
) AS dept_stats
WHERE avg_salary > 90000;

-- 5. Коррелированный подзапрос — ссылается на внешний запрос (строка за строкой)
SELECT e1.fullname, e1.department, e1.salary
FROM employees e1
WHERE e1.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.department = e1.department
);
