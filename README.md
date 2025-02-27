﻿# Jamboxx Infinite Backends

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

- Python 3.9+
- CUDA-compatible GPU (recommended)
- FFmpeg

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/jamboxx-infinite-backends.git
cd jamboxx-infinite-backends
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configurations
```

## Usage

### Running the Server

Development mode:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Production mode:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

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
├── tests/
├── requirements.txt
├── Dockerfile
└── README.md
```

## Acknowledgments

- DDSP-SVC project
- FastAPI framework
- PyTorch community
