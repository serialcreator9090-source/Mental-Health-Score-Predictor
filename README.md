# 🧠 Mental Health Score Predictor

An end-to-end Machine Learning application that predicts a mental health score based on lifestyle, social media usage, academic activities, sleep patterns and other user-provided factors.

The project demonstrates the complete ML development workflow — from data preprocessing and model training to API development, frontend integration and cloud deployment.

## 🚀 Live Demo

**[Visit Mental Health Score Predictor](https://mental-health-score-predictor-1-yg9q.onrender.com)**

**[View Source Code on GitHub](https://github.com/serialcreator9090-source/Mental-Health-Score-Predictor)**

> Note: This is an educational machine learning prototype. Its predictions are not clinically validated and must not be used for medical diagnosis or treatment decisions.

## 📌 Project Overview

The application uses a trained Random Forest Regression model to estimate a mental health score from multiple input features, including:

- Age and gender
- Country and academic level
- Most-used social media platform
- Purpose of social media usage
- Average daily social media usage
- Daily phone unlocks
- Study hours
- Physical activity hours
- Sleep hours per night
- Stress level

Users enter their information through a web interface and receive a predicted score through the deployed machine learning API.

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Model | Random Forest Regressor |
| Model Optimization | RandomizedSearchCV |
| Model Serialization | Joblib |
| Backend | FastAPI |
| Frontend | HTML, CSS, JavaScript |
| Deployment | Render |
| Development | VS Code, Jupyter Notebook |

## 🧠 Machine Learning Workflow

1. **Data Collection:** Used the Student Social Media and Mental Health Impact dataset.
2. **Data Preprocessing:** Handled duplicate records, prepared categorical and numerical features, and grouped less frequent countries.
3. **Feature Engineering:** Applied numerical scaling, ordinal encoding and one-hot encoding.
4. **Model Development:** Experimented with Linear Regression and Random Forest Regression.
5. **Hyperparameter Tuning:** Used RandomizedSearchCV with 5-fold cross-validation.
6. **Model Evaluation:** Evaluated the model using MAE, RMSE and R².
7. **Model Deployment:** Saved the trained preprocessing and prediction pipeline using Joblib.

## 📊 Model Performance

The tuned Random Forest model achieved the following results on the held-out test dataset:

| Evaluation Metric | Result |
|---|---:|
| MAE | 0.3389 |
| RMSE | 0.4512 |
| R² Score | 0.8841 |
| Cross-validation Mean R² | 0.8569 |

The complete trained pipeline was compressed using Joblib for deployment.

## 🏗️ System Architecture

```text
             USER
               |
               v
       HTML / CSS / JavaScript
               |
               v
          Form Submission
               |
               v
          FastAPI Backend
               |
               v
       Input Preprocessing
               |
               v
       Trained ML Pipeline
       (Random Forest Model)
               |
               v
       Predicted Score
               |
               v
        Frontend Result
```

## 📁 Project Structure

```text
Mental-Health-Score-Predictor/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── main.py
├── mental_health_pipeline_compressed.pkl
├── compress_model.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/serialcreator9090-source/Mental-Health-Score-Predictor.git
```

### 2. Navigate into the project

```bash
cd Mental-Health-Score-Predictor
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**Ubuntu/Linux:**
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the FastAPI server

```bash
uvicorn main:app --reload
```

### 6. Open the API documentation

Visit:

```text
http://127.0.0.1:8000/docs
```

The interactive Swagger documentation allows you to test the prediction endpoint.

To use the frontend locally, open `frontend/index.html` through a local development server and ensure its API URL points to your local backend.

## 🔌 API Endpoint

**POST** `/predict`

Accepts user information in JSON format and returns a predicted mental health score.

Example response:

```json
{
  "predicted_mental_health_score": 7.32
}
```

The actual prediction depends on the submitted input.

## 🌐 Deployment

The application is deployed using Render:

- **Frontend:** Render Static Site
- **Backend:** Render Web Service
- **API:** FastAPI
- **Model:** Compressed Scikit-learn pipeline

## 🎯 Learning Outcomes

Through this project, I explored and implemented:

- End-to-end machine learning development
- Data preprocessing and feature engineering
- Regression model training and evaluation
- Hyperparameter optimization
- Model serialization and compression
- REST API development using FastAPI
- Frontend and backend integration
- Cloud deployment of an ML application

## 👨‍💻 Author

**Yash**

B.Tech – Robotics & Automation

Interested in Machine Learning, Artificial Intelligence, Robotics and Automation.

---

⭐ If you find this project interesting, feel free to explore the repository and try the live application.
