-- Задания повышенной сложности: индексы, подзапросы, JOIN и аналитика

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    registered_at DATE
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    category_id INTEGER REFERENCES categories(id),
    price REAL,
    stock INTEGER DEFAULT 0
);

CREATE TABLE purchases (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    item_id INTEGER REFERENCES items(id),
    quantity INTEGER,
    purchased_at DATE
);

INSERT INTO users (username, registered_at) VALUES
('anna_shop', '2024-01-10'),
('petr_buyer', '2024-03-22'),
('olga_new', '2025-01-05');

INSERT INTO categories (name) VALUES ('Электроника'), ('Книги'), ('Одежда');

INSERT INTO items (title, category_id, price, stock) VALUES
('Наушники', 1, 5000, 20),
('Python для начинающих', 2, 1200, 50),
('Футболка', 3, 1500, 0),
('Клавиатура', 1, 3500, 15),
('Дюна (книга)', 2, 800, 30);

INSERT INTO purchases (user_id, item_id, quantity, purchased_at) VALUES
(1, 1, 1, '2024-06-01'),
(1, 2, 2, '2024-06-01'),
(2, 1, 1, '2024-07-15'),
(2, 4, 1, '2024-08-20'),
(1, 5, 1, '2025-02-01');
-- olga_new (id=3) покупок не совершала; «Футболка» ни разу не покупалась


-- Задание 1: Создайте индекс на items(category_id) и составной индекс на purchases(user_id, purchased_at).
-- Затем напишите запрос: для каждого пользователя — логин, дата регистрации,
-- количество покупок и суммарная потраченная сумма (quantity * price).
-- Используйте LEFT JOIN, чтобы показать и пользователей без покупок.
CREATE INDEX idx_items_category ON items(category_id);
CREATE INDEX idx_purchases_user_date ON purchases(user_id, purchased_at);

SELECT u.username,
       u.registered_at,
       COUNT(p.id) AS purchase_count,
       COALESCE(SUM(p.quantity * i.price), 0) AS total_spent
FROM users u
LEFT JOIN purchases p ON p.user_id = u.id
LEFT JOIN items i ON i.id = p.item_id
GROUP BY u.id, u.username, u.registered_at;


-- Задание 2: Выведите товары, которые ни разу не покупались, но есть на складе (stock > 0).
-- Используйте подзапрос с NOT IN или NOT EXISTS.
SELECT i.title, i.price, i.stock
FROM items i
WHERE i.stock > 0
  AND i.id NOT IN (
      SELECT DISTINCT item_id FROM purchases WHERE item_id IS NOT NULL
  );


-- Задание 3: Найдите категории, средний чек покупок в которых выше общего среднего чека по магазину.
-- Средний чек одной покупки = quantity * price.
-- Используйте подзапрос в FROM для статистики по категориям и скалярный подзапрос для общего среднего.
SELECT cat_stats.category_name,
       cat_stats.avg_check
FROM (
    SELECT c.name AS category_name,
           ROUND(AVG(p.quantity * i.price)::numeric, 2) AS avg_check
    FROM purchases p
    JOIN items i ON i.id = p.item_id
    JOIN categories c ON c.id = i.category_id
    GROUP BY c.id, c.name
) AS cat_stats
WHERE cat_stats.avg_check > (
    SELECT ROUND(AVG(p.quantity * i.price)::numeric, 2)
    FROM purchases p
    JOIN items i ON i.id = p.item_id
);
