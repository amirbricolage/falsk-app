# app.py
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    # Perform your mathematical operations here
    result = data['a'] * data['b']  # Example operation
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)