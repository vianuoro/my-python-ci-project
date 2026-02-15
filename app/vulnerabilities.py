from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Mock database setup
def get_db_connection():
    conn = sqlite3.connect(':memory:', check_same_thread=False)
    conn.execute('CREATE TABLE users (id INTEGER, username TEXT, secret TEXT)')
    conn.execute("INSERT INTO users VALUES (1, 'admin', 'SuperSecret123')")
    return conn

db = get_db_connection()

@app.route('/')
def home():
    # 1. XSS VULNERABILITY
    # Directly reflecting user input in HTML without escaping
    name = request.args.get('name', 'Guest')
    html_content = f"<h1>Welcome, {name}!</h1>"
    return render_template_string(html_content)

@app.route('/user')
def get_user():
    # 2. SQL INJECTION VULNERABILITY
    # Using f-strings to build a query instead of parameterized inputs
    user_id = request.args.get('id')
    query = f"SELECT username FROM users WHERE id = {user_id}"
    
    cursor = db.execute(query)
    user = cursor.fetchone()
    return f"User found: {user[0]}" if user else "User not found"

if __name__ == '__main__':
    app.run(debug=True)
