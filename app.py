from flask import Flask, jsonify, request
from greq import get_counts
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/')
def welcome():
    arg = request.args.get('search')
    res = {'searchTerm': arg, 'counts': get_counts(arg)}
    return jsonify(res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
