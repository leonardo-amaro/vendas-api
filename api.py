from flask import Flask, jsonify, request
from flask_cors import CORS

api = Flask(__name__)
CORS(api)

@api.route("/api/vendas", methods=["GET"])
def get_vendas():
    dados = [
        {"id": 1, "mes": "Jan", "vendas": 2000},
        {"id": 2, "mes": "Fev", "vendas": 4000},
        {"id": 2, "mes": "Mar", "vendas": 3700}
    ]
    return jsonify(dados)

api.run(host="localhost", port=3000, debug=True)
