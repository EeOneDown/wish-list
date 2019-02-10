import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

base = declarative_base()


class Wish(base):
    __tablename__ = "wishes"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    title = sqlalchemy.Column(
        sqlalchemy.String(30), nullable=False, unique=True
    )
    price = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    link = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.Text, nullable=True)

    def __repr__(self):
        return f"Wish(id={self.id}, title={self.title}"


DATABASE_URI = os.getenv("DATABASE_URI",
                         "sqlite:///" + os.path.join(basedir, "app.db"))
engine = sqlalchemy.create_engine(DATABASE_URI)

DBsession = sessionmaker(bind=engine)
session = DBsession()

base.metadata.create_all(engine)
