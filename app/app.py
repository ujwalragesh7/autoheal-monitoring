from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of HTTP requests"
)


@app.before_request
def count_request():
    REQUEST_COUNT.inc()


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>AutoHeal Monitoring App</title>
        </head>
        <body>
            <h1>AutoHeal DevOps Platform</h1>
            <p>Application is running successfully.</p>
            <p>Monitoring: Prometheus + Grafana</p>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
