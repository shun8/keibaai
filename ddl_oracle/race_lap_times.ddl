CREATE TABLE race_lap_times (
    race_id NUMBER(12),
    lap_distance NUMBER(4),
    lap_time NUMBER(3,1),
    PRIMARY KEY (race_id, lap_distance)
);
