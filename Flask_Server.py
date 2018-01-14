from flask import Flask;
app = Flask(__name__);
from sqlalchemy import create_engine;
from sqlalchemy.orm import sessionmaker;
from database_setup import Base,Person,Address;
from getLatLong import getLatLong

engine = create_engine('sqlite:///sqlalchemy_storage.db');
Base.metadata.bind = engine;
DBSession = sessionmaker(bind=engine);
session = DBSession();
@app.route('/<int:id>')
def getAddress(id):
	persons = session.query(Person).all();
	intendedPerson={};
	#intendedPerson;
	for person in persons:
		if (person.id ==id):
			intendedPerson = person;
			break;
	address = session.query(Address).filter_by(person_id = intendedPerson.id).first();
	print(address.street_name+' '+address.street_number);
	lattitude,longitude =  getLatLong(address.street_name+address.street_number);
	return longitude;

if __name__ == '__main__':
	app.debug = True;
	app.run();