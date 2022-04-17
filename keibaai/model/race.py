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
        return "<Race(name='%s', grade='%s', date='%s')>" % (
                            self.name, self.grade, self.date)

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
        return "<RaceUma(bracket_number='%s', horse_number='%s', result='%s')>" % (
                            self.bracket_number, self.horse_number, self.result)

class RaceLapTimes(base):
    __tablename__ = 'race_lap_times'

    race_id = Column(BigInteger, primary_key=True)
    lap_distance = Column(SmallInteger, primary_key=True)
    lap_time = Column(Float)

    def __repr__(self):
        return "<RaceUma(lap_distance='%s', lap_time='%s'>" % (
                            self.lap_distance, self.lap_time)
