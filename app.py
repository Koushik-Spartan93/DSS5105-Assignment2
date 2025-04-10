from flask import Flask, request, jsonify
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

app = Flask(__name__)

data = {
    'Yobs': [137, 118, 124, 124, 120, 129, 122, 142, 128, 114,
             132, 130, 130, 112, 132, 117, 134, 132, 121, 128],
    'W':    [0, 1, 1, 1, 0, 1, 1, 0, 0, 1,
             1, 0, 0, 1, 0, 1, 0, 0, 1, 1],
    'X':    [19.8, 23.4, 27.7, 24.6, 21.5, 25.1, 22.4, 29.3, 20.8, 20.2,
             27.3, 24.5, 22.9, 18.4, 24.2, 21.0, 25.9, 23.2, 21.6, 22.8]
}
df = pd.DataFrame(data)


X_train = df[['W', 'X']]  # predictors: Treatment + Spending
y_train = df['Yobs']      # outcome: Engagement Score
model = LinearRegression().fit(X_train, y_train)

# Add intercept
df['intercept'] = 1

# Fit linear regression model
model = sm.OLS(df['Yobs'], df[['intercept', 'W', 'X']])
results = model.fit()

# Display results
print(results.summary())


@app.route("/predict")
def predict():
    try:
        W = float(request.args.get("W"))
        X = float(request.args.get("X"))
    except (TypeError, ValueError):
        return jsonify({"error": "Please provide valid numeric values for W and X"}), 400

    y_pred = model.predict([[W, X]])[0]

    try:
        with open("output.txt", "a") as f:
            f.write(f"Input W: {W}, X: {X} -> Predicted Y: {y_pred:.2f}\n")
        print("✔️ Successfully wrote to output.txt")
    except Exception as e:
        print("❌ Failed to write to output.txt:", e)

    return jsonify({"W": W, "X": X, "predicted_Yobs": round(y_pred, 2)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000, debug=True)
