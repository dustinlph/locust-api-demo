from flask import Flask, jsonify, request
from data_store import users, fake_db

app = Flask(__name__)
tokens = {}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    user = users.get(username)
    if user and user["password"] == password:
        token = f"token-{username}"
        tokens[token] = username
        return jsonify({"token": token})
    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(list(fake_db.values()))

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = fake_db.get(item_id)
    if not item:
        return jsonify({"message": "Not found"}), 404
    return jsonify(item)

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    item_id = max(fake_db.keys()) + 1
    new_item = {"id": item_id, "title": data["title"], "content": data["content"]}
    fake_db[item_id] = new_item
    return jsonify(new_item), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    if item_id not in fake_db:
        return jsonify({"message": "Not found"}), 404
    data = request.get_json()
    fake_db[item_id].update(data)
    return jsonify(fake_db[item_id])

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id in fake_db:
        del fake_db[item_id]
        return jsonify({"message": "Deleted"})
    return jsonify({"message": "Not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)