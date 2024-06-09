CREATE OR REPLACE VIEW agg_race_first_time AS
SELECT r.course_id
     , g.rank
     , u.age
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
 GROUP BY r.course_id, g.rank, u.age
WITH READ ONLY
;
