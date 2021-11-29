import sqlalchemy
from sqlalchemy import Column, BigInteger, DateTime, Float, SmallInteger, Numeric

base = sqlalchemy.orm.declarative_base()

class WinOdds(base):
    __tablename__ = 'win_odds'

    race_id = Column(BigInteger, primary_key=True)
    horse_number = Column(SmallInteger, primary_key=True)
    odds = Column(Float)
    last_updated = Column(DateTime)

class PlaceOdds(base):
    __tablename__ = 'place_odds'

    race_id = Column(BigInteger, primary_key=True)
    horse_number = Column(SmallInteger, primary_key=True)
    odds_min = Column(Numeric)
    odds_max = Column(Numeric)
    last_updated = Column(DateTime)

class QuinellaPlaceOdds(base):
    __tablename__ = 'quinella_place_odds'

    race_id = Column(BigInteger, primary_key=True)
    horse_number_1 = Column(SmallInteger, primary_key=True)
    horse_number_2 = Column(SmallInteger, primary_key=True)
    odds_min = Column(Numeric)
    odds_max = Column(Numeric)
    last_updated = Column(DateTime)

class BracketQuinellaOdds(base):
    __tablename__ = 'bracket_quinella_odds'

    race_id = Column(BigInteger, primary_key=True)
    bracket_number_1 = Column(SmallInteger, primary_key=True)
    bracket_number_2 = Column(SmallInteger, primary_key=True)
    odds = Column(Numeric)
    last_updated = Column(DateTime)

class ExactaOdds(base):
    __tablename__ = 'exacta_odds'

    race_id = Column(BigInteger, primary_key=True)
    horse_number_1 = Column(SmallInteger, primary_key=True)
    horse_number_2 = Column(SmallInteger, primary_key=True)
    odds = Column(Numeric)
    last_updated = Column(DateTime)

class QuinellaOdds(base):
    __tablename__ = 'quinella_odds'

    race_id = Column(BigInteger, primary_key=True)
    horse_number_1 = Column(SmallInteger, primary_key=True)
    horse_number_2 = Column(SmallInteger, primary_key=True)
    odds = Column(Numeric)
    last_updated = Column(DateTime)

class TrifectaOdds(base):
    __tablename__ = 'trifecta_odds'

    race_id = Column(BigInteger, primary_key=True)
    horse_number_1 = Column(SmallInteger, primary_key=True)
    horse_number_2 = Column(SmallInteger, primary_key=True)
    horse_number_3 = Column(SmallInteger, primary_key=True)
    odds = Column(Numeric)
    last_updated = Column(DateTime)

class TrioOdds(base):
    __tablename__ = 'trio_odds'

    race_id = Column(BigInteger, primary_key=True)
    horse_number_1 = Column(SmallInteger, primary_key=True)
    horse_number_2 = Column(SmallInteger, primary_key=True)
    horse_number_3 = Column(SmallInteger, primary_key=True)
    odds = Column(Numeric)
    last_updated = Column(DateTime)
