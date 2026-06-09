-- Задания на подзапросы

CREATE TABLE menu_items (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT,
    price REAL,
    calories INTEGER
);

INSERT INTO menu_items (name, category, price, calories) VALUES
('Цезарь', 'Салаты', 450, 320),
('Борщ', 'Супы', 380, 280),
('Стейк', 'Горячее', 1200, 650),
('Капучино', 'Напитки', 250, 120),
('Чизкейк', 'Десерты', 400, 480),
('Греческий салат', 'Салаты', 420, 290);


-- Задание 1: Выведите блюда, цена которых выше средней цены по всему меню.
-- Используйте скалярный подзапрос в WHERE.
SELECT name, category, price
FROM menu_items
WHERE price > (SELECT AVG(price) FROM menu_items);


-- Задание 2: Выведите категории, в которых есть хотя бы одно блюдо дороже 500 руб.
-- Используйте подзапрос с IN.
SELECT DISTINCT category
FROM menu_items
WHERE category IN (
    SELECT category
    FROM menu_items
    WHERE price > 500
);


-- Задание 3: Выведите название и калорийность каждого блюда, а также разницу
-- между его калорийностью и средней калорийностью в той же категории.
-- Используйте коррелированный подзапрос.
SELECT m.name,
       m.category,
       m.calories,
       m.calories - (
           SELECT ROUND(AVG(m2.calories)::numeric, 2)
           FROM menu_items m2
           WHERE m2.category = m.category
       ) AS calories_diff_from_category_avg
FROM menu_items m;
