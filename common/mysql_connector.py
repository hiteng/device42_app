



from sqlalchemy.engine import create_engine
engine = create_engine("mysql+pymysql://hiteng:mysql123@localhost/device42_db?host=localhost?port=3306")
conn = engine.connect()
print conn
