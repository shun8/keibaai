CREATE TABLE IF NOT EXISTS race_lap_times (
    race_id BIGINT PRIMARY KEY,
    lap_distance SMALLINT PRIMARY_KEY,
    lap_time INTERVAL MINUTE TO SECOND(1)
);
