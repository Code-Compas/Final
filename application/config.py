import os
basedir=os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG=False
    SQLITE_DB_DIR=None
    SQLALCHEMY_DATABASE_URI=None
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    
class LocalDevlopmentConfig(Config):
    SQLITE_DB_DIR=os.path.join(basedir,"../db_directory")
    # default local sqlite DB (can be overridden by env var)
    SQLALCHEMY_DATABASE_URI=os.getenv("SQLALCHEMY_DATABASE_URI") or "sqlite:///"+os.path.join(SQLITE_DB_DIR,"projectdb.db")
    DEBUG=True
    
