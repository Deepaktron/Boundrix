from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_account', methods=['POST'])
def create_account():
    # This is a simplified example. In a real application, you'd securely handle user data.
    username = request.form.get('username')
    password = request.form.get('password')

    # Here, you would typically save the user data to a database.
    # For simplicity, we'll just return a success message.
    return jsonify({'message': 'Account created successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
