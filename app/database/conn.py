from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import dotenv
import os
from dataclasses import asdict
from common.config import conf

dotenv.load_dotenv()

# TODO split db credentials into env variables
c = conf()
conf_dict = asdict(c)

DB_USERNAME : str = conf_dict.get("DB_USERNAME") #os.getenv("DB_USERNAME") 
DB_PASSWORD : str = conf_dict.get("DB_PASSWORD")
DB_HOST : str = conf_dict.get("DB_HOST")
DB_PORT : str = conf_dict.get("DB_PORT")
DB_DATABASE : str = conf_dict.get("DB_DATABASE")

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}?charset=utf8mb4"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionMaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()