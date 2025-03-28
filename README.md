# Jamboxx Infinite Backends

#### Voice cloning - a FastAPI-based backend service for DDSP-SVC voice conversion and audio processing.

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

# Install PyTorch with CUDA support(with your cuda version is avaiable)
conda install pytorch==2.0.1 torchaudio==2.0.1 pytorch-cuda=11.8 -c pytorch -c nvidia
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage - voice cloning

### Running the Server

Using pre-compiled executable:
```batch
cd dist\main.dist
start.bat
```

Using python:
```bash
python app/main.py
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

## Contributor
WesleyXu
JoyceKong
