-- Связи в реляционных базах данных
-- 1:1 — одна запись в таблице A соответствует одной записи в таблице B
-- 1:N — одна запись в A связана с несколькими в B (самый частый случай)
-- M:N — много записей в A связаны со многими в B (нужна промежуточная таблица)

-- --- Связь 1:N: один преподаватель — много курсов ---
CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    teacher_id INTEGER REFERENCES teachers(id)
);

INSERT INTO teachers (name) VALUES ('Иванова'), ('Петров');
INSERT INTO courses (title, teacher_id) VALUES
('Python для начинающих', 1),
('SQL и базы данных', 1),
('Веб-разработка', 2);

-- --- Связь M:N: студенты записываются на несколько курсов, на курс — несколько студентов ---
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

-- Промежуточная (связующая) таблица — хранит пары student_id + course_id
CREATE TABLE enrollments (
    student_id INTEGER REFERENCES students(id),
    course_id INTEGER REFERENCES courses(id),
    enrolled_at DATE DEFAULT CURRENT_DATE,
    PRIMARY KEY (student_id, course_id)
);

INSERT INTO students (name) VALUES ('Алексей'), ('Мария'), ('Иван');
INSERT INTO enrollments (student_id, course_id) VALUES
(1, 1), (1, 2),   -- Алексей на двух курсах
(2, 1),           -- Мария на Python
(3, 2), (3, 3);   -- Иван на SQL и Веб

-- Когда использовать какую связь:
-- 1:1  — паспортные данные отдельно от профиля пользователя
-- 1:N  — автор и его книги, отдел и сотрудники
-- M:N  — студенты и курсы, товары и заказы (через таблицу позиций)

SELECT t.name AS teacher, c.title AS course
FROM teachers t
JOIN courses c ON c.teacher_id = t.id;

SELECT s.name AS student, c.title AS course
FROM students s
JOIN enrollments e ON e.student_id = s.id
JOIN courses c ON c.id = e.course_id;
