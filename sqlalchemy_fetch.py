from sqlalchemy import create_engine;
from database_setup import Base,Person,Address;
from sqlalchemy.orm import sessionmaker;

engine = create_engine('sqlite:///sqlalchemy_storage.db');
Base.metadata.bind = engine;
DBSession = sessionmaker(bind = engine);
session = DBSession();
person  = session.query(Person).all();
for i in person:
	print(i.id);
