-- Индексы ускоряют поиск и сортировку, но замедляют INSERT/UPDATE/DELETE
-- и занимают дополнительное место на диске.

CREATE TABLE products (
    id SERIAL PRIMARY KEY,          -- PRIMARY KEY автоматически создаёт индекс
    sku TEXT UNIQUE,                -- UNIQUE тоже создаёт индекс
    title TEXT,
    category TEXT,
    price REAL,
    stock INTEGER
);

INSERT INTO products (sku, title, category, price, stock) VALUES
('PHN-001', 'iPhone 15', 'Смартфоны', 90000, 10),
('TAB-002', 'iPad Air', 'Планшеты', 65000, 5),
('NBK-003', 'MacBook Air', 'Ноутбуки', 120000, 3),
('PHN-004', 'Xiaomi 14', 'Смартфоны', 55000, 15);

-- 1. Обычный (B-tree) индекс — для частых фильтров и сортировки по одному столбцу
CREATE INDEX idx_products_category ON products(category);

-- 2. Составной индекс — когда часто ищем по комбинации полей
CREATE INDEX idx_products_category_price ON products(category, price);

-- 3. Частичный индекс — только для подмножества строк (экономит место)
CREATE INDEX idx_products_in_stock ON products(title) WHERE stock > 0;

-- Запросы, которые выиграют от индекса idx_products_category:
SELECT title, price FROM products WHERE category = 'Смартфоны';
SELECT category, AVG(price) FROM products GROUP BY category;

-- Проблемы индексов и как их избежать:
-- • Слишком много индексов на таблице с частыми записями — замедление вставок
-- • Индекс на столбце с малым числом уникальных значений (например, пол «М/Ж») — мало пользы
-- • Индекс не поможет, если в запросе функция над столбцом: WHERE LOWER(title) = 'iphone'
--   (лучше хранить нормализованные данные или создать индекс по выражению)

-- Посмотреть план выполнения запроса (PostgreSQL):
EXPLAIN SELECT * FROM products WHERE category = 'Смартфоны';
