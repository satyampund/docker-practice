from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({"message": "Server is up and running"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000 , debug=True)

