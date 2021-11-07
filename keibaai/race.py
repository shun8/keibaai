import sqlalchemy
from sqlalchemy import Column, BigInteger, Date, Integer, String, Time

base = sqlalchemy.orm.declarative_base()

class Race(base):
    __tablename__ = 'races'

    race_id = Column(BigInteger, primary_key=True)
    name = Column(String)
    grade = Column(String)
    date = Column(Date)
    start = Column(Time)
    course_id = Column(Integer)
    surface_condition = Column(String)
    weather = Column(String)
    


    

    def __repr__(self):
        return "<Race(name='%s', grade='%s', date='%s')>" % (
                            self.name, self.grade, self.date)