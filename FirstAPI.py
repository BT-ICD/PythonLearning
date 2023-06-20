import uvicorn
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import sessionmaker
import urllib

from fastapi import FastAPI

app = FastAPI()
conn = urllib.parse.quote_plus(
    'Data Source Name=MssqlDataSource;'
    'Driver={SQL Server};'
    'Server=Bhavin;'
    'Database=LearningDB;'
    'Trusted_connection=yes;'
)

try:

    engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(conn))
    print("Passed")
except:
    print("failed!")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
session = SessionLocal()
class Student(Base):
    __tablename__ = "StudentData"

    ID = Column(Integer, primary_key=True, index=True)
    SName = Column(String)
    Area = Column(String)
    Phone = Column(String)
@app.get("/")
async def root():
    students = session.query(Student).all();
    return students

@app.get("/{id}")
async def getById(id:int):
    student = session.query(Student).filter(Student.ID==id).first();
    return student

@app.get("/item")
async def getItems():
    return {"message": "From items"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)