CREATE TABLE habits (
    id SERIAL PRIMARY KEY,
    habit_name TEXT,
    days_completed INTEGER,
    reward_points INTEGER
);

INSERT INTO habits (habit_name, days_completed, reward_points) VALUES 
('Утренняя зарядка', 14, 140),
('Чтение книг', 5, 50),
('Изучение Python', 21, 420),
('Медитация', 2, 20);



-- Напишите запрос с оператором CASE, который выводит имя привычки и её статус: 
-- если days_completed >= 20 — 'Привычка зафиксирована', от 10 до 19 — 'В процессе', 
-- меньше 10 — 'Только начали'.
SELECT habit_name,
       CASE
           WHEN days_completed >= 20 THEN 'Привычка зафиксирована'
           WHEN days_completed >= 10 THEN 'В процессе'
           ELSE 'Только начали'
       END AS status
FROM habits;

-- Посчитайте общую сумму баллов (SUM), которую заработал пользователь за все свои привычки.
SELECT SUM(reward_points) FROM habits;

-- Напишите выборку привычек, у которых количество выполненных дней (days_completed) 
-- находится в диапазоне от 5 до 15 включительно (используйте BETWEEN).
SELECT * FROM habits
WHERE days_completed BETWEEN 5 AND 15;