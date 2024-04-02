from flask import Flask, render_template, request, jsonify
import redis
import os

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))

r = redis.Redis(host=redis_host, port=redis_port)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_value', methods=['GET'])
def get_value():
    value = r.get('counter')
    permanent_value = r.get('permanentCounter')
    if value is None and permanent_value is None:
        value = 0
        permanent_value = 0
    elif value is None:
        value = 0
        permanent_value = int(permanent_value)
    else:
        value = int(value)
        permanent_value = int(permanent_value)
    return jsonify({'value': value, 'permanentValue': permanent_value})

@app.route('/save', methods=['POST'])
def save():
    value = request.json['value']
    r.set('counter', value)
    return jsonify({'status': 'success'})

@app.route('/permanent_save', methods=['POST'])
def permanent_save():
    permanent_value = request.json['permanentValue']
    r.set('permanentCounter', permanent_value)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
