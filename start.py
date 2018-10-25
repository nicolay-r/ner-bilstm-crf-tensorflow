from flask import Flask, jsonify, request
import init

app = Flask(__name__)

@app.route('/ner', methods=['POST'])
def add():
    data = request.get_json()
    print(data)
    tokens, tags = init.predict(data['terms'])
    return jsonify({'tokens': tokens, 'tags': tags})

if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=True)
