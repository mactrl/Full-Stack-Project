from sqlalchemy import create_engine;
from sqlalchemy.orm import sessionmaker;
from database_setup import Address,Base,Person;
engine = create_engine('sqlite:///sqlalchemy_storage.db');
Base.metadata.bind = engine;
DBSession = sessionmaker(bind=engine);
session = DBSession();
new_person = Person(name = 'DEVODYUTI MUKHERJEE');
session.add(new_person);
session.commit();
new_address = Address(street_name = '1600',street_number = 'Amphitheatre+Parkway,+Mountain+View,+CA',Post_Code = '',person = new_person);
session.add(new_address);
session.commit()