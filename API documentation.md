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
