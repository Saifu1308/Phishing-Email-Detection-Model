import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

import matplotlib.pyplot as plt

# -----------------------------
# Load Dataset
# -----------------------------
data = pd.read_csv("phishing_emails.csv")

X = data["text"]
y = data["label"]

# -----------------------------
# Split Dataset
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# Create ML Pipeline
# -----------------------------
model = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english")),
    ("classifier", MultinomialNB())
])

# -----------------------------
# Train Model
# -----------------------------
model.fit(X_train, y_train)

# -----------------------------
# Test Model
# -----------------------------
predictions = model.predict(X_test)

print("\nAccuracy:")
print(f"{accuracy_score(y_test, predictions) * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, predictions))

# -----------------------------
# Confusion Matrix
# -----------------------------
cm = confusion_matrix(y_test, predictions)

plt.imshow(cm)

plt.title("Confusion Matrix")
plt.colorbar()

plt.xticks([0,1],["Phishing","Safe"])
plt.yticks([0,1],["Phishing","Safe"])

plt.xlabel("Predicted")
plt.ylabel("Actual")

for i in range(len(cm)):
    for j in range(len(cm)):
        plt.text(j, i, cm[i][j], ha="center", va="center")

plt.show()

# -----------------------------
# Test New Email
# -----------------------------
print("\n----- Email Prediction -----")

email = input("Enter email text:\n")

prediction = model.predict([email])[0]

print("\nPrediction:", prediction.upper())
