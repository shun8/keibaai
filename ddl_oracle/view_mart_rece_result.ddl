CREATE OR REPLACE VIEW mart_race_result AS
SELECT r.course_id
     , SUBSTR(r.course_id, 4, 1) AS surface
     , u.gender
     , u.age
     , u.weight_to_carry
     , MIN(u.time) AS min_first
     , MAX(u.time) AS max_first
     , ROUND(AVG(u.time), 2) AS avg_first
     , VARIANCE(u.time) AS variance_first
     , COUNT(*) AS count_first
  FROM races r
 INNER JOIN grade g
    ON r.grade_id = g.id
 INNER JOIN race_uma u
    ON r.id = u.race_id
   AND u.result = 1
 GROUP BY r.course_id, u.gender, u.age, u.weight_to_carry
WITH READ ONLY
;
