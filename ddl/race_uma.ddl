CREATE TABLE IF NOT EXISTS race_uma (
    race_id BIGINT PRIMARY KEY,
    uma_id BIGINT PRIMARY KEY,
    result SMALLINT,
    bracket_number SMALLINT,
    horse_number SMALLINT,
    gender CHAR(1) NOT NULL,
    age SMALLINT NOT NULL,
    weight_to_carry REAL,
    jockey_id INTEGER,
    win_odds REAL,
    time INTERVAL MINUTE TO SECOND(1),
    margin VARCHAR(6),
    final_3_furlong INTERVAL MINUTE TO SECOND(1),
    corner_order VARCHAR(12),
    trainer_id INTEGER NOT NULL,
    horse_weight SMALLINT,
    gain_and_loss_weight SMALLINT,
    is_excluded BOOLEAN,
    is_demoted BOOLEAN
);