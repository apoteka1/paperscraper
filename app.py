from flask import Flask, jsonify, request
from greq import get_counts

app = Flask(__name__)

@app.route('/')
def welcome():
    arg = request.args.get('search')
    return jsonify(get_counts(arg))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
