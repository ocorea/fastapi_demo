
import math

from fastapi import Depends, FastAPI, Body
from pydantic import BaseModel
from sqlalchemy.orm import Session

from  data.models import Result
from data.database import SessionLocal

app = FastAPI(title="Vessel GHG Emission Calculation")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



class Factorial(BaseModel):
    number: int  = Body(...,ge=1, le=12)


@app.post("/factorial", status_code=200)
def createFactorial(factorial: Factorial, db: Session = Depends(get_db)):
    print(factorial)
    #calculate the factorial of the received number
    result=math.factorial(factorial.number)
    #save into sqlite
    record=Result(number=factorial.number, factorial=result)
    db.add(record)
    db.commit()
    return {"response":"OK"}

@app.get("/getmax", status_code=200)
async def getMax(db:Session=Depends(get_db)):
    max_value=db.execute("select max(factorial) as max_value from results").first()['max_value']
    result=math.sqrt(max_value)
    return {'max_factorial': max_value, 'square':result }




