from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(_name_)
swagger = Swagger(app)

@app.route('/soma', methods=['POST'])
def soma():
    num1 = request.form.get('num1', type=float)
    num2 = request.form.get('num2', type=float)
    return jsonify({'soma': num1 + num2})

@app.route('/multiplicacao', methods=['POST'])
def multiplicacao():
    num1 = request.form.get('num1', type=float)
    num2 = request.form.get('num2', type=float)
    return jsonify({'produto': num1 * num2})