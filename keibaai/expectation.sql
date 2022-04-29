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
UNION ALL
SELECT 'quinella_place' AS way
     , TO_CHAR(od.horse_number_1) || '-' || TO_CHAR(od.horse_number_2) AS bet
     , od.odds_min AS odds
     , ((rp1.first_prob + rp1.second_prob + rp1.third_prob) / 100) * ((rp2.first_prob + rp2.second_prob + rp2.third_prob) / 100) AS prob
     , ((rp1.first_prob + rp1.second_prob + rp1.third_prob) / 100) * ((rp2.first_prob + rp2.second_prob + rp2.third_prob) / 100) * od.odds_min AS expectation
  FROM quinella_place_odds od
 INNER JOIN race_predict rp1
    ON od.race_id = rp1.race_id
   AND od.horse_number_1 = rp1.horse_number
 INNER JOIN race_predict rp2
    ON od.race_id = rp2.race_id
   AND od.horse_number_2 = rp2.horse_number
 WHERE ((rp1.first_prob + rp1.second_prob + rp1.third_prob) / 100) * ((rp2.first_prob + rp2.second_prob + rp2.third_prob) / 100) * od.odds_min > 1
UNION ALL
SELECT 'exacta' AS way
     , TO_CHAR(od.horse_number_1) || '-' || TO_CHAR(od.horse_number_2) AS bet
     , od.odds AS odds
     , (rp1.first_prob / 100) * (rp2.second_prob / 100) AS prob
     , (rp1.first_prob / 100) * (rp2.second_prob / 100) * od.odds AS expectation
  FROM exacta_odds od
 INNER JOIN race_predict rp1
    ON od.race_id = rp1.race_id
   AND od.horse_number_1 = rp1.horse_number
 INNER JOIN race_predict rp2
    ON od.race_id = rp2.race_id
   AND od.horse_number_2 = rp2.horse_number
 WHERE (rp1.first_prob / 100) * (rp2.second_prob / 100) * od.odds > 1
UNION ALL
SELECT 'quinella' AS way
     , TO_CHAR(od.horse_number_1) || '-' || TO_CHAR(od.horse_number_2) AS bet
     , od.odds AS odds
     , (rp1.first_prob / 100) * (rp2.second_prob / 100) + (rp1.second_prob / 100) * (rp2.first_prob / 100) AS prob
     , ((rp1.first_prob / 100) * (rp2.second_prob / 100) + (rp1.second_prob / 100) * (rp2.first_prob / 100)) * od.odds AS expectation
  FROM quinella_odds od
 INNER JOIN race_predict rp1
    ON od.race_id = rp1.race_id
   AND od.horse_number_1 = rp1.horse_number
 INNER JOIN race_predict rp2
    ON od.race_id = rp2.race_id
   AND od.horse_number_2 = rp2.horse_number
 WHERE ((rp1.first_prob / 100) * (rp2.second_prob / 100) + (rp1.second_prob / 100) * (rp2.first_prob / 100)) * od.odds > 1
UNION ALL
SELECT 'trifecta' AS way
     , TO_CHAR(od.horse_number_1) || '-' || TO_CHAR(od.horse_number_2) || '-' || TO_CHAR(od.horse_number_3) AS bet
     , od.odds AS odds
     , (rp1.first_prob / 100) * (rp2.second_prob / 100) * (rp3.third_prob / 100) AS prob
     , (rp1.first_prob / 100) * (rp2.second_prob / 100) * (rp3.third_prob / 100) * od.odds AS expectation
  FROM trifecta_odds od
 INNER JOIN race_predict rp1
    ON od.race_id = rp1.race_id
   AND od.horse_number_1 = rp1.horse_number
 INNER JOIN race_predict rp2
    ON od.race_id = rp2.race_id
   AND od.horse_number_2 = rp2.horse_number
 INNER JOIN race_predict rp3
    ON od.race_id = rp3.race_id
   AND od.horse_number_3 = rp3.horse_number
 WHERE (rp1.first_prob / 100) * (rp2.second_prob / 100) * (rp3.third_prob / 100) * od.odds > 1
UNION ALL
SELECT 'trio' AS way
     , TO_CHAR(od.horse_number_1) || '-' || TO_CHAR(od.horse_number_2) || '-' || TO_CHAR(od.horse_number_3) AS bet
     , od.odds AS odds
     , (rp1.first_prob / 100) * (rp2.second_prob / 100) * (rp3.third_prob / 100)
        + (rp1.first_prob / 100) * (rp3.second_prob / 100) * (rp2.third_prob / 100)
        + (rp2.first_prob / 100) * (rp1.second_prob / 100) * (rp3.third_prob / 100)
        + (rp2.first_prob / 100) * (rp3.second_prob / 100) * (rp1.third_prob / 100)
        + (rp3.first_prob / 100) * (rp1.second_prob / 100) * (rp2.third_prob / 100)
        + (rp3.first_prob / 100) * (rp2.second_prob / 100) * (rp1.third_prob / 100) AS prob
     , ((rp1.first_prob / 100) * (rp2.second_prob / 100) * (rp3.third_prob / 100)
        + (rp1.first_prob / 100) * (rp3.second_prob / 100) * (rp2.third_prob / 100)
        + (rp2.first_prob / 100) * (rp1.second_prob / 100) * (rp3.third_prob / 100)
        + (rp2.first_prob / 100) * (rp3.second_prob / 100) * (rp1.third_prob / 100)
        + (rp3.first_prob / 100) * (rp1.second_prob / 100) * (rp2.third_prob / 100)
        + (rp3.first_prob / 100) * (rp2.second_prob / 100) * (rp1.third_prob / 100)) * od.odds AS expectation
  FROM trio_odds od
 INNER JOIN race_predict rp1
    ON od.race_id = rp1.race_id
   AND od.horse_number_1 = rp1.horse_number
 INNER JOIN race_predict rp2
    ON od.race_id = rp2.race_id
   AND od.horse_number_2 = rp2.horse_number
 INNER JOIN race_predict rp3
    ON od.race_id = rp3.race_id
   AND od.horse_number_3 = rp3.horse_number
 WHERE ((rp1.first_prob / 100) * (rp2.second_prob / 100) * (rp3.third_prob / 100)
        + (rp1.first_prob / 100) * (rp3.second_prob / 100) * (rp2.third_prob / 100)
        + (rp2.first_prob / 100) * (rp1.second_prob / 100) * (rp3.third_prob / 100)
        + (rp2.first_prob / 100) * (rp3.second_prob / 100) * (rp1.third_prob / 100)
        + (rp3.first_prob / 100) * (rp1.second_prob / 100) * (rp2.third_prob / 100)
        + (rp3.first_prob / 100) * (rp2.second_prob / 100) * (rp1.third_prob / 100)) * od.odds > 1
UNION ALL
 ORDER BY expectation DESC
;
