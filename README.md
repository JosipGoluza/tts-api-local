# Local TTS API

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) <!-- Optional license badge -->

A flexible, locally deployable Text-to-Speech (TTS) API server built with Python and FastAPI. This project allows easy testing and integration of various TTS models through a single, consistent API endpoint.

## Motivation

This project was initially developed as part of my Master's thesis to help me test different Text-to-Speech models within a virtual assistant prototype. The goal is to provide a simple backend service that can host multiple TTS models and allow a frontend application (like a virtual assistant) to request speech synthesis from a selected model without needing to interface with each TTS library directly.

## Core Concept

The API acts as a gateway to one or more underlying TTS models. You send text and specify which model to use, and the API returns the synthesized audio data.

The design emphasizes extensibility, aiming to allow the addition of new TTS models with minimal changes to the core API structure.

## Technology Stack

*   **Backend:** Python 3.13
*   **API Framework:** FastAPI
*   **Initial TTS Model:** Coqui TTS
*   *(Other dependencies will be listed in `requirements.txt`)*

## Getting Started

*(Instructions will be added here as the project develops)*

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

*(API endpoint details will be added here)*

## Extensibility

*(Details on adding new TTS models will be added here)*

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
