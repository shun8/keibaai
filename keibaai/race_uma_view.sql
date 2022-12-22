SELECT ru.result
     , ru.bracket_number
     , ru.horse_number
     , ru.gender
     , ru.age
     , ru.weight_to_carry
  FROM race_uma ru
  LEFT OUTER JOIN (
         SELECT t1.uma_id
              , t1.
           FROM race_uma t1
          GROUP BY t1.uma_id
       ) pru
