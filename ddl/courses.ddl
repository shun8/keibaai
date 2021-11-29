CREATE TABLE IF NOT EXISTS courses (
    id VARCHAR(20) PRIMARY KEY,
    race_course_name VARCHAR(10) NOT NULL,
    surface CHAR(1) NOT NULL,
    distance SMALLINT NOT NULL,
    rotation CHAR(1) NOT NULL,
    in_out VARCHAR(3),
    num_of_corners SMALLINT
);
