# Jamboxx Infinite Backends

#### Voice cloning - a FastAPI-based backend service for DDSP-SVC voice conversion and audio processing.
#### Offline chatbot - this project provides a lightweight FastAPI wrapper around a [llama.cpp](https://github.com/ggerganov/llama.cpp)-based large language model (LLM) binary, enabling real-time streamed AI chat completions via HTTP.

## Features - voice cloning

- Real-time voice conversion using DDSP-SVC
- Multiple speaker support
- Pitch adjustment capabilities
- RESTful API endpoints
- Async processing
- Docker support
- Comprehensive error handling

## Requirements - voice cloning 

- Windows 10/11 (64-bit)
- Visual C++ Redistributable 2019 or later
- CUDA-compatible GPU (recommended)
- FFmpeg
- Anaconda or Miniconda

## Installation - voice cloning

### Method 1: Using Pre-compiled Executable (Windows Only)

1. Download the latest release from the releases page
2. Extract the archive to your desired location
3. Run `start.bat` in the extracted folder

### Method 2: From Source

1. Clone the repository:
```bash
git clone https://github.com/yourusername/jamboxx-infinite-backends.git
cd jamboxx-infinite-backends
```

2. Create and activate virtual environment:
```bash
# Create new environment with Python 3.10.12
conda create -n jamboxx python=3.10.12
conda activate jamboxx

# Install PyTorch with CUDA support
conda install pytorch==2.0.1 torchaudio==2.0.1 pytorch-cuda=11.8 -c pytorch -c nvidia
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configurations
```

5. Download required models:
```bash
python scripts/download_models.py
```

## Installation - offline chatbot

1. Clone the repository:

```bash
git clone https://github.com/yourusername/llama-fastapi-backend.git
cd llama-fastapi-backend
```

2. Build `llama.cpp` binary (assumes it's located at `build/bin/llama-cli`):

```bash
# Inside the llama.cpp directory
mkdir -p build && cd build
cmake ..
make -j
```

3. Download your model (`.gguf` format) into `models/` directory:

```bash
mkdir -p models
# Move your .gguf model file into the models/ directory
```

4. Run the API server:

```bash
python app.py
```

## Usage - voice cloning

### Running the Server

Using pre-compiled executable:
```batch
cd dist\main.dist
start.bat
```

Development mode:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Production mode:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Using Docker:
```bash
docker build -t jamboxx-backend .
docker run -p 8000:8000 jamboxx-backend
```

### Building from Source

To compile the application into a standalone executable:

```batch
cd scripts
build.bat
```

The compiled executable and required files will be available in the `dist/main.dist` directory.

### API Endpoints
See [API documentations.md]

### Project Structure
```
jamboxx_infinite_backends/
├── app/
│   ├── main.py
│   ├── routers/
│   ├── services/
│   ├── core/
│   ├── utils/
│   └── schemas/
├── scripts/
│   ├── build.bat
│   └── download_models.py
├── dist/
│   └── main.dist/
├── tests/
├── requirements.txt
├── Dockerfile
└── README.md
```

## Acknowledgments

- [DDSP-SVC project](https://github.com/magenta/ddsp)
- FastAPI framework
- PyTorch community
- [ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp) 
- [Mistral AI](https://mistral.ai/)
- 
## Contributor
WesleyXu - wesley.xu.23@ucl.ac.uk
Joyce Kong - hui.kong.23@ucl.ac.uk
