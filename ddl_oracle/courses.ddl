CREATE TABLE IF NOT EXISTS courses (
    id VARCHAR2(20) PRIMARY KEY,
    race_course_name NVARCHAR2(10) NOT NULL,
    surface NCHAR(1) NOT NULL,
    distance NUMBER(4) NOT NULL,
    rotation NCHAR(1) NOT NULL,
    in_out NVARCHAR2(3),
    num_of_corners NUMBER(1)
);
