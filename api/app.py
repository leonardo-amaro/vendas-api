from flask import Flask, jsonify, request
from flask_cors import CORS

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

def handler(event, context):
    from werkzeug.wrappers import Request, Response

    @Request.application
    def application(request):
        with app.request_context(request.environ):
            response = app.full_dispatch_request()
            return response

    req = Request.from_values(**event)
    res = application(req)

    return {
        "statusCode": res.status_code,
        "headers": dict(res.headers),
        "body": res.get_data(as_text=True),
    }
