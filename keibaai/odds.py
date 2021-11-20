import sqlalchemy
from sqlalchemy import Column, BigInteger, DateTime, SmallInteger, String, Numeric

base = sqlalchemy.orm.declarative_base()

class Win(base):
    __tablename__ = 'odds_win'

    race_id = Column(BigInteger, primary_key=True)
    bracket_number = Column(SmallInteger)
    horse_number = Column(SmallInteger)
    odds = Column(Numeric)
    last_updated = Column(DateTime)

