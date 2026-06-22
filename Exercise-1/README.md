# Exercise 1: QuickFoods Model Artifact and Reproducible ML Pipeline

## Objective

The objective of this exercise is to create a reproducible Machine Learning project that predicts food delivery time using a baseline Linear Regression model.

The project demonstrates MLOps fundamentals such as:
- Proper project structure
- Virtual environment management
- Dependency tracking using requirements.txt
- Script-based model training
- Model artifact generation using Pickle format
- Version control using Git

---

## Problem Statement

QuickFoods is a food delivery company that wants to estimate the delivery time of an order based on different order and traffic related factors.

### Input Features

- `distance_km` – Distance between restaurant and customer
- `items_count` – Number of items in the order
- `is_peak_hour` – Whether the order is placed during peak hours (0 or 1)
- `traffic_level` – Traffic intensity level (1 to 3)

### Target Variable

- `delivery_time_min` – Estimated delivery time in minutes

---

## Project Structure

```
Exercise-1/
│
├── data/
│   └── delivery_times.csv
│
├── models/
│   └── delivery_time_model.pkl
│
├── src/
│   ├── __init__.py
│   └── train.py
│
├── view_pkl.py
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

Install required dependencies:

```bash
pip install -r requirements.txt
```

---

## Training the Model

Run the training script:

```bash
python src/train.py
```

The script:
- Loads the delivery dataset
- Splits data into training and testing sets
- Trains a Linear Regression model
- Evaluates model using MAE and MSE
- Saves the trained model as `delivery_time_model.pkl`

---

## Model Artifact Analysis

The saved model artifact can be inspected using:

```bash
python view_pkl.py
```

The script displays:
- Model type
- Learned coefficients (weights)
- Intercept (bias)
- Feature names
- Manual prediction using the linear regression equation
- Comparison with Scikit-learn prediction

---

## Mathematical Representation

The Linear Regression model predicts delivery time using:

```
delivery_time = w1 × distance_km + w2 × items_count + w3 × is_peak_hour + w4 × traffic_level + bias
```

The weights are learned from training data and represent the influence of each feature on the predicted delivery time.

---

## Learning Outcome

Through this exercise, we learned:

- Building a reproducible ML project
- Managing dependencies with virtual environments
- Training ML models through Python scripts
- Saving and loading model artifacts
- Understanding that ML models store learned parameters rather than human-like intelligence
- Using Git for version control
