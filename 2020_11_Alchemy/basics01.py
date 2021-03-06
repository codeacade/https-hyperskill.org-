#!/usr/bin/env python
#### source: https://www.youtube.com/watch?v=OT5qJBINiJY

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()   # see line 16 "Session"

class py_User(Base):  # inheritating from Base
  __tablename__ = "sql_tablename"
  py_id = Column('sql_id', Integer, primary_key = True)
  py_username = Column('sql_username', String)

engine = create_engine("sqlite:///d.db", echo = True)
Base.metadata.create_all(bind = engine)


Session = sessionmaker(bind = engine)  # see line 6 "Base"
sess = Session()  # sess-object (class Base) START

while True:
  user = py_User()  # user-object (class py_User < Base)
  user.py_id = int(input())
  user.py_username = input()
  sess.add(user)
  if user.py_id > 100:
    break

sess.commit()  # END OF WRITING

uu = sess.query(py_User).all()  # START OF READING
for i in uu:print(i.py_username)

sess.close() # sess-object (class Base) END
