import os
import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

from dotenv import load_dotenv

load_dotenv()
username=os.getenv('MYSQL_USERNAME')
password=os.getenv('MYSQL_PASSWORD')
host=os.getenv('MYSQL_HOST')

# engine = sqlalchemy.create_engine('sqlite:///:memory:')
# engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)
# engine = sqlalchemy.create_engine('sqlite:///test_sqlite2', echo=True)
engine = sqlalchemy.create_engine(f'mysql+pymysql://{username}:{password}@{host}/test_mysql_database2', echo=True)

Base = sqlalchemy.orm.declarative_base()

class Person(Base):
    __tablename__ = 'persons'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(14))

Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

p1 = Person(name='Mike')
session.add(p1)
p2 = Person(name='Nancy')
session.add(p2)
p3 = Person(name='Jun')
session.add(p3)
session.commit()

p4 = session.query(Person).filter_by(name='Mike').first()
p4.name = 'Michel'
session.add(p4)
session.commit()

p5 = session.query(Person).filter_by(name='Nancy').first()
session.delete(p5)
session.commit()

persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)