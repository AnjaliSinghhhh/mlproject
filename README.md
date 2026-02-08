##END TO END MACHINE LEARNING PROJECT 
# Student Exam Performance Predictor

## 📌 Project Overview

The **Student Exam Performance Predictor** is a machine learning-based web application that predicts a student’s **Maths exam score** based on demographic data, parental education, test preparation, and performance in other subjects (Reading and Writing). This project demonstrates **end-to-end ML workflow**, from data preprocessing and model training to deployment as a Flask web app.

## 🛠 Features

* Predicts Maths scores based on:

  * Gender
  * Race/Ethnicity
  * Parental level of education
  * Lunch type
  * Test preparation course
  * Writing and Reading scores
* Simple and intuitive **web interface** built with Flask
* Real-time predictions
* Input validation for accurate results

## 📊 Dataset

The app uses the **Students Performance Dataset** from Kaggle, which contains:

| Feature                     | Description                        |
| --------------------------- | ---------------------------------- |
| Gender                      | Student’s gender (male/female)     |
| Race/Ethnicity              | Group classification (A–E)         |
| Parental Level of Education | Highest parental education level   |
| Lunch                       | Standard or free/reduced           |
| Test Preparation Course     | Completed or none                  |
| Reading Score               | Score out of 100                   |
| Writing Score               | Score out of 100                   |
| Maths Score                 | Score out of 100 (Target variable) |

**Source:** [Kaggle: Students Performance Dataset](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)

## 🧠 Model

* **Model type:** Regression model (Random Forest / XGBoost / Linear Regression)
* **Target variable:** Maths Score
* **Features:** All other columns except Maths score
* **Evaluation Metrics:** MAE, RMSE, R² Score

## 💻 Installation

1. **Clone the repository**

```bash
git clone https://github.com/AnjaliSinghhhh/mlproject.git
cd mlproject
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the Flask app**

```bash
python app.py
```

5. **Open the app in browser**

```
http://127.0.0.1:5000/predictdata
```

## DEMO VIDEO
[![Watch Demo](demo_thumbnail.png)](PROJECT_RECORDING.mp4)

## 📸  Screenshot

![Flask App Screenshot](https://raw.githubusercontent.com/AnjaliSinghhhh/mlproject/main/assets/project_img.png)



## 🔮 Usage

1. Open the web app.
2. Select your **Gender**, **Race**, **Parental Education**, **Lunch type**, and **Test Preparation Course**.
3. Enter **Writing** and **Reading** scores.
4. Click **"Predict your Maths Score"** to get the predicted Maths score instantly.

## 🏆 Key Takeaways

* Demonstrates **data preprocessing, model training, and deployment**.
* Shows ability to **build interactive ML applications**.
* Highlights knowledge of **regression modeling, feature engineering, and evaluation**.
* Ready to **showcase in ML portfolios or interviews**.

## 📂 Future Improvements

* Add predictions for **all subjects**.
* Include **visualizations** for predicted vs actual scores.
* Deploy on **Heroku or AWS** for public access.
* Implement **model comparison** (Random Forest vs XGBoost vs Linear Regression).

## ⚡ Tech Stack

* Python 3.x
* Flask
* Scikit-learn / XGBoost
* Pandas / NumPy
* HTML/CSS (Bootstrap optional)

---

