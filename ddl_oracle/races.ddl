CREATE TABLE races (
    id NUMBER(12),
    name VARCHAR(30) NOT NULL,
    grade VARCHAR(6) NOT NULL,
    race_date DATE NOT NULL,
    race_start TIMESTAMP,
    course_id VARCHAR2(20) NOT NULL,
    weather VARCHAR2(4),
    going VARCHAR2(2),
    race_data VARCHAR2(100),
    corner_order_1 VARCHAR2(60),
    corner_order_2 VARCHAR2(60),
    corner_order_3 VARCHAR2(60),
    corner_order_4 VARCHAR2(60),
    pace CHAR(1),
    PRIMARY KEY (id)
);
