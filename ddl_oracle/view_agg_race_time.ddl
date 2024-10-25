CREATE OR REPLACE VIEW agg_race_time AS
SELECT r.course_id
     , SUBSTR(r.course_id, 4, 1) AS surface
     , u.gender
     , u.age
     , u.weight_to_carry
     , MIN(u.time) AS min_all
     , MAX(u.time) AS max_all
     , ROUND(AVG(u.time), 2) AS avg_all
     , VARIANCE(u.time) AS variance_all
     , COUNT(*) AS count_all
  FROM races r
 INNER JOIN grade g
    ON r.grade_id = g.id
 INNER JOIN race_uma u
    ON r.id = u.race_id
   AND u.result IS NOT NULL
 GROUP BY r.course_id, u.gender, u.age, u.weight_to_carry
WITH READ ONLY
;
