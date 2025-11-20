"""
Flask Tutorial Server

A simple Flask web server demonstrating basic HTTP GET endpoints.
This application was created as a Python Flask implementation featuring
multiple endpoints that return plain text responses.
"""

from flask import Flask
import os

# Initialize Flask application
app = Flask(__name__)

# Port configuration with environment variable support
PORT = int(os.environ.get('PORT', 5000))


@app.route('/hello', methods=['GET'])
def hello():
    """
    Hello endpoint for HTTP GET requests.
    
    Returns:
        str: Plain text response "Hello world"
    """
    return 'Hello world'


@app.route('/', methods=['GET'])
def index():
    """
    Root endpoint for HTTP GET requests.
    
    Returns:
        str: Plain text response "Hello world"
    """
    return 'Hello world'


@app.route('/evening', methods=['GET'])
def evening():
    """
    Evening greeting endpoint for HTTP GET requests.
    
    Returns:
        str: Plain text response "Good evening"
    """
    return 'Good evening'


if __name__ == '__main__':
    # Run Flask development server with debug mode enabled
    # Debug mode provides auto-reload on code changes and detailed error messages
    print(f'Starting Flask server on http://0.0.0.0:{PORT}')
    print(f'Available endpoints:')
    print(f'  - GET http://localhost:{PORT}/hello')
    print(f'  - GET http://localhost:{PORT}/')
    print(f'  - GET http://localhost:{PORT}/evening')
    app.run(debug=True, host='0.0.0.0', port=PORT)
