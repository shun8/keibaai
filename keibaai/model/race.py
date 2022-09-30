from re import S
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BigInteger, Date, Float, Integer, Interval, SmallInteger, String, Time

base = declarative_base()


class Race(base):
    __tablename__ = 'races'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(30))
    race_track_id = Column(SmallInteger)
    kai = Column(SmallInteger)
    nichi = Column(SmallInteger)
    race_no = Column(SmallInteger)
    course_id = Column(String(20))
    grade_id = Column(SmallInteger)
    is_win5 = Column(String(1))
    condition = Column(String(10))
    handicap = Column(String(2))
    race_date = Column(Date)
    race_start = Column(String(5))
    weather = Column(String(4))
    going = Column(String(2))
    num_of_horses = Column(SmallInteger)
    race_data = Column(String(100))
    corner_order_1 = Column(String(60))
    corner_order_2 = Column(String(60))
    corner_order_3 = Column(String(60))
    corner_order_4 = Column(String(60))
    pace = Column(String(1))

    def __repr__(self):
        return "<Race(id='%s', name='%s', race_track_id='%s', kai='%s', nichi='%s', race_no='%s', course_id='%s', grade_id='%s', is_win5='%s', condition='%s', handicap='%s', race_date='%s', race_start='%s', weather='%s', going='%s', num_of_horses='%s', race_data='%s', corner_order_1='%s', corner_order_2='%s', corner_order_3='%s', corner_order_4='%s', pace='%s')>" % (
                self.id, self.name, self.race_track_id, self.kai, self.nichi, self.race_no, self.course_id, self.grade_id, self.is_win5, self.condition, self.handicap, self.race_date, self.race_start, self.weather, self.going, self.num_of_horses, self.race_data, self.corner_order_1, self.corner_order_2, self.corner_order_3, self.corner_order_4, self.pace)

class RaceUma(base):
    __tablename__ = 'race_uma'

    race_id = Column(BigInteger, primary_key=True)
    uma_id = Column(BigInteger, primary_key=True)
    result = Column(SmallInteger)
    bracket_number = Column(SmallInteger)
    horse_number = Column(SmallInteger)
    gender = Column(String)
    age = Column(SmallInteger)
    weight_to_carry = Column(Float)
    jockey_id = Column(Integer)
    time = Column(Interval)
    margin = Column(String)
    ninki = Column(SmallInteger)
    win_odds = Column(Float)
    final_3_furlong = Column(Interval)
    corner_order = Column(String)
    trainer_id = Column(Integer)
    horse_weight = Column(SmallInteger)
    gain_and_loss_weight = Column(SmallInteger)
    is_excluded = Column(String, default="0")
    is_demoted = Column(String, default="0")

    def __repr__(self):
        return "<RaceUma(race_id='%s', uma_id='%s', result='%s', bracket_number='%s', horse_number='%s', gender='%s', age='%s', weight_to_carry='%s', jockey_id='%s', time='%s', margin='%s', ninki='%s', win_odds='%s', final_3_furlong='%s', corner_order='%s', trainer_id='%s', horse_weight='%s', gain_and_loss_weight='%s', is_excluded='%s', is_demoted='%s')>" % (
                self.race_id, self.uma_id, self.result, self.bracket_number, self.horse_number, self.gender, self.age, self.weight_to_carry, self.jockey_id, self.time, self.margin, self.ninki, self.win_odds, self.final_3_furlong, self.corner_order, self.trainer_id, self.horse_weight, self.gain_and_loss_weight, self.is_excluded, self.is_demoted)

class RaceLapTimes(base):
    __tablename__ = 'race_lap_times'

    race_id = Column(BigInteger, primary_key=True)
    lap_distance = Column(SmallInteger, primary_key=True)
    lap_time = Column(Float)

    def __repr__(self):
        return "<RaceLapTimes(race_id='%s', lap_distance='%s', lap_time='%s'>" % (
                self.race_id, self.lap_distance, self.lap_time)
