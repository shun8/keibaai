SELECT 'win' AS way
     , TO_CHAR(od.horse_number) AS bet
     , od.odds AS odds
     , rp.first_prob / 100 AS prob
     , (rp.first_prob / 100) * od.odds AS expectation
  FROM win_odds od
 INNER JOIN race_predict rp
    ON od.race_id = rp.race_id
   AND od.horse_number = rp.horse_number
 WHERE (rp.first_prob / 100) * od.odds > 1
UNION ALL
SELECT 'place' AS way
     , TO_CHAR(od.horse_number) AS bet
     , od.odds_min AS odds
     , (rp.first_prob + rp.second_prob + rp.third_prob) / 100 AS prob
     , ((rp.first_prob + rp.second_prob + rp.third_prob) / 100) * od.odds_min AS expectation
  FROM place_odds od
 INNER JOIN race_predict rp
    ON od.race_id = rp.race_id
   AND od.horse_number = rp.horse_number
 WHERE ((rp.first_prob + rp.second_prob + rp.third_prob) / 100) * od.odds_min > 1
 ORDER BY expectation DESC
;