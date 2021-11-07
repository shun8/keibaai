import sqlalchemy
from sqlalchemy import Column, BigInteger, Date, Integer, String

base = sqlalchemy.orm.declarative_base()

class Race(base):
    __tablename__ = 'races'

    cource_id = Column(BigInteger, primary_key=True)
    name = Column(String)
    surface = Column(String)
    distance = Column(Integer)
    rotation = Column(String)



    def __repr__(self):
        return "<Course(name='%s', distance='%s', date='%s')>" % (
                            self.name, self.grade, self.date)