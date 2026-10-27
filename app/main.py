from fastapi import FastAPI

from app.modules.auth.route import router as auth_router

app = FastAPI(title="Cuewise API", version="1.0.0")

app.include_router(auth_router)


@app.get("/health")
def health_check():
    return {"status": "healthy"}
