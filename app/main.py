from fastapi import FastAPI

app = FastAPI(title="FastAPI CI/CD Demo")


@app.get("/")
def read_root():
    return {"message": "CI/CD Deployment Successful"}


@app.get("/health")
def health_check():
    return {"status": "success"}
