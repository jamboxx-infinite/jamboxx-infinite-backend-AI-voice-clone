import logging
import subprocess
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
from pathlib import Path
from routers import router
import sys

logger = logging.getLogger(__name__)

def verify_ffmpeg():
    # Get the directory where the executable/script is located
    base_dir = Path(get_app_path())
    print(base_dir)
    ffmpeg_path = str(base_dir / "ffmpeg" / "bin" / "ffmpeg.exe")
    ffprobe_path = str(base_dir / "ffmpeg" / "bin" / "ffprobe.exe")
    
    try:
        # Verify file existence
        if not os.path.exists(ffmpeg_path):
            raise FileNotFoundError(f"FFmpeg not found at {ffmpeg_path}")
        if not os.path.exists(ffprobe_path):
            raise FileNotFoundError(f"FFprobe not found at {ffprobe_path}")
            
        # Verify executability
        subprocess.run([ffmpeg_path, "-version"], check=True, capture_output=True)
        subprocess.run([ffprobe_path, "-version"], check=True, capture_output=True)
        
        # Set environment variables
        os.environ["FFMPEG_BINARY"] = ffmpeg_path
        os.environ["FFPROBE_BINARY"] = ffprobe_path
        
        logger.info("FFmpeg verified successfully")
        return True
    except Exception as e:
        logger.error(f"FFmpeg verification failed: {str(e)}")
        return False

def get_app_path():
    """Get the root path of the application, compatible with both development and compiled environments"""
    if getattr(sys, 'frozen', False):
        # If running in a compiled environment
        return os.path.dirname(sys.executable)
    else:
        # Development environment
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def setup_environment():
    """Set environment variables and Python path"""
    base_dir = get_app_path()
    
    # Add the app directory to the Python path
    app_dir = os.path.join(base_dir, "app")
    if (app_dir not in sys.path):
        sys.path.append(app_dir)
    
    # Set the model path environment variable
    os.environ["MODEL_BASE_DIR"] = os.path.join(base_dir, "pretrain")
    
    logger.info(f"Environment setup complete. Base dir: {base_dir}")

app = FastAPI(title="Jamboxx Infinite Backends")

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create static file directory
static_dir = os.path.join(get_app_path(), "static")
os.makedirs(static_dir, exist_ok=True)

# Mount static file service
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Verify on application startup
@app.on_event("startup")
async def startup_event():
    setup_environment()
    if not verify_ffmpeg():
        raise RuntimeError("FFmpeg configuration failed")

# Register routes
app.include_router(router.router)

@app.get("/ping")
def ping():
    """Health check endpoint"""
    return {"status": "ok", "message": "pong"}

@app.get("/")
async def root():
    return {"message": "Welcome to Jamboxx Infinite Backends"}

if __name__ == "__main__":
    import uvicorn
    """
    Ways to start the server:
    1. Using the uvicorn command (recommended):
       uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
    
    2. Running this file directly:
       python app/main.py
    """
    uvicorn.run(app, host="0.0.0.0", port=8000)
