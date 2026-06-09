ICREATE TABLE players (
    player_id SERIAL PRIMARY KEY,
    nickname TEXT,
    country TEXT,
    level INTEGER,
    playtime_hours REAL,
    is_banned BOOLEAN DEFAULT FALSE -- Используем BOOLEAN вместо INTEGER
);

INSERT INTO players (nickname, country, level, playtime_hours, is_banned) VALUES 
('ShadowKnight', 'Russia', 45, 120.5, FALSE),
('CyberQueen', 'Kazakhstan', 12, 14.2, FALSE),
('ElvenArcher', 'Belarus', 78, 450.0, FALSE),
('TrollFace', 'Russia', 5, 2.1, TRUE),
('DragonSlayer', 'Kazakhstan', 52, 210.8, FALSE),
('SniperPro', 'Russia', 89, 612.4, FALSE);


-- Гео-анализ с исключением: Посчитайте суммарное игровое время (SUM) 
-- и средний уровень игроков для каждой страны. При этом в расчетах не должны участвовать 
-- забаненные пользователи. 
-- (Подсказка: условие фильтрации должно выглядеть как WHERE is_banned = FALSE или просто WHERE NOT is_banned).
SELECT country,
       SUM(playtime_hours) AS total_playtime,
       AVG(level) AS avg_level
FROM players
WHERE NOT is_banned
GROUP BY country;


-- Многоуровневый CASE: Напишите запрос, выводящий nickname и текстовый status_tier. Правила:

-- Если игрок забанен (is_banned = TRUE), то статус всегда 'Блокировка'.

-- Если не забанен и уровень (level) > 60 — 'Элита'.

-- Если не забанен и уровень от 20 до 60 — 'Опытный'.

-- В остальных случаях — 'Новичок'.
SELECT nickname,
       CASE
           WHEN is_banned THEN 'Блокировка'
           WHEN level > 60 THEN 'Элита'
           WHEN level >= 20 THEN 'Опытный'
           ELSE 'Новичок'
       END AS status_tier
FROM players;



-- Очистка базы: Напишите команду удаления (DELETE), 
-- которая уберет из базы всех забаненных игроков, чей уровень меньше 10. 
-- Напишите финальный SELECT * FROM players, чтобы проверить, кто остался в таблице.
DELETE FROM players
WHERE is_banned AND level < 10;

SELECT * FROM players;