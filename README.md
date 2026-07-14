# 🛡️ Phishing Email Detection Model

A machine learning-based phishing email detection system built with **Python** and **Scikit-learn**. The model analyzes email content using **TF-IDF** feature extraction and classifies emails as **Phishing** or **Safe**, helping demonstrate the application of NLP in cybersecurity.

## 🚀 Features

- 📧 Train on phishing and legitimate email datasets
- 🔍 Extract email features using TF-IDF
- 🤖 Classify emails as **Phishing** or **Safe**
- 📊 Display model accuracy and confusion matrix
- 💬 Predict the category of custom email text
- 📈 Evaluate model performance with classification metrics

## 🛠️ Technologies Used

- Python
- Scikit-learn
- Pandas
- NumPy
- Matplotlib

## 📂 Project Structure

```text
Phishing-Email-Detection/
│── phishing_detector.py
│── phishing_emails.csv
│── requirements.txt
└── README.md
```

## ⚙️ Installation

```bash
git clone https://github.com/your-username/Phishing-Email-Detection.git

cd Phishing-Email-Detection

pip install -r requirements.txt
```

## ▶️ Run the Project

```bash
python 
```

## 📌 Example Output

```text
Accuracy: 96.5%

Enter Email:
Your account has been suspended. Verify immediately.

Prediction: PHISHING
```

## 📊 Model Workflow

1. Load the email dataset.
2. Preprocess and clean the text.
3. Convert text into TF-IDF features.
4. Train the machine learning model.
5. Evaluate using accuracy and confusion matrix.
6. Predict new email messages.

## 🔮 Future Enhancements

- Support multiple ML algorithms
- Detect malicious URLs
- Build a Flask/Django web application
- Deploy using Streamlit
- Improve accuracy with larger datasets

## 📜 License

This project is licensed under the **MIT License**.

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!
