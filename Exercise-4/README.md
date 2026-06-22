# Exercise 4: Docker for Model Packaging and Local Model Deployment

## Objective

The objective of this exercise is to package the QuickFoods delivery time prediction model into a Docker container and run the model application in a reproducible environment.

The exercise demonstrates MLOps concepts such as:

- Containerizing Machine Learning applications using Docker
- Creating a Dockerfile for ML projects
- Packaging trained model artifacts with application code
- Building and tagging Docker images
- Running containers with custom input parameters
- Ensuring consistent execution across different environments

---

## Problem Statement

QuickFoods has developed a machine learning model to predict food delivery time. Although the model works locally, the company requires a portable package that can run consistently across different systems such as local machines, cloud servers, and production environments.

To solve this problem, the trained model is converted into a CLI-based application and packaged inside a Docker container.

---

## Project Structure

```text
Exercise-4/
│
├── data/
│   └── delivery_times.csv
│
├── models/
│   └── delivery_time_model.pkl
│
├── src/
│   └── predict_cli.py
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation and Setup

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Local Model Testing

Before containerization, the model was tested locally using the CLI application.

Run the prediction script:

```bash
python src/predict_cli.py \
--distance_km 4.2 \
--items_count 3 \
--is_peak_hour 1 \
--traffic_level 2
```

Sample output:

```json
{
  "input": {
    "distance_km": 4.2,
    "items_count": 3,
    "is_peak_hour": 1,
    "traffic_level": 2
  },
  "prediction": {
    "delivery_time_min": 41.25
  }
}
```

---

## Dockerfile Configuration

A Dockerfile was created to package the application.

The Docker configuration performs the following tasks:

- Uses Python 3.11 slim image as the base environment
- Creates a working directory inside the container
- Installs required Python dependencies
- Copies the source code and trained model artifact
- Executes the CLI prediction application as the container entry point

---

## Building Docker Image

Build the Docker image and assign a version tag:

```bash
docker build -t quickfoods-delivery-model:0.1 .
```

Verify the created Docker image:

```bash
docker images
```

Docker image details:

- Image Name: `quickfoods-delivery-model`
- Version Tag: `0.1`

---

## Running Docker Container

### Test Case 1

Run the container with the following input:

```bash
docker run --rm quickfoods-delivery-model:0.1 \
--distance_km 4.2 \
--items_count 3 \
--is_peak_hour 1 \
--traffic_level 2
```

Output:

```json
{
  "input": {
    "distance_km": 4.2,
    "items_count": 3,
    "is_peak_hour": 1,
    "traffic_level": 2
  },
  "prediction": {
    "delivery_time_min": 41.25
  }
}
```

---

### Test Case 2

Run another prediction:

```bash
docker run --rm quickfoods-delivery-model:0.1 \
--distance_km 1.0 \
--items_count 1 \
--is_peak_hour 0 \
--traffic_level 1
```

Output:

```json
{
  "input": {
    "distance_km": 1.0,
    "items_count": 1,
    "is_peak_hour": 0,
    "traffic_level": 1
  },
  "prediction": {
    "delivery_time_min": 14.26
  }
}
```

---

## Docker Container Lifecycle Commands

The following Docker commands were used to inspect container and image information:

List running containers:

```bash
docker ps
```

List all containers:

```bash
docker ps -a
```

List available Docker images:

```bash
docker images
```

These commands help monitor the Docker environment and manage containerized applications.

---

## Results

The QuickFoods delivery time prediction model was successfully containerized using Docker.

The Docker image `quickfoods-delivery-model:0.1` was created successfully, and the container executed prediction requests correctly for different input combinations.

The model produced the following prediction results:

| Test Case | Input Conditions | Predicted Delivery Time |
|---|---|---|
| Test Case 1 | Distance: 4.2 km, Items: 3, Peak Hour: Yes, Traffic Level: 2 | 41.25 minutes |
| Test Case 2 | Distance: 1.0 km, Items: 1, Peak Hour: No, Traffic Level: 1 | 14.26 minutes |

This confirms that the model application runs successfully both locally and inside a Docker container.

---

## Learning Outcome

Through this exercise, we learned:

- How to package an ML application using Docker
- How to create a Dockerfile for reproducible deployment
- How to include model artifacts and source code inside containers
- How to build and tag Docker images
- How to run containerized ML applications using command-line inputs
- The importance of containerization for portable and consistent ML deployment
