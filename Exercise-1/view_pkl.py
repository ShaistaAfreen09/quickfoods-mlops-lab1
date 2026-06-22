import joblib

# Load saved model
model = joblib.load("models/delivery_time_model.pkl")

# Model type
print("Model Type:")
print(type(model))

# Coefficients
print("\nWeights:")
print(model.coef_)

# Intercept
print("\nIntercept:")
print(model.intercept_)

# Feature names
print("\nFeatures:")
print(model.feature_names_in_)

# Manual prediction
x = [5, 3, 1, 2]

manual = sum(w * v for w, v in zip(model.coef_, x)) + model.intercept_

sklearn_pred = model.predict([x])[0]

print("\nManual Prediction:")
print(manual)

print("\nSklearn Prediction:")
print(sklearn_pred)