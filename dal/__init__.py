

from sqlalchemy.ext.declarative import declarative_base
from device42_app.common.mysql_connector import engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

Session = sessionmaker(bind=engine)


