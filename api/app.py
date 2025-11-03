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
    return app(request.environ, start_response)

def start_response(status, headers):
    from io import BytesIO
    body = BytesIO()

    def write(data):
        body.write(data)
        return None

    def get_response():
        return {
            "statusCode": int(status.split()[0]),
            "headers": dict(headers),
            "body": body.getvalue().decode()
        }

    write.get_response = get_response
    return write
