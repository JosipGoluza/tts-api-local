# Local TTS API

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) <!-- Optional license badge -->
[![Python: 3.12](https://img.shields.io/badge/python-3.12-blue)](https://www.python.org/downloads/release/python-3120/)

A flexible, locally deployable Text-to-Speech (TTS) API server built with Python and FastAPI. This project allows easy testing and integration of various TTS models through a single, consistent API endpoint.

## Motivation

This project was initially developed as part of my Master's thesis to help me test different Text-to-Speech models within a virtual assistant prototype. The goal is to provide a simple backend service that can host multiple TTS models and allow a frontend application (like a virtual assistant) to request speech synthesis from a selected model without needing to interface with each TTS library directly.

## Core Concept

The API acts as a gateway to one or more underlying TTS models. You send text and specify which model to use, and the API returns the synthesized audio data.

The design emphasizes extensibility, aiming to allow the addition of new TTS models with minimal changes to the core API structure.

## Technology Stack

*   **Backend:** Python 3.12
*   **API Framework:** FastAPI
*   *(Other dependencies will be listed in `requirements.txt`)*

## Getting Started

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/JosipGoluza/local-tts-api.git
    cd local-tts-api
    ```
2.  **Create a virtual environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the API server (Development):**
    ```bash
    fastapi dev app/main.py
    ```
5.  **Access the API docs:**
    Open your browser and go to `http://127.0.0.1:8000/docs`.

## Usage

### GET /models
- **Description**: Returns a list of available TTS models
- **Response**: JSON object containing array of available model names
- **Example Response**:
  ```json
  {
    "models": ["coqui_tts"]
  }
  ```


### POST /synthesize/{model_name}
- **Description**: Synthesizes speech from an input text using the specified model
- **Path Parameters**: 
  - `model_name`: Name of the TTS model to use (e.g., "coqui_tts")
- **Request Body**: JSON object containing:
  ```json
  {
    "text": "Text to be synthesized into speech"
  }
  ```
- **Response**: JSON object containing the generated audio file identifier
- **Example Response**:
  ```json
  {
    "message": "[file_hash]"
  }
  ```
  
### GET /stream/{hash_id}
- **Description**: Streams the generated audio file for playback or download
- **Path Parameters**:
  - `hash_id`: The file identifier returned from the synthesize endpoint
- **Response**: Audio file stream (WAV format)
- **Content-Type**: audio/wav
- **Error Responses**:
  - `404`: Audio file not found
  - `500`: Server error

## Configuration

### TTS Models
Currently supported TTS models:
- **Coqui TTS**
  - Default model: `tts_models/hr/vits`
  - Device: Automatically uses CUDA if available, falls back to CPU
  - Output format: WAV files
  - Output location: `./output` directory (configurable)

### CORS Configuration
The API implements CORS (Cross-Origin Resource Sharing) - a security feature that controls which web applications can access the API. By default, requests from `http://localhost` and `http://localhost:3000` are allowed. Additional origins can be added to the `origins` list in the application configuration.


## Extensibility

To add support for a new TTS model:
1. Create a new model class in `app/tts_interface/models/`
2. Implement the `TTSInterface` abstract class
3. Add the model to `TTSClient._available_strategies`


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
