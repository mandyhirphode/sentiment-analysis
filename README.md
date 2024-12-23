
# FastAPI Sentiment Analysis Project

This project demonstrates how to build a RESTful API using FastAPI for performing sentiment analysis on text input. The sentiment analysis is powered by the `transformers` library from Hugging Face.

## Table of Contents

- [Features](#features)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Making API Requests](#making-api-requests)
- [Project Structure](#project-structure)


## Features

- **Sentiment Analysis:** Analyze the sentiment of text input using a pre-trained model.
- **FastAPI:** Build a high-performance web API with automatic interactive documentation.
- **Docker Support:** (Optional) Containerize the application for easy deployment.

## Setup

### Prerequisites

- Python 3.7+
- Virtualenv (optional but recommended)
- Docker (optional)

### Installation

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/yourusername/fastapi-sentiment-analysis.git
   cd fastapi-sentiment-analysis
   ```

2. **Create a Virtual Environment:**
   ```sh
   python3 -m venv venv
   ```

3. **Activate the Virtual Environment:**
   - On Windows:
     ```sh
     .\venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```sh
     source venv/bin/activate
     ```

4. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

5. **Set Environment Variables:**
   - Create a `.env` file in the project root and add any necessary environment variables. For example:
     ```
     DATABASE_URL=postgresql://user:password@localhost/dbname
     ```

## Usage

### Running the Application

1. **Start the FastAPI Server:**
   ```sh
   uvicorn app.main:app --reload
   ```

2. **Access the Interactive Documentation:**
   - Open your web browser and navigate to `http://127.0.0.1:8000/docs`.
   - You will see the automatically generated documentation provided by FastAPI.

### Making API Requests

1. **Using `curl`:**
   ```sh
   curl -X POST "http://127.0.0.1:8000/analyze/" -H "Content-Type: application/json" -d '{"text": "I love this product!"}'
   ```

2. **Using the Interactive Documentation:**
   - Navigate to `http://127.0.0.1:8000/docs`.
   - Find the `/analyze/` endpoint and use the "Try it out" feature to send a request.

## Project Structure

```
my_project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── api.py
│   ├── sentiment.py
├── requirements.txt
├── .env
├── README.md
```

- **`app/main.py`:** Entry point of the FastAPI application.
- **`app/api.py`:** Defines the API endpoints and routes.
- **`app/models.py`:** Defines the database models (if any).
- **`app/sentiment.py`:** Contains the sentiment analysis logic.
- **`requirements.txt`:** Lists all the dependencies required for the project.
- **`.env`:** Stores environment variables.
- **`README.md`:** Provides an overview of the project, setup instructions, and usage examples.
