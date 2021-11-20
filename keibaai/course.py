import sqlalchemy
from sqlalchemy import Column, BigInteger, Date, SmallInteger, String
from sqlalchemy.sql.sqltypes import SmallInteger

base = sqlalchemy.orm.declarative_base()

class Course(base):
    __tablename__ = 'courses'

    id = Column(BigInteger, primary_key=True)
    race_course_name = Column(String)
    surface = Column(String)
    distance = Column(SmallInteger)
    rotation = Column(String)
    in_out = Column(String)
    num_of_corners = Column(SmallInteger)

    def __repr__(self):
        return "<Course(race_course_name='%s', distance='%s', surface='%s', rotation='%s')>" % (
                            self.race_course_name, self.distance, self.surface, self.rotation)
