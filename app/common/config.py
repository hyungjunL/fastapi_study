from dataclasses import dataclass, asdict
from os import path, environ
import dotenv
import os

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))

dotenv.load_dotenv()

@dataclass
class Config:
    BASE_DIR = base_dir 
    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True

@dataclass
class LocalConfig(Config):
    #DB_URL: str = "mysql+pymysql://root:1234@localhost/rgt?charset=utf8mb4"
    DB_USERNAME : str = os.getenv("DB_USERNAME") 
    DB_PASSWORD : str = os.getenv("DB_PASSWORD")
    DB_HOST : str = os.getenv("DB_HOST")
    DB_PORT : str = os.getenv("DB_PORT")
    DB_DATABASE : str = os.getenv("DB_DATABASE")
    DB_URL : str = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}?charset=utf8mb4"
    PROJ_RELOAD: bool = True


@dataclass
class ProdConfig(Config):
    PROJ_RELOAD: bool = False


def conf():
    config = dict(prod=ProdConfig(), local=LocalConfig())
    return config.get(environ.get("API_ENV", os.getenv("PROFILES")))