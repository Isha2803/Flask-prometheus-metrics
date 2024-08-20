from flask import Flask, request, Response
from fileUpload import file_upload_blueprint
from getMetrics import metrics_blueprint

app = Flask(__name__)
app.register_blueprint(file_upload_blueprint)
app.register_blueprint(metrics_blueprint)

@app.route('/')
def index():
    return "Welcome to the File Upload Service!"

if __name__ == '__main__':
    app.run(port=5000)
    
    
    
    