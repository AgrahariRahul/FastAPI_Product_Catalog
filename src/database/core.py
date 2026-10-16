from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base,Session
from src.config import settings



engine = create_engine(url=settings.db_url)

SessionLocal =sessionmaker(bind=engine,autoflush=False)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    
        
        
Db_Session = Annotated[Session, Depends(get_db)]        