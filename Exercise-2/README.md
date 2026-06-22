# Exercise 2: QuickFoods Experiment Tracking using MLflow

## Objective

The objective of this exercise is to integrate MLflow into the QuickFoods delivery time prediction pipeline to track machine learning experiments, store parameters and evaluation metrics, and maintain reproducibility of model training runs.

The experiment demonstrates MLOps concepts such as:

- Experiment tracking
- Recording model parameters and performance metrics
- Logging trained model artifacts
- Managing multiple training runs
- Reproducibility of ML experiments

---

## Problem Statement

In traditional machine learning development, it becomes difficult to track different training runs, model versions, and their performance.

QuickFoods requires a system that can answer questions such as:

- Which model configuration produced the best result?
- What parameters were used during training?
- Which model artifact belongs to a particular experiment?

MLflow solves this problem by storing experiment metadata, metrics, parameters, and artifacts.

---

## Project Structure

```
Exercise-2/
│
├── data/
│   └── delivery_times.csv
│
├── models/
│   └── delivery_time_model.pkl
│
├── src/
│   ├── __init__.py
│   └── train_with_mlflow.py
│
├── mlruns/
│
├── requirements.txt
└── README.md
```

---

## Installation and Setup

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

---

## Running MLflow Training

Execute the training script:

```bash
python src/train_with_mlflow.py
```

The script performs the following tasks:

- Loads the QuickFoods delivery dataset
- Splits the data into training and testing sets
- Trains the Linear Regression model
- Calculates evaluation metrics
- Logs parameters and metrics into MLflow
- Saves the trained model as an MLflow artifact

---

## Viewing MLflow Dashboard

Start the MLflow tracking server:

```bash
mlflow ui
```

Open the browser and navigate to:

```
http://127.0.0.1:5000
```

The MLflow dashboard provides:

- Experiment name
- Run ID
- Execution time
- Logged parameters
- Performance metrics
- Model artifacts

---

## Results

### Model Training and MLflow Tracking Results

The experiment was executed successfully and the model training details were recorded in MLflow.

The following information was logged:

| Logged Information | Description |
|--------------------|-------------|
| Model Name | Linear Regression |
| Parameters | Training configuration and dataset information |
| Metrics | MAE, MSE, RMSE, and R² score |
| Artifact | Trained model file |
| Run Details | Unique MLflow run ID and execution timestamp |

MLflow successfully stored the complete experiment history, making the model training process reproducible.

---

### MLflow UI Results

The MLflow dashboard displayed:

- Experiment details
- Individual training runs
- Model evaluation metrics
- Logged model artifacts
- Run metadata for comparison and analysis

---

## Output Screenshots

Add the following screenshots:

### Figure 1: MLflow Training Execution

<img width="998" height="173" alt="image" src="https://github.com/user-attachments/assets/1d3299c3-da93-4f34-8e7e-fbbf394ce674" />


```bash
python src/train.py
```

---

### Figure 2: MLflow Experiment Dashboard

<img width="1538" height="221" alt="image" src="https://github.com/user-attachments/assets/72323835-5924-42dc-8fbe-9abce6d40fa0" />


---

### Figure 3: MLflow Run Details

<img width="1918" height="972" alt="image" src="https://github.com/user-attachments/assets/1ea6fe4c-0fd2-42d6-98b5-3b30314e1b4c" />


## Learning Outcome

Through this exercise, we learned:

- How to integrate MLflow into an ML pipeline.
- How to track machine learning experiments.
- How to record model parameters and evaluation metrics.
- How to store and retrieve trained model artifacts.
- How MLflow improves reproducibility and model management.
- The importance of experiment tracking in MLOps workflows.
