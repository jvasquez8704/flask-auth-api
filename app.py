from flask import Flask, jsonify, request

app = Flask(__name__)


#Test Route
@app.route('/test')
def ping():
    return jsonify({"message":"Hola Mundo!"});


@app.route('/register', methods=['POST'])
def register():
    return jsonify({'mesagge': "Registro realizado para: " + request.json['email'] })



if __name__ == '__main__':
    app.run(debug=True, port=4000)