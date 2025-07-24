# 💓 CardioSmart360

## 🩺 Project Overview

**CardioSmart360** is a comprehensive desktop application that provides heart disease risk analysis and patient management through a clean Tkinter-based GUI, backed by machine learning and persistent MySQL + Excel storage. It enables users to securely register, log in, input patient data, visualize health metrics, and generate predictive insights using ML models like Logistic Regression, Random Forest, and Gradient Boosting.

---

## 🚀 Features

* 🔐 **Secure Login System**: User registration and login with admin code validation.
* 👤 **Patient Data Management**: Add, update, and search patient records including lifestyle and medical details.
* 🤖 **ML-Based Heart Disease Prediction**: Logistic Regression, Random Forest, and Gradient Boosting models.
* 📊 **Interactive Visualizations**: Line charts, radar plots, heatmaps, and boxplots for metric analysis.
* 💾 **MySQL + Excel Integration**: Dual data storage for flexibility and portability.
* 📃 **Risk Report Generation**: Summarized insights from ML models and patient features.
* 📘 **In-App Help**: Dataset feature explanations and user instructions.

---

## 🛠 Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Subhapreet21/CardioSmart-360.git
   cd CardioSmart360
   ```

2. **Install Dependencies**

   ```bash
   pip install numpy pandas scikit-learn matplotlib
   pip install mysql-connector-python pymysql openpyxl seaborn Pillow
   ```

3. **Configure MySQL**

   * Ensure MySQL is running locally.
   * Update credentials in:

     * `MySQL.py`
     * `register.py`
     * `Login.py`

---

## 🧪 Usage

* **Run the main application**

  ```bash
  python main.py
  ```

* **Run extended/test version**

  ```bash
  python main_test.py
  ```

* **New User Registration** (admin code required)

* **Login** to access patient entry, prediction, and reports

---

## 📁 Project Structure

```
CardioSmart360/
├── backend.py                # ML logic for training and prediction
├── main.py                   # Main GUI app
├── main_test.py              # Extended testing GUI
├── register.py               # Registration screen
├── Login.py                  # Login + password reset
├── MySQL.py                  # MySQL DB operations
├── info.py                   # Dataset info/help window
├── Images/                   # GUI assets (icons, backgrounds)
├── heart_with_smoker_cleaned.csv
├── heart_with_smoker_updated.csv
├── heart.csv
├── refined_heart_dataset.csv
├── Heart_data.xlsx           # Excel record storage
├── requirements.txt
└── README.md
```

---

## 📊 Datasets

* `heart_with_smoker_cleaned.csv`: Primary dataset for ML predictions.
* `refined_heart_dataset.csv`: Normalized/preprocessed dataset.
* `heart_with_smoker_updated.csv`: Extended dataset with extra entries.
* `heart.csv`: Base UCI dataset.
* `Heart_data.xlsx`: Patient data saved via GUI.

---

## 🔍 Core Modules

| Module         | Description                                                            |
| -------------- | ---------------------------------------------------------------------- |
| `main.py`      | Launch GUI for data input, visualization, and ML-based prediction      |
| `main_test.py` | Extended version for testing, additional features, graphs, and reports |
| `backend.py`   | Loads data, trains ML models, performs predictions                     |
| `MySQL.py`     | Connects and saves patient records to MySQL                            |
| `register.py`  | Registers new users (admin code protected)                             |
| `Login.py`     | Handles user login and password reset                                  |
| `info.py`      | Shows dataset feature explanations and help text                       |

---

## 🧑‍⚕️ GUI Layout

* **Home**: Entry for patient name, gender, age, metrics, smoking status, etc.
* **Graphs**: View health data visualizations using matplotlib/seaborn.
* **Report**: Risk prediction summary and contributing factors.
* **Info**: Feature-by-feature guide for dataset understanding.
* **Controls**: Buttons for save, update, clear, search, and toggle smoker mode.

---

## 💽 Database Info

* **MySQL**: Primary storage with auto-table creation.
* **Excel**: Mirror backup using `Heart_data.xlsx`.
* ⚠️ *User Credentials*:

  ```txt
  user: root
  password: YOUR_MYSQL_PASSWORD
  ```

  *(Change before deploying to production)*

---

## 🧪 Testing & Debug

* Use `main_test.py` for:

  * Advanced reporting
  * Update/search capability
  * Full feature demonstration

> 🔧 Unit tests are not included. You can extend test coverage for `backend.py` and `MySQL.py`.

---

## 📚 Acknowledgements

* UCI Heart Disease Dataset
* Libraries: Python, Tkinter, scikit-learn, matplotlib, pandas, MySQL, Pillow, openpyxl, seaborn

---

## ❗ Notes

* Ensure all image files are available in `Images/` for UI rendering.
* Modify MySQL credentials and schema as per your environment.
* Check code comments for debugging support or guidance.
