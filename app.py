from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Storing the transactions and points balance
transactions = []
points_balance = {}


@app.route('/add', methods=['POST'])
def add_points():
    data = request.get_json()
    
    payer = data.get('payer')
    points = data.get('points')
    timestamp = data.get('timestamp')
    
    if not payer or points is None or not timestamp:
        return jsonify({"error": "Missing Required Fields"}), 400
    
    timestamp = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
    
    # Update Points Balance
    points_balance[payer] = points_balance.get(payer, 0) + points
    
    # Log the transaction
    transactions.append({"payer": payer, "points": points, "timestamp": timestamp})
    
    # Sort transactions by timestamp
    transactions.sort(key=lambda x: x['timestamp'])
    
    return '', 200


@app.route('/spend', methods=['POST'])
def spend_points():
    points_to_spend = request.get_json().get('points')
    if not points_to_spend or points_to_spend < 0:
        return jsonify({"error": "Invalid points value"}), 400
    
    if sum(points_balance.values()) < points_to_spend:
        return "Insufficient points", 400
    
    spent_points = []
    for transaction in transactions:
        payer = transaction['payer']
        points = transaction['points']
        
        if points_to_spend <= 0:
            break
        
        deduct_points = min(points, points_to_spend)
        points_balance[payer] -= deduct_points
        points_to_spend -= deduct_points
        
        spent_points.append({"payer": payer, "points": -deduct_points})
    
    # Remove the transactions where all points are spent
    transactions[:] = [t for t in transactions if t['points'] > 0]
    
    return jsonify(spent_points), 200


@app.route('/balance', methods=['GET'])
def get_balance():
    return jsonify(points_balance), 200


if __name__ == "__main__":
    app.run(port=8000, debug=True)
