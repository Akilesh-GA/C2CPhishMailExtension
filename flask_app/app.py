import numpy as np
import pandas as pd
from flask import Flask, request, render_template, jsonify
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

try:
    df = pd.read_csv('flask_app/flask/phishing_mail_final.csv', encoding='ISO-8859-1')
except Exception as e:
    logging.error(f"Error reading CSV file: {e}")
    df = pd.DataFrame(columns=['Message', 'Category'])

data = df.where((pd.notnull(df)), '')
data['Category'] = data['Category'].str.strip()
data.loc[data['Category'] == 'spam', 'Category'] = 0
data.loc[data['Category'] == 'ham', 'Category'] = 1

X = data['Message']
Y = data['Category'].astype(int)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

feature_extraction = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
X_train_features = feature_extraction.fit_transform(X_train)
X_test_features = feature_extraction.transform(X_test)

model = LogisticRegression()
model.fit(X_train_features, Y_train)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    message = data['message']
    try:
        input_data_feature = feature_extraction.transform([message])
        prediction_proba = model.predict_proba(input_data_feature)
        phishing_forecast = prediction_proba[0][0] * 100
        legitimate_forecast = prediction_proba[0][1] * 100

        prediction = model.predict(input_data_feature)
        result = "Legitimate Mail" if prediction[0] == 1 else "Phishing Mail"

        return jsonify(result=result, phishing_forecast=phishing_forecast, legitimate_forecast=legitimate_forecast)
    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        return jsonify(result="Error during prediction. Please try again.", phishing_forecast=0, legitimate_forecast=0)

if __name__ == "__main__":
    app.run(debug=True)