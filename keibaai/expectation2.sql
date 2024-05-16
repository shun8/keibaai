SELECT rp.race_id AS race_id
     , rp.way AS way
     , rp.first AS first
     , rp.second AS second
     , rp.third AS third
     , rp.prob AS prob
     , od.odds AS odds
     , rp.prob * od.odds AS expectation
  FROM win_odds od
 INNER JOIN race_predict2 rp
    ON rp.way = 'win'
   AND od.race_id = rp.race_id
   AND od.horse_number = rp.first
UNION ALL
SELECT rp.race_id AS race_id
     , rp.way AS way
     , rp.first AS first
     , rp.second AS second
     , rp.third AS third
     , rp.prob AS prob
     , od.odds AS odds
     , rp.prob * od.odds AS expectation
  FROM place_odds od
 INNER JOIN race_predict2 rp
    ON rp.way = 'place'
   AND od.race_id = rp.race_id
   AND od.horse_number = rp.first
UNION ALL
SELECT rp.race_id AS race_id
     , rp.way AS way
     , rp.first AS first
     , rp.second AS second
     , rp.third AS third
     , rp.prob AS prob
     , od.odds AS odds
     , rp.prob * od.odds AS expectation
  FROM quinella_place_odds od
 INNER JOIN race_predict2 rp
    ON rp.way = 'quinella_place'
   AND od.race_id = rp.race_id
   AND od.horse_number_1 = rp.first
   AND od.horse_number_2 = rp.second
UNION ALL
SELECT rp.race_id AS race_id
     , rp.way AS way
     , rp.first AS first
     , rp.second AS second
     , rp.third AS third
     , rp.prob AS prob
     , od.odds AS odds
     , rp.prob * od.odds AS expectation
  FROM bracket_quinella_odds od
 INNER JOIN race_predict2 rp
    ON rp.way = 'bracket_quinella'
   AND od.race_id = rp.race_id
   AND od.bracket_number_1 = rp.first
   AND od.bracket_number_2 = rp.second
UNION ALL
SELECT rp.race_id AS race_id
     , rp.way AS way
     , rp.first AS first
     , rp.second AS second
     , rp.third AS third
     , rp.prob AS prob
     , od.odds AS odds
     , rp.prob * od.odds AS expectation
  FROM exacta_odds od
 INNER JOIN race_predict2 rp
    ON rp.way = 'exacta'
   AND od.race_id = rp.race_id
   AND od.horse_number_1 = rp.first
   AND od.horse_number_2 = rp.second
UNION ALL
SELECT rp.race_id AS race_id
     , rp.way AS way
     , rp.first AS first
     , rp.second AS second
     , rp.third AS third
     , rp.prob AS prob
     , od.odds AS odds
     , rp.prob * od.odds AS expectation
  FROM quinella_odds od
 INNER JOIN race_predict2 rp
    ON rp.way = 'quinella'
   AND od.race_id = rp.race_id
   AND od.horse_number_1 = rp.first
   AND od.horse_number_2 = rp.second
UNION ALL
SELECT rp.race_id AS race_id
     , rp.way AS way
     , rp.first AS first
     , rp.second AS second
     , rp.third AS third
     , rp.prob AS prob
     , od.odds AS odds
     , rp.prob * od.odds AS expectation
  FROM trifecta_odds od
 INNER JOIN race_predict2 rp
    ON rp.way = 'trifecta'
   AND od.race_id = rp.race_id
   AND od.horse_number_1 = rp.first
   AND od.horse_number_2 = rp.second
   AND od.horse_number_3 = rp.third
UNION ALL
SELECT rp.race_id AS race_id
     , rp.way AS way
     , rp.first AS first
     , rp.second AS second
     , rp.third AS third
     , rp.prob AS prob
     , od.odds AS odds
     , rp.prob * od.odds AS expectation
  FROM trio_odds od
 INNER JOIN race_predict2 rp
    ON rp.way = 'trio'
   AND od.race_id = rp.race_id
   AND od.horse_number_1 = rp.first
   AND od.horse_number_2 = rp.second
   AND od.horse_number_3 = rp.third
 ORDER BY expectation DESC
;
