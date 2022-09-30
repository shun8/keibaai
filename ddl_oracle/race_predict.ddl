CREATE TABLE race_predict (
    race_id CHAR(12),
    bracket_number NUMBER(1),
    horse_number NUMBER(2),
    uma_name VARCHAR2(40),
    first_prob NUMBER(2) DEFAULT 0 NOT NULL,
    second_prob NUMBER(2) DEFAULT 0 NOT NULL,
    third_prob NUMBER(2) DEFAULT 0 NOT NULL,
    PRIMARY KEY (race_id, bracket_number, horse_number)
);
