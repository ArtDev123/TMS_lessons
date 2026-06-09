CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    title TEXT,
    category TEXT,
    price REAL,
    stock INTEGER
);

INSERT INTO products (title, category, price, stock) VALUES 
('iPhone 15', 'Смартфоны', 90000, 10),
('iPad Air', 'Планшеты', 65000, 5),
('MacBook Air', 'Ноутбуки', 120000, 3),
('Xiaomi 14', 'Смартфоны', 55000, 0);


-- Напишите SELECT-запрос, который выведет товары из категории 'Смартфоны', которые есть в наличии (stock > 0).
SELECT * FROM products
WHERE category = 'Смартфоны' AND stock > 0;

-- Напишите UPDATE-запрос, который снижает цену (price) на все товары из категории 'Планшеты' на 10%.
UPDATE products
SET price = price * 0.9
WHERE category = 'Планшеты';

-- Напишите DELETE-запрос, который удалит из таблицы товары стоимостью более 100 000, которых нет на складе (stock = 0).
DELETE FROM products
WHERE price > 100000 AND stock = 0;