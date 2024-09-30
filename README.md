
# PoketEncyclopedia-Server

This project is a server-side application built using Flask, which provides a simple API for processing images with a local LLM. It handles incoming requests, processes images, and returns a response with AI-processed results, response times, and average response time.

## Features

- Flask-based server with a `/process_image` endpoint.
- AI image processing using external API calls.

## Prerequisites

- Python 3.6+
- [Poetry](https://python-poetry.org/docs/#installation) for dependency management

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/rivasadam01/Pocket-Encyclopedia.git
    cd Pocket-Encyclopedia
    ```

2. Install dependencies using Poetry:

    ```sh
    poetry install
    ```

## Running the Server

1. Activate the Poetry environment:

    ```sh
    poetry shell
    ```

2. Run the server:

    ```sh
    python run.py
    ```

3. The server will be available at `http://0.0.0.0:8000`.

## Running LLaMA.cpp

To run the LLaMA.cpp server, I use the following command:

```sh
~/git/llama.cpp-b2356/server --mlock --ctx-size 4096 --n-gpu-layers 33 --port 8888 --model ~/LLM_Models/vision/llava-v1.6-mistral-7b.Q4_K_M.gguf --mmproj ~/LLM_Models/vision/mmproj-llava-v1.6-mistral-7b-f16.gguf
```

This command starts the LLaMA.cpp server with the specified model and configurations, which the PoketEncyclopedia-Server relies on for image processing.

The server will return a JSON response with the following information:

- `response`: AI-processed result.
- `image`: The base64 encoded image.
- `response_time`: Time taken to process the image.
- `avg_response_time`: Rolling average response time for the last 5 requests.

## Dependencies

- **Flask**: A lightweight web framework to create and manage server routes.
- **Flask-CORS**: Enables Cross-Origin Resource Sharing to allow requests from other domains.
- **Requests**: Used to send HTTP requests to the external API for image processing.
# PoketEncyclopedia-Server
