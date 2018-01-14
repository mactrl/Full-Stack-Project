import os;
import sys;
from sqlalchemy import Column,Integer,String,ForeignKey;
from sqlalchemy.orm import relationship;
from sqlalchemy.ext.declarative import declarative_base;
from sqlalchemy import create_engine;
Base = declarative_base();
class Person(Base):
	__tablename__ = 'person';
	id = Column(Integer,primary_key = True);
	name = Column(String(250),nullable = False);
class Address(Base):
	__tablename__ = 'address';
	id = Column(Integer,primary_key=True);
	street_name = Column(String(250));
	street_number = Column(String(250));
	Post_Code = Column(String(250),nullable=False);
	person_id = Column(Integer,ForeignKey('person.id'));
	person = relationship(Person);
engine = create_engine('sqlite:///sqlalchemy_storage.db');
Base.metadata.create_all(engine);


