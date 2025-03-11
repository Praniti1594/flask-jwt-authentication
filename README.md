# flask-jwt-authentication

Testing in Postman
Login to Get JWT Token

Method: POST
URL: http://127.0.0.1:5000/login
Body (JSON):
{
  "username": "testuser",
  "password": "password123"
}
Response:
{
  "access_token": "your_jwt_token_here",
  "refresh_token": "your_refresh_token_here"
}


Access Protected Route

Method: GET
URL: http://127.0.0.1:5000/protected
Headers:
Authorization: Bearer your_jwt_token_here
Response: 
{
  "msg": "Hello, testuser! You have access."
}


Refresh the Token

Method: POST
URL: http://127.0.0.1:5000/refresh
Headers:
Authorization: Bearer your_refresh_token_here
Response:
{
  "access_token": "new_access_token_here"
}


Example Flow in Simple Terms
🔐 Login:
➡️ You send your username/password ➔ Server verifies ➔ Gives you a token.

🔓 Access a protected route:
➡️ Include your token in the request ➔ Server checks ➔ Grants access.

🔄 Refresh your token:
➡️ When your old token expires, send the refresh token ➔ Get a new access token.

