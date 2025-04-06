from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["MONGO_URI"] = "mongodb://localhost:27017/resume_db"
mongo = PyMongo(app)

# User Registration
@app.route("/register", methods=["POST"])
def register():
    data = request.json
    if mongo.db.users.find_one({"email": data["email"]}):
        return jsonify({"error": "Email already registered"}), 400

    hashed_password = generate_password_hash(data["password"])
    mongo.db.users.insert_one({"name": data["name"], "email": data["email"], "password": hashed_password, "role": "user"})
    return jsonify({"message": "Registration successful"}), 201

# User Login
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    user = mongo.db.users.find_one({"email": data["email"]})

    if not user or not check_password_hash(user["password"], data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    return jsonify({"message": "Login successful"}), 200

# HR Login (Hardcoded)
@app.route("/hr-login", methods=["POST"])
def hr_login():
    data = request.json
    if data["email"] == "hr@company.com" and data["password"] == "hr123":
        return jsonify({"message": "HR login successful"}), 200
    return jsonify({"error": "Invalid HR credentials"}), 401

if __name__ == "__main__":
    app.run(debug=True)
