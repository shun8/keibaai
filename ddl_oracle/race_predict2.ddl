CREATE TABLE race_predict2 (
    race_id CHAR(12),
    way VARCHAR2(20),
    first NUMBER(2) DEFAULT 0 NOT NULL,
    second NUMBER(2) DEFAULT 0 NOT NULL,
    third NUMBER(2) DEFAULT 0 NOT NULL,
    prob NUMBER(16,15),
    PRIMARY KEY (race_id, way, first, second, third)
);
