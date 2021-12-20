#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter 'a' from
the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # Using Python array slices and typically in conjunction with ORDER BY
    for instance in session.query(State).order_by(State.id):
        if ('a' in instance.name):
            print("{}: {}".format(instance.id, instance.name))

    session.close()
