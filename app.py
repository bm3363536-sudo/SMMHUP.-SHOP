from flask import Flask, jsonify, request

app = Flask(__name__)

# This is a very basic example. In a real app, you would save orders to a database.
# We will use a simple list here for demonstration purposes.
fake_database_orders = []
order_counter = 1

@app.route('/')
def home():
    """
    This is the default home endpoint.
    """
    return "Welcome to the SMM API Project! Use /api/order to place an order (POST request)."

@app.route('/api/order', methods=['POST'])
def place_order():
    """
    API endpoint to place a new SMM order.
    Requires JSON data with 'service_id', 'link', and 'quantity'.
    """
    global order_counter
    
    # Get the data sent by the customer in JSON format
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Validate required fields
    if 'service_id' not in data or 'link' not in data or 'quantity' not in data:
        return jsonify({"error": "Missing required fields (service_id, link, quantity)"}), 400
    
    # Extract data
    service_id = data['service_id']
    link = data['link']
    quantity = data['quantity']
    
    # --- HERE IS WHERE YOU WOULD CALL THE 3RD PARTY RESELLER API (The real work happens here later) ---
    
    # Simulate an internal order ID
    new_order_id = order_counter
    order_counter += 1
    
    # Store the order details (simulation)
    order_record = {
        "order_id": new_order_id,
        "service_id": service_id,
        "link": link,
        "quantity": quantity,
        "status": "Received"
    }
    fake_database_orders.append(order_record)
    
    # Return success response to the customer
    return jsonify({
        "status": "success",
        "message": "Order placed successfully (simulated)",
        "order_id": new_order_id
    }), 200

if __name__ == '__main__':
    # Run the application
    app.run(host='0.0.0.0', port=8000)

