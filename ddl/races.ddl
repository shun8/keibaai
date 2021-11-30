CREATE TABLE IF NOT EXISTS races (
    id BIGINT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    grade VARCHAR(6) NOT NULL,
    race_date DATE NOT NULL,
    race_start TIMESTAMP,
    course_id INTEGER NOT NULL,
    weather VARCHAR(4),
    going VARCHAR(2),
    race_data VARCHAR(100),
    corner_order_1 VARCHAR(60),
    corner_order_2 VARCHAR(60),
    corner_order_3 VARCHAR(60),
    corner_order_4 VARCHAR(60),
    pace CHAR(1)
);
