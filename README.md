# ABK-1929

## Flask Tutorial Server

A simple Flask web server demonstrating basic HTTP GET endpoints with plain text responses. This tutorial project showcases fundamental Flask routing patterns and server configuration.

## Prerequisites

- Python 3.12.3 or higher
- pip (Python package installer)

## Installation

### 1. Create Virtual Environment

Create an isolated Python environment for the project dependencies:

```bash
python3 -m venv venv
```

### 2. Activate Virtual Environment

**On Linux/macOS:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### 3. Install Dependencies

Install Flask and all required packages:

```bash
pip install -r requirements.txt
```

## Running the Server

Start the Flask development server:

```bash
python app.py
```

The server will start on `http://localhost:5000` by default. You should see output indicating the server is running and listing available endpoints.

### Custom Port Configuration

To run the server on a different port, set the `PORT` environment variable:

```bash
PORT=8080 python app.py
```

## Available Endpoints

The server provides three HTTP GET endpoints:

### 1. Hello Endpoint
- **URL:** `http://localhost:5000/hello`
- **Method:** GET
- **Response:** `Hello world`
- **Example:**
  ```bash
  curl http://localhost:5000/hello
  ```

### 2. Root Endpoint
- **URL:** `http://localhost:5000/`
- **Method:** GET
- **Response:** `Hello world`
- **Example:**
  ```bash
  curl http://localhost:5000/
  ```

### 3. Evening Endpoint
- **URL:** `http://localhost:5000/evening`
- **Method:** GET
- **Response:** `Good evening`
- **Example:**
  ```bash
  curl http://localhost:5000/evening
  ```

## Development

The server runs in **debug mode** by default, which provides:
- **Auto-reload:** Server automatically restarts when code changes are detected
- **Detailed error messages:** Enhanced debugging information in the browser
- **Interactive debugger:** Web-based debugger for exceptions

### Testing Endpoints

You can test the endpoints using:

**1. Web Browser:**
- Navigate to `http://localhost:5000/hello`
- Navigate to `http://localhost:5000/`
- Navigate to `http://localhost:5000/evening`

**2. curl Command:**
```bash
curl http://localhost:5000/hello
curl http://localhost:5000/
curl http://localhost:5000/evening
```

**3. Python requests:**
```python
import requests
response = requests.get('http://localhost:5000/hello')
print(response.text)  # Outputs: Hello world
```

## Project Structure

```
.
├── app.py              # Flask application entry point
├── requirements.txt    # Python package dependencies
├── .python-version     # Python version specification (3.12.3)
├── .gitignore         # Git ignore patterns for Python
├── venv/              # Virtual environment (not tracked in Git)
└── README.md          # This file
```

## Technology Stack

- **Python:** 3.12.3
- **Flask:** 3.0.0 - Micro web framework
- **Werkzeug:** 3.1.3 - WSGI utility library
- **Jinja2:** 3.1.6 - Template engine
- **click:** 8.3.1 - CLI toolkit

## Stopping the Server

To stop the development server:
- Press `Ctrl+C` in the terminal where the server is running

## Troubleshooting

### Virtual Environment Not Activated
If you see module import errors, ensure the virtual environment is activated:
```bash
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### Port Already in Use
If port 5000 is already in use, specify a different port:
```bash
PORT=8080 python app.py
```

### Missing Dependencies
If Flask is not found, reinstall dependencies:
```bash
pip install -r requirements.txt
```