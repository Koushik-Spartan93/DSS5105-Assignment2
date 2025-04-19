
# Causal ATE Estimation API

This project implements a Flask-based API that estimates the **Average Treatment Effect (ATE)** using a linear regression model inspired by the **Rubin Causal Model**. It determines the causal impact of a treatment (e.g. participation in a carbon offset program) on engagement score, controlling for sustainability spending.

##  Model

The regression formula used is:

```
Yᵉ = α + τ·Wᵉ + β·Xᵉ + εᵉ
```

Where:
- **Yᵉ**: Engagement Score (observed outcome)
- **Wᵉ**: Treatment indicator (1 = participated, 0 = did not)
- **Xᵉ**: Sustainability Spending ($1,000s)
- **α, τ, β**: Parameters to be estimated
- **τ**: Interpreted as the **Average Treatment Effect (ATE)**

---

output : question 2 

![image](https://github.com/user-attachments/assets/ece2b720-d853-4ce9-ab15-1c340e957f6c)
output : question 1 

![image](https://github.com/user-attachments/assets/fbd2bc6d-6ddf-401b-a447-9040e591d574)

b) Report the estimated ATE (ˆ τ) and its statistical significance.
![image](https://github.com/user-attachments/assets/416c2c85-a745-4174-b760-9d02e1259a40)

![image](https://github.com/user-attachments/assets/ffb42605-e2f8-4d96-aae2-72e4ef1bfd98)


![Uploading image.png…]()


Explanation

app.py: This Python script defines a Flask web application that trains a linear regression model using a dataset and provides an API endpoint (/predict) to estimate engagement scores based on treatment (W) and sustainability spending (X). It handles HTTP requests, performs the prediction, and returns results in JSON format.
Dockerfile: The Dockerfile defines the environment needed to run the Flask app, including installing Python, required libraries, and setting up the application. It creates a portable image of your project.
Containerization: Using Docker ensures the application runs consistently across different machines by packaging code, dependencies, and environment together. This improves reproducibility, simplifies deployment, and avoids the “it works on my machine” problem.




