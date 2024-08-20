from flask import Blueprint
from prometheus_client import Histogram, CollectorRegistry
import random
import time

file_upload_blueprint = Blueprint('file_upload', __name__)
file_upload_bucket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# create prometheus histogram for metric collection
collectorRegistry = CollectorRegistry()
file_upload_histogram = Histogram(
    'file_upload_duration_seconds', 
    'File upload duration in seconds', 
    buckets= file_upload_bucket,
    registry = collectorRegistry
)

@file_upload_blueprint.route('/file-upload', methods=['POST'])
def handle_file_upload():
    # timer = file_upload_histogram.start_timer()
    start_time = time.time()
    delay = random.uniform(1, 10)  
    time.sleep(delay)  
    # timer.observe_duration()
    duration = time.time() - start_time
    file_upload_histogram.observe(duration)
    print("File upload took %f seconds!", duration)
    return "File upload took {:.2f} seconds!".format(duration)

