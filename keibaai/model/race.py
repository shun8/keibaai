from re import S
import sqlalchemy
from sqlalchemy import Column, BigInteger, Boolean, Date, Float, Integer, Interval, SmallInteger, String, Time

base = sqlalchemy.orm.declarative_base()

class Race(base):
    __tablename__ = 'races'

    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    grade = Column(String)
    date = Column(Date)
    start = Column(Time)
    course_id = Column(Integer)
    going = Column(String)
    weather = Column(String)
    kai = Column(SmallInteger)
    nichi = Column(SmallInteger)
    handicap = Column(String)
    race_data = Column(String)
    corner_order_1 = Column(String)
    corner_order_2 = Column(String)
    corner_order_3 = Column(String)
    corner_order_4 = Column(String)
    pace = Column(String)

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
    win_odds = Column(Float)
    time = Column(Interval)
    margin = Column(String)
    final_3_furlong = Column(Interval)
    corner_order = Column(String)
    trainer_id = Column(Integer)
    horse_weight = Column(SmallInteger)
    gain_and_loss_weight = Column(SmallInteger)
    is_excluded = Column(String)
    is_demoted = Column(String)

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
