from sqlalchemy import create_engine, Table, MetaData, insert
from sqlalchemy.orm import DeclarativeBase, sessionmaker

psql_url = "postgresql+psycopg2://postgres:1423@localhost:5432/namozvaqtibot"

engine = create_engine(psql_url)

conn = engine.connect()

metadata = MetaData()

User = Table("users", metadata, autoload_with=engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()


user1 = User.insert().values(chat_id = "111122111", region = "Toshkent", town = "Toshkent")
# user1.compile()
res = conn.execute(user1)
# print(user1)
print(res)
# session.add(user1)
session.commit()

# print(session.query(User).all()[0].region)
# print(session.query(User).all())
print()
result = conn.execute(User.select()).fetchone()
print(result)