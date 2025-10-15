# 🚢 Titanic Survival Prediction (Machine Learning Project)

### 📘 Description
This project trains a **Logistic Regression** model to predict passenger survival using the **Titanic dataset** from Kaggle.

It includes:
- Data cleaning and feature engineering  
- Model training and evaluation  
- A small function `predict_survival()` that outputs survival probability

---

### ⚙️ How to Run

1. **Clone this repository:**
   git clone https://github.com/bach88/titanic-survival-prediction.git
   cd titanic-survival-prediction
2. **Install dependencies:**
   pip install -r requirements.txt
3. **Download dataset:**
   Go to Kaggle Titanic Dataset
   Place train.csv in the same folder as notebook.ipynb
4. **Run the notebook:**
   jupyter notebook notebook.ipynb
**Input:**
predict_survival(3, "male", 22, 1, 0, 7.25, "S")
**Output:**
0.14  # ≈14% survival probability
**Another example:**
  predict_survival(1, "female", 29, 0, 0, 100, "C")
**Output:**
  0.97  # ≈97% survival probability
