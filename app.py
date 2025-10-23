from flask import Flask
import os

app = Flask(__name__)

# Detect environment from ENV variable
ENV_COLOR = os.environ.get('APP_COLOR', 'blue')  # default to 'blue'

@app.route('/')
def home():
    return f"Hello from Flask app running in Kubernetes! Environment: {ENV_COLOR}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
