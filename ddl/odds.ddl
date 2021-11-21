CREATE TABLE IF NOT EXISTS win_odds (
    race_id BIGINT PRIMARY KEY,
    horse_number SMALLINT PRIMARY KEY,
    odds REAL,
    last_updated Timestamp
);

CREATE TABLE IF NOT EXISTS place_odds (
    race_id BIGINT PRIMARY KEY,
    horse_number SMALLINT PRIMARY KEY,
    odds REAL,
    last_updated Timestamp
);

CREATE TABLE IF NOT EXISTS quinella_place_odds (
    race_id BIGINT PRIMARY KEY,
    horse_number SMALLINT PRIMARY KEY,
    odds REAL,
    last_updated Timestamp
);

CREATE TABLE IF NOT EXISTS bracket_quinella_odds (
    race_id BIGINT PRIMARY KEY,
    bracket_number_1 SMALLINT PRIMARY KEY,
    bracket_number_2 SMALLINT PRIMARY KEY,
    odds REAL,
    last_updated Timestamp
);

CREATE TABLE IF NOT EXISTS exacta_odds (
    race_id BIGINT PRIMARY KEY,
    horse_number_1 SMALLINT PRIMARY KEY,
    horse_number_2 SMALLINT PRIMARY KEY,
    odds REAL,
    last_updated Timestamp
);

CREATE TABLE IF NOT EXISTS quinella_odds (
    race_id BIGINT PRIMARY KEY,
    horse_number_1 SMALLINT PRIMARY KEY,
    horse_number_2 SMALLINT PRIMARY KEY,
    odds REAL,
    last_updated Timestamp
);

CREATE TABLE IF NOT EXISTS trifecta_odds (
    race_id BIGINT PRIMARY KEY,
    horse_number_1 SMALLINT PRIMARY KEY,
    horse_number_2 SMALLINT PRIMARY KEY,
    horse_number_3 SMALLINT PRIMARY KEY,
    odds DOUBLE PRECISION,
    last_updated Timestamp
);

