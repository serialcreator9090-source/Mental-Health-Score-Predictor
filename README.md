# Mental Health Score Predictor

An end-to-end Machine Learning project that predicts a user's mental health score based on digital habits, academic activities, lifestyle patterns, and stress levels.

## Project Overview

This project uses a trained Random Forest Regression model to estimate a mental health score from user-provided information.

The project includes:
- Exploratory Data Analysis (EDA)
- Data cleaning and preprocessing
- Feature engineering and encoding
- Linear Regression and Random Forest models
- Hyperparameter tuning using RandomizedSearchCV
- Model evaluation using MAE, RMSE, and R²
- FastAPI backend for predictions
- HTML, CSS, and JavaScript frontend

## Tech Stack

- Python
- Pandas and NumPy
- Scikit-learn
- Matplotlib and Seaborn
- FastAPI
- HTML, CSS, JavaScript
- Joblib

## Model Performance

| Metric | Tuned Random Forest |
|---|---:|
| MAE | 0.3389 |
| RMSE | 0.4512 |
| R² Score | 0.8841 |

## Project Structure

```text
Mental-Health-Score-Predictor/
├── backend/
│   ├── main.py
│   ├── mental_health_pipeline_compressed.pkl
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
└── README.md
```

## Running Locally

Install dependencies:

```bash
pip install -r backend/requirements.txt
```

Start the FastAPI server from the backend directory:

```bash
uvicorn main:app --reload
```

Open the API documentation:

```text
http://127.0.0.1:8000/docs
```

## Disclaimer

This project is an educational machine learning prototype. Its predictions are not clinical assessments, diagnoses, or substitutes for professional mental healthcare.

## Author

Developed as a Machine Learning and full-stack deployment learning project.
