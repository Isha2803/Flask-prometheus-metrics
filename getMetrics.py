from flask import Response, Blueprint
from prometheus_client import generate_latest
from fileUpload import collectorRegistry

metrics_blueprint = Blueprint('metrics', __name__)

@metrics_blueprint.route('/metrics')
def metrics():
    metrics_data = generate_latest(collectorRegistry).decode('utf-8')
    # print(metrics_data)
    return Response(metrics_data, mimetype='text/plain')