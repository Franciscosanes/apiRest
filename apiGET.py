from flask import Flask, jsonify, request

app = Flask(__name__)

# Ruta que acepta GET
@app.route('/saludo', methods=['GET'])
def saludo():
    return jsonify({"message": "¡Hola! Bienvenido a + la API con GET"}), 200

# Ruta que acepta POST
@app.route('/saludo', methods=['POST'])
def saludo_post():
    return jsonify({"message": "¡Hola! Has enviado un POST"}), 201

# Ruta que acepta PUT
@app.route('/saludo', methods=['PUT'])
def saludo_put():
    return jsonify({"message": "¡Hola! Has actualizado con un PUT"}), 200

# Ruta que acepta DELETE
@app.route('/saludo', methods=['DELETE'])
def saludo_delete():
    return jsonify({"message": "¡Adiós! Has eliminado con un DELETE"}), 200

if __name__ == '__main__':
    app.run(debug=True)
