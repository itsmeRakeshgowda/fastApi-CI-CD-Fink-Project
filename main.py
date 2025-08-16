from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"writer": "see you in the next episode!"}
                                                                      