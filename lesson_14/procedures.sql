-- Создаем процедуру. На входе — название факультета
CREATE OR REPLACE PROCEDURE celebrate_academic_year(target_faculty TEXT)
AS $$
BEGIN
    -- Обновляем возраст студентов на указанном факультете
    UPDATE students
    SET age = age + 1
    WHERE faculty = target_faculty;
    
    -- Фиксируем изменения в базе данных
    COMMIT;
END;
$$ LANGUAGE plpgsql;

-- 1. Смотрим на возраст студентов факультета 'Информатика' до вызова процедуры
SELECT name, age, faculty FROM students WHERE faculty = 'Информатика';

-- 2. Вызываем процедуру для Информатиков
CALL celebrate_academic_year('Информатика');

-- 3. Проверяем результат — все Информатики стали на год старше
SELECT name, age, faculty FROM students WHERE faculty = 'Информатика';