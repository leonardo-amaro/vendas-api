from flask import Flask, jsonify
from flask_cors import CORS
from vercel_wsgi import handle

app = Flask(__name__)
CORS(app)

@app.route("/api/vendas", methods=["GET"])
def get_vendas():
    dados = [
        {"id": 1, "mes": "Jan", "vendas": 2000},
        {"id": 2, "mes": "Fev", "vendas": 4000},
        {"id": 2, "mes": "Mar", "vendas": 3700}
    ]
    return jsonify(dados)

def handler(request, context):
    return handle(app, request, context)
