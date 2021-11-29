CREATE TABLE IF NOT EXISTS win_odds (
    race_id NUMBER(12) PRIMARY KEY,
    horse_number NUMBER(2) PRIMARY KEY,
    odds NUMBER(6,1),
    last_updated Timestamp
);

CREATE TABLE IF NOT EXISTS place_odds (
    race_id NUMBER(12) PRIMARY KEY,
    horse_number NUMBER(2) PRIMARY KEY,
    odds_min NUMBER(6,1),
    odds_max NUMBER(6,1),
    last_updated Timestamp
);

CREATE TABLE IF NOT EXISTS quinella_place_odds (
    race_id NUMBER(12) PRIMARY KEY,
    horse_number_1 NUMBER(2) PRIMARY KEY,
    horse_number_2 NUMBER(2) PRIMARY KEY,
    odds_min NUMBER(6,1),
    odds_max NUMBER(6,1),
    last_updated Timestamp
);

CREATE TABLE IF NOT EXISTS bracket_quinella_odds (
    race_id NUMBER(12) PRIMARY KEY,
    bracket_number_1 NUMBER(2) PRIMARY KEY,
    bracket_number_2 NUMBER(2) PRIMARY KEY,
    odds NUMBER(6,1),
    last_updated Timestamp
);

CREATE TABLE IF NOT EXISTS exacta_odds (
    race_id NUMBER(12) PRIMARY KEY,
    horse_number_1 NUMBER(2) PRIMARY KEY,
    horse_number_2 NUMBER(2) PRIMARY KEY,
    odds NUMBER(7,1),
    last_updated Timestamp
);

CREATE TABLE IF NOT EXISTS quinella_odds (
    race_id NUMBER(12) PRIMARY KEY,
    horse_number_1 NUMBER(2) PRIMARY KEY,
    horse_number_2 NUMBER(2) PRIMARY KEY,
    odds NUMBER(6,1),
    last_updated Timestamp
);

CREATE TABLE IF NOT EXISTS trifecta_odds (
    race_id NUMBER(12) PRIMARY KEY,
    horse_number_1 NUMBER(2) PRIMARY KEY,
    horse_number_2 NUMBER(2) PRIMARY KEY,
    horse_number_3 NUMBER(2) PRIMARY KEY,
    odds NUMBER(7,1),
    last_updated Timestamp
);

CREATE TABLE IF NOT EXISTS trio_odds (
    race_id NUMBER(12) PRIMARY KEY,
    horse_number_1 NUMBER(2) PRIMARY KEY,
    horse_number_2 NUMBER(2) PRIMARY KEY,
    horse_number_3 NUMBER(2) PRIMARY KEY,
    odds NUMBER(7,1),
    last_updated Timestamp
);
