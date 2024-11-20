from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:admin@localhost/restaurant')