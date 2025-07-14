from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()


DATABASE_URL=os.getenv("DATABASE_URL")
engine=create_engine(DATABASE_URL)
Session_local=sessionmaker(bind=engine,autoflush=False,autocommit=False)
base=declarative_base()
