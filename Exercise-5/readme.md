# Exercise 5: Hyperparameter Tuning with MLflow

## Objective

The objective of this exercise is to improve the QuickFoods delivery time prediction model by performing hyperparameter tuning and tracking all experiments using MLflow nested runs.

The exercise demonstrates MLOps concepts such as:

- Hyperparameter optimization using Grid Search and Random Search
- Experiment tracking using MLflow nested runs
- Logging parameters, metrics, and model artifacts
- Comparing multiple model configurations
- Selecting the best performing model automatically
- Registering the best model into the MLflow Model Registry

---

## Problem Statement

QuickFoods previously trained multiple delivery time prediction models and identified ensemble models as better performing approaches. However, different hyperparameter configurations can significantly affect model performance.

To find the optimal configuration, hyperparameter tuning is performed on:

- Random Forest Regressor using Grid Search
- Gradient Boosting Regressor using Random Search

Every trial is recorded as an independent child run under a parent MLflow experiment, enabling reproducibility and comparison of all tested configurations.

---

## Project Structure

```text
Exercise-5/
│
├── data/
│   └── delivery_times.csv
│
├── models/
│   ├── RandomForest_*.pkl
│   └── GradientBoosting_*.pkl
│
├── src/
│   ├── train_hyperparameter_tuning.py
│   └── register_best_model.py
│
├── mlflow.db
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

## Hyperparameter Tuning

Run the hyperparameter tuning script:

```bash
python src/train_hyperparameter_tuning.py
```

The script performs the following operations:

- Loads the QuickFoods delivery dataset
- Splits the data into training and testing sets
- Performs Grid Search on Random Forest Regressor
- Performs Random Search on Gradient Boosting Regressor
- Evaluates every model using MAE, MSE, RMSE, and R² score
- Creates nested MLflow runs for every hyperparameter trial
- Saves trained model artifacts
- Identifies the best model based on the lowest MAE

---

## MLflow Experiment Tracking

Start the MLflow user interface:

```bash
mlflow ui
```

Open the browser and navigate to:

```
http://127.0.0.1:5000
```

The MLflow UI provides:

- Parent hyperparameter sweep run
- Child runs for each hyperparameter combination
- Model parameters
- Evaluation metrics
- Saved model artifacts
- Experiment history and reproducibility information

---

## Model Registration

After identifying the best performing configuration, register the model using:

```bash
python src/register_best_model.py
```

The registration process:

- Searches all MLflow child runs
- Finds the run with the lowest MAE
- Retrieves the corresponding trained model
- Registers the model in MLflow Model Registry with a version number

---

## Results

The hyperparameter tuning process tested multiple configurations of Random Forest and Gradient Boosting models.

### Best Model Configuration

| Parameter | Value |
|---|---|
| Model | Gradient Boosting Regressor |
| n_estimators | 200 |
| learning_rate | 0.1 |
| max_depth | 3 |
| Best MAE | 5.751 minutes |
| MLflow Run ID | 8ef840c774a44df99503a04758b1b990 |
| Parent Run ID | e0d2f94cd439414b867b09e95a16612f |

The best performing model was successfully registered in MLflow Model Registry.

### Registered Model Details

| Attribute | Value |
|---|---|
| Registered Model Name | quickfoods-delivery-predictor |
| Model Version | 1 |
| Status | READY |

The experiment demonstrated that hyperparameter tuning can be used to systematically explore different model configurations and select the most suitable model for deployment.

---

## Grid Search vs Random Search

| Feature | Grid Search | Random Search |
|---|---|---|
| Search Method | Tests every possible parameter combination | Tests randomly selected combinations |
| Models Used | Random Forest Regressor | Gradient Boosting Regressor |
| Number of Trials | 18 combinations | 6 random combinations |
| Advantage | Exhaustive search within defined space | Faster search with lower computational cost |

---

## Learning Outcome

Through this exercise, we learned:

- How to perform hyperparameter tuning for ML models
- The difference between Grid Search and Random Search
- How to organize experiments using MLflow nested runs
- How to track parameters, metrics, and model artifacts
- How to automatically identify the best performing model
- How to register optimized models in MLflow Model Registry
- The importance of reproducibility and experiment management in MLOps workflows
