-- Создаем функцию. На входе gpa (число), на выходе (RETURNS) — итоговая стипендия (NUMERIC)
CREATE OR REPLACE FUNCTION calculate_scholarship(student_gpa REAL)
RETURNS NUMERIC AS $$
BEGIN
    IF student_gpa >= 4.5 THEN
        RETURN 3000 * 1.5; -- Повышенная стипендия: 4500 руб.
    ELSIF student_gpa >= 4.0 THEN
        RETURN 3000 * 1.2; -- Обычная стипендия: 3600 руб.
    ELSE
        RETURN 3000;       -- Базовая стипендия: 3000 руб.
    END IF;
END;
$$ LANGUAGE plpgsql;

-- Выводим список студентов, их средний балл и рассчитанную функцию стипендии
SELECT name, faculty, gpa, calculate_scholarship(gpa) AS final_scholarship
FROM students;