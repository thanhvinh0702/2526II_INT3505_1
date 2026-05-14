from prometheus_client import Counter, Histogram, generate_latest
from flask import request, Response
import logging
import time

REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP Requests',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP Request latency'
)

logger = logging.getLogger(__name__)

def setup_metrics(app):

    @app.before_request
    def before_request():
        request.start_time = time.perf_counter()

    @app.after_request
    def after_request(response):
        latency = time.perf_counter() - request.start_time

        REQUEST_LATENCY.observe(latency)

        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.path,
            status=response.status_code
        ).inc()

        logger.info(
            "HTTP %s %s -> %s in %.4fs",
            request.method,
            request.path,
            response.status_code,
            latency
        )

        return response

    @app.route("/metrics")
    def metrics():
        return Response(
            generate_latest(),
            mimetype="text/plain"
        )
