SELECT *
  FROM race_uma ru
 INNER JOIN races r
    ON ru.race_id = r.id
 WHERE r.name = '有馬記念'
 ORDER BY ru.result
;