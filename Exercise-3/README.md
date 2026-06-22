# Exercise 3: MLflow Model Comparison and Model Registry

## Objective

The objective of this exercise is to compare multiple Machine Learning models for predicting QuickFoods delivery time and track all experiments using MLflow.

The exercise demonstrates MLOps concepts such as:

- Training and comparing multiple ML models
- Experiment tracking using MLflow
- Logging model parameters and evaluation metrics
- Saving model artifacts for reproducibility
- Selecting the best performing model based on evaluation metrics
- Registering the best model in MLflow Model Registry

---

## Problem Statement

QuickFoods wants to improve the accuracy of delivery time prediction by evaluating different Machine Learning algorithms and identifying the most suitable model for production deployment.

The models used in this experiment are:

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

The best model is selected based on the lowest Mean Absolute Error (MAE) and overall prediction performance.

---

## Project Structure

```text
Exercise-3/
│
├── data/
│   └── delivery_times.csv
│
├── models/
│   ├── LinearRegression.pkl
│   ├── RandomForest.pkl
│   └── GradientBoosting.pkl
│
├── src/
│   ├── train_compare_models.py
│   └── register_best_model.py
│
├── mlruns/
│
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

## Model Training and Comparison

Run the training script:

```bash
python src/train_compare_models.py
```

The script performs the following operations:

- Loads the QuickFoods delivery dataset
- Splits the dataset into training and testing sets
- Trains Linear Regression, Random Forest, and Gradient Boosting models
- Evaluates each model using MAE, MSE, RMSE, and R² score
- Logs experiment details, metrics, and model artifacts into MLflow
- Identifies the best performing model based on MAE

---

## MLflow UI

Start the MLflow user interface using:

```bash
mlflow ui
```

Open the browser and navigate to:

```
http://127.0.0.1:5000
```

The MLflow dashboard allows inspection of:

- Experiment runs
- Model parameters
- Performance metrics
- Saved model artifacts

---

## Model Registration

After identifying the best model, register it using:

```bash
python src/register_best_model.py
```

The registration process:

- Searches MLflow experiment history
- Selects the model with the lowest MAE
- Registers the best model with a version number
- Stores a reproducible reference for deployment

---

## Results

The trained models were compared based on their prediction performance.

| Model | Description |
|---|---|
| Linear Regression | Baseline model for delivery time prediction |
| Random Forest Regressor | Ensemble model with improved prediction capability |
| Gradient Boosting Regressor | Best performing model and selected for registration |

The MLflow experiment tracking system stored:

- Model parameters
- Evaluation metrics (MAE, MSE, RMSE, R²)
- Training runs
- Model artifacts
- Registered model information

The best performing model was selected and promoted to the MLflow Model Registry for future deployment.

---

## Learning Outcome

Through this exercise, we learned:

- How to train and compare multiple Machine Learning models
- How to use MLflow for experiment tracking
- How to analyze model performance using different evaluation metrics
- How to store and manage model artifacts
- How to register the best model for reproducible deployment workflows
- The importance of experiment tracking in MLOps pipelines
