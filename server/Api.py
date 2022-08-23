from fastapi import FastAPI

app = FastAPI()

@app.get("/")   
def GetQuestion():
    return {"message": "Hello World"}