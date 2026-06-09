CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    fullname TEXT,
    department TEXT,
    salary REAL,
    hire_date DATE -- Используем настоящий тип DATE вместо TEXT
);

INSERT INTO employees (fullname, department, salary, hire_date) VALUES 
('Иванов Иван', 'Разработка', 150000, '2023-01-15'),
('Петрова Анна', 'Разработка', 165000, '2022-05-10'),
('Сидоров Антон', 'Маркетинг', 90000, '2024-02-01'),
('Кузнецова Елена', 'HR', 85000, '2021-11-20'),
('Смирнов Олег', 'Маркетинг', 95000, '2023-08-12');


-- Напишите запрос, который сгруппирует сотрудников 
-- по отделам (department) и для каждого отдела посчитает: количество сотрудников, 
-- среднюю зарплату (округлите до 2 знаков) и минимальную зарплату.
SELECT department,
       COUNT(*) AS employee_count,
       ROUND(AVG(salary)::numeric, 2) AS avg_salary,
       MIN(salary) AS min_salary
FROM employees
GROUP BY department;

-- Модифицируйте предыдущий запрос с помощью ключевого слова HAVING так, 
-- чтобы в итоговой таблице остались только те отделы, где средняя зарплата строго выше 90 000.
SELECT department,
       COUNT(*) AS employee_count,
       ROUND(AVG(salary)::numeric, 2) AS avg_salary,
       MIN(salary) AS min_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 90000;

-- Напишите запрос, выводящий имена и зарплаты сотрудников, 
-- 'которые были приняты на работу после 1 января 2023 года. 
-- В Postgres вы можете сравнивать тип DATE напрямую: WHERE hire_date > '2023-01-01'.
SELECT fullname, salary
FROM employees
WHERE hire_date > '2023-01-01';