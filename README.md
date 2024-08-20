# Flask Prometheus Metrics Demo

This repository contains a Python Flask application that demonstrates how to use the Prometheus simple client library to collect and expose metrics. The demo showcases the use of `CollectorRegistry` for collecting metrics, specifically simulating file upload durations.

## Overview

The application consists of three main files:

1. **app.py**: The main Flask application that sets up routes for file uploads and metrics collection.
2. **fileUpload.py**: Contains a Blueprint for simulating file upload functionality and collecting duration metrics using Prometheus.
3. **getMetrics.py**: Contains a Blueprint for exposing Prometheus metrics collected by the `CollectorRegistry`.

### Purpose

This demo simulates file upload functionality to showcase the use of the Prometheus simple client library. The primary goal is to demonstrate how to use `CollectorRegistry` to collect and expose metrics. The demo is not a full file upload service but rather a simulation for educational purposes.

### Components

- **Simple Client Library**: The `prometheus_client` library provides tools for instrumenting code and exposing metrics to Prometheus.
- **CollectorRegistry**: This is used to register and collect metrics. In this demo, it collects histogram data on simulated file upload durations.

    #### Types of Metrics

    The `prometheus_client` library provides several types of metrics that can be collected using `CollectorRegistry`, including:

    - **Counter**: A monotonically increasing counter that is used to count events or occurrences. For example, the number of requests received by the server.
    - **Gauge**: A metric that can go up and down. It is used to measure values like current memory usage or active connections.
    - **Histogram**: A metric that samples observations (e.g., durations) and counts them in configurable buckets. Useful for measuring request durations or sizes.
    - **Summary**: Similar to a histogram but provides quantiles and other statistical information about observations.

### Running the Demo

1. **Install Dependencies**: Ensure you have the required dependencies installed. You can use the following command to install them:

    ```bash
    pip install Flask prometheus_client
    ```

2. **Run the Application**: Start the Flask application with:

    ```bash
    python app.py
    ```

3. **Access the Endpoints**:
    - Simulate a file upload by sending a POST request to `http://localhost:5000/file-upload`.
    - View the collected metrics by visiting `http://localhost:5000/metrics`.
   
   To test the file upload simulation, use the following commands:
   #### Using curl (Command Line):
   ```
    curl -X POST http://localhost:5000/file-upload
   ```
   ```
    curl http://localhost:5000/metrics
   ```

   #### Using Invoke-RestMethod (PowerShell):
   ```
    Invoke-RestMethod -Method Post -Uri http://localhost:5000/file-upload
   ```
   ```
    Invoke-RestMethod -Uri http://localhost:5000/metrics
   ```

### Extending the Demo

While this demo runs locally, it can be extended to run in a Docker container. Once containerized, it can be deployed to Kubernetes or OpenShift environments. Prometheus can be configured to scrape metrics from this service and use customized queries for monitoring and visualization.
