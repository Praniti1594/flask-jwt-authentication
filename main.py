from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager, create_access_token, create_refresh_token,
    jwt_required, get_jwt_identity
)

app = Flask(__name__)

# Secret key for JWT
app.config['JWT_SECRET_KEY'] = 'your_secret_key_here'  # Change this to a strong secret key
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600  # 1 hour

jwt = JWTManager(app)

# Mock user database (replace with a real DB)
users = {
    "testuser": "password123"
}

# Route: User Login (Generate JWT Token)
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check user credentials
    if username in users and users[username] == password:
        access_token = create_access_token(identity=username)
        refresh_token = create_refresh_token(identity=username)
        return jsonify(access_token=access_token, refresh_token=refresh_token), 200
    else:
        return jsonify({"msg": "Invalid username or password"}), 401

# Route: Access a Protected Resource
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({"msg": f"Hello, {current_user}! You have access."})

# Route: Refresh Token
@app.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)
    return jsonify(access_token=new_access_token)

if __name__ == '__main__':
    app.run(debug=True)
