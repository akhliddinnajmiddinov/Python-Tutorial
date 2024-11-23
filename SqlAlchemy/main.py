from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import DeclarativeBase, sessionmaker

psql_url = "postgresql+psycopg2://postgres:1423@localhost:5432/namozvaqtibot"

engine = create_engine(psql_url)

class Base(DeclarativeBase):
    pass

class User(Base):
    __table__ = Table("users", Base.metadata, autoload_with=engine)


    def __str__(self):
        return self.chat_id

DBSession = sessionmaker(bind=engine)
session = DBSession()

user1 = User(chat_id = "1231231", region = "Toshkent", town = "Toshkent")
session.add(user1)
session.commit()
print(*session.query(User).all())