CREATE TABLE win_odds (
    race_id NUMBER(12),
    horse_number NUMBER(2),
    odds NUMBER(6,1),
    last_updated TIMESTAMP,
    PRIMARY KEY (race_id, horse_number)
);

CREATE TABLE place_odds (
    race_id NUMBER(12),
    horse_number NUMBER(2),
    odds_min NUMBER(6,1),
    odds_max NUMBER(6,1),
    last_updated TIMESTAMP,
    PRIMARY KEY (race_id, horse_number)
);

CREATE TABLE quinella_place_odds (
    race_id NUMBER(12),
    horse_number_1 NUMBER(2),
    horse_number_2 NUMBER(2),
    odds_min NUMBER(6,1),
    odds_max NUMBER(6,1),
    last_updated TIMESTAMP,
    PRIMARY KEY (race_id, horse_number_1, horse_number_2)
);

CREATE TABLE bracket_quinella_odds (
    race_id NUMBER(12),
    bracket_number_1 NUMBER(1),
    bracket_number_2 NUMBER(1),
    odds NUMBER(6,1),
    last_updated TIMESTAMP,
    PRIMARY KEY (race_id, bracket_number_1, bracket_number_2)
);

CREATE TABLE exacta_odds (
    race_id NUMBER(12),
    horse_number_1 NUMBER(2),
    horse_number_2 NUMBER(2),
    odds NUMBER(6,1),
    last_updated TIMESTAMP,
    PRIMARY KEY (race_id, horse_number_1, horse_number_2)
);

CREATE TABLE quinella_odds (
    race_id NUMBER(12),
    horse_number_1 NUMBER(2),
    horse_number_2 NUMBER(2),
    odds NUMBER(6,1),
    last_updated TIMESTAMP,
    PRIMARY KEY (race_id, horse_number_1, horse_number_2)
);

CREATE TABLE trifecta_odds (
    race_id NUMBER(12),
    horse_number_1 NUMBER(2),
    horse_number_2 NUMBER(2),
    horse_number_3 NUMBER(2),
    odds NUMBER(7,1),
    last_updated TIMESTAMP,
    PRIMARY KEY (race_id, horse_number_1, horse_number_2, horse_number_3)
);

CREATE TABLE trio_odds (
    race_id NUMBER(12),
    horse_number_1 NUMBER(2),
    horse_number_2 NUMBER(2),
    horse_number_3 NUMBER(2),
    odds NUMBER(6,1),
    last_updated TIMESTAMP,
    PRIMARY KEY (race_id, horse_number_1, horse_number_2, horse_number_3)
);
