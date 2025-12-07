from fastapi import FastAPI
from dotenv import load_dotenv
from api.routers import api_router
from utils.logging import log_requests_middleware, error_handler_middleware
from config.settings import settings

load_dotenv()

# Create FastAPI app with settings
app = FastAPI(
    title=settings.app_name,
    description="Backend API for the AI-Native Textbook project",
    version=settings.app_version,
    debug=settings.debug
)

# Add middleware
app.middleware("http")(log_requests_middleware)
app.middleware("http")(error_handler_middleware)

# Include API routes
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI-Native Textbook API", "version": settings.app_version}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": settings.app_name}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)