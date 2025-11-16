from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    """
    This is the default home endpoint.
    """
    return "Welcome to the SMM API Project! Use /api/status endpoint."

@app.route('/api/status', methods=['GET'])
def api_status():
    """
    An API endpoint that returns the current status of the SMM service.
    """
    status_data = {
        "service_name": "My SMM Panel API",
        "status": "Operational",
        "version": "1.0",
        "message": "API is working correctly."
    }
    # Return data as a JSON response
    return jsonify(status_data)

if __name__ == '__main__':
    # Run the application
    app.run(host='0.0.0.0', port=8000)

