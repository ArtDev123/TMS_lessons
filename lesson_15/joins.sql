-- JOIN — объединение данных из нескольких таблиц по общему ключу

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    product TEXT,
    amount REAL,
    order_date DATE
);

INSERT INTO customers (name) VALUES ('Анна'), ('Пётр'), ('Ольга');
INSERT INTO orders (customer_id, product, amount, order_date) VALUES
(1, 'Клавиатура', 3500, '2025-03-01'),
(1, 'Мышь', 1200, '2025-03-15'),
(2, 'Монитор', 18000, '2025-02-10');
-- У Ольги (id=3) заказов нет — удобно для демонстрации LEFT JOIN

-- 1. INNER JOIN — только строки, где есть совпадение в обеих таблицах
SELECT c.name, o.product, o.amount
FROM customers c
INNER JOIN orders o ON o.customer_id = c.id;

-- 2. LEFT JOIN — все строки из левой таблицы + совпадения справа (или NULL)
SELECT c.name, o.product, o.amount
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id;

-- 3. RIGHT JOIN — все строки из правой таблицы + совпадения слева
SELECT c.name, o.product, o.amount
FROM customers c
RIGHT JOIN orders o ON o.customer_id = c.id;

-- 4. FULL OUTER JOIN — все строки из обеих таблиц
SELECT c.name, o.product, o.amount
FROM customers c
FULL OUTER JOIN orders o ON o.customer_id = c.id;

-- 5. CROSS JOIN — декартово произведение (каждая строка с каждой)
-- SELECT c.name, o.product FROM customers c CROSS JOIN orders o;

-- 6. Несколько JOIN в одном запросе (пример с тремя таблицами)
CREATE TABLE order_statuses (
    order_id INTEGER PRIMARY KEY REFERENCES orders(id),
    status TEXT
);

INSERT INTO order_statuses (order_id, status) VALUES
(1, 'доставлен'), (2, 'в пути'), (3, 'доставлен');

SELECT c.name, o.product, o.amount, s.status
FROM customers c
JOIN orders o ON o.customer_id = c.id
JOIN order_statuses s ON s.order_id = o.id;
