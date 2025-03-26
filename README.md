# Jamboxx Infinite Backends

A FastAPI-based backend service for DDSP-SVC voice conversion and audio processing.

## Features

- Real-time voice conversion using DDSP-SVC
- Multiple speaker support
- Pitch adjustment capabilities
- RESTful API endpoints
- Async processing
- Docker support
- Comprehensive error handling

## Requirements

- Windows 10/11 (64-bit)
- Visual C++ Redistributable 2019 or later
- CUDA-compatible GPU (recommended)
- FFmpeg
- Anaconda or Miniconda

## Installation

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

## Usage

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

#### Health Check
```
GET /ping
```

#### Voice Conversion
```
POST /api/v1/voiceConvert
```

Request body:
```json
{
    "audio_data": "base64_encoded_audio",
    "speaker_id": "speaker1",
    "pitch_shift": 0.0,
    "sample_rate": 44100
}
```

#### List Available Models
```
GET /api/v1/models
```

#### Update Model
```
POST /api/v1/updateModel
```

## Development

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

## Building Notes

- Python 3.10.12 is recommended for optimal compatibility
- Compilation requires approximately 2GB of disk space
- First startup may take longer than subsequent launches
- Compiled version includes all necessary dependencies
- Target system must have Visual C++ Redistributable 2019 or later installed
- CUDA 11.8 is recommended for GPU acceleration

## Acknowledgments

- DDSP-SVC project
- FastAPI framework
- PyTorch community

## Contributor
WesleyXu - wesley.xu.23@ucl.ac.uk

# Jamboxx Infinite Backends API Documentation

## Overview
RESTful API for AI-powered voice conversion and audio processing services.

## Endpoints

### Voice Conversion

#### `POST /voice/convert`
Convert voice using DDSP-SVC model.

**Parameters:**
- `file`: Audio file (required)
- `speaker_id`: Target speaker ID (default: 1)
- `key`: Pitch adjustment in semitones (default: 0)
- `enhance`: Enable audio enhancement (default: true)
- `pitch_extractor`: Algorithm for pitch extraction (default: "rmvpe")
- `f0_min`: Minimum pitch in Hz (default: 50)
- `f0_max`: Maximum pitch in Hz (default: 1100)
- `threhold`: Volume threshold in dB (default: -60)
- `enhancer_adaptive_key`: Enhancer key adaptation value (default: 0)

**Response:**
```json
{
  "status": "success",
  "message": "Conversion complete",
  "file_url": "/static/convert/output_[uuid].wav",
  "file_size": 1234567
}
```

### Speaker Management

#### `GET /speakers`
Get available speaker voices.

**Response:**
```json
{
  "speakers": ["Child", "Male", "Female"]
}
```

#### `POST /model/load`
Load or switch voice models.

**Parameters:**
- `model_name`: Model name (required)

#### `GET /model/info`
Get current model information.

### Audio Processing

#### `POST /audio/separate`
Separate audio into vocals and instruments.

**Parameters:**
- `audio_file`: Audio file (required)

**Response:**
```json
{
  "vocals_url": "/static/separator/vocals_[uuid].wav",
  "instruments_url": "/static/separator/instruments_[uuid].wav",
  "sample_rate": 44100
}
```

#### `POST /audio/merge`
Merge vocals and instruments tracks.

**Parameters:**
- `vocals_path`: Path to vocals file (required)
- `instruments_path`: Path to instruments file (required)
- `vocals_volume`: Volume multiplier for vocals (default: 1.5)
- `instruments_volume`: Volume multiplier for instruments (default: 1.0)
- `output_filename`: Custom filename (optional)

#### `POST /audio/merge-uploads`
Merge uploaded vocals and instruments files.

**Parameters:**
- `vocals_file`: Vocals audio file (required)
- `instruments_file`: Instruments audio file (required)
- `vocals_volume`: Volume multiplier for vocals (default: 1.5)
- `instruments_volume`: Volume multiplier for instruments (default: 1.0)

### Complete Pipeline

#### `POST /audio/process-all`
Full audio processing pipeline: separate → convert → merge.

**Parameters:**
- `file`: Audio file (required)
- All voice conversion parameters
- `vocals_volume`: Volume multiplier for vocals (default: 1.5)
- `instruments_volume`: Volume multiplier for instruments (default: 1.0)

**Response:**
```json
{
  "status": "success",
  "message": "Audio processing pipeline completed successfully",
  "original_audio": { "filename": "input.mp3" },
  "separated_audio": {
    "vocals_url": "/static/separator/vocals_[uuid].wav",
    "instruments_url": "/static/separator/instruments_[uuid].wav"
  },
  "converted_audio": {
    "vocals_url": "/static/converter/converted_[uuid].wav"
  },
  "final_output": {
    "file_url": "/static/pipeline/processed_[uuid].wav",
    "file_size": 1234567
  },
  "processing_info": {
    "speaker_id": 1,
    "key": 0,
    "enhance": true,
    "vocals_volume": 1.5,
    "instruments_volume": 1.0
  }
}
```

### Utilities

#### `GET /ping`
Health check endpoint.

**Response:**
```json
{
  "status": "ok",
  "message": "pong"
}
