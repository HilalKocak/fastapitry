from fastapi import FastAPI

app = FastAPI()

import uvicorn

@app.get("/")
def home():
    return {"message":"Hello Hilal"}
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)