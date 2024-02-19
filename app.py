import numpy as np
import pandas as pd
import pickle
from flask import Flask, request, render_template
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Read data from CSV file
data = pd.read_csv('train.csv')

# Load the AdaBoost model from the pickle file
with open('abmodel.pkl', 'rb') as f:
    model = pickle.load(f)

# Initialize StandardScaler
std_scaler = StandardScaler()
# Fit the scaler on your entire dataset once
std_scaler.fit(data.drop(['material','t_sisso', 't', 'tau','p_t_sisso','exp_label'], axis=1))

def get_features(composition):
    # Search for the composition in the 'material' column
    row = data[data['material'] == composition]
    if not row.empty:
        # Extract the corresponding features
        features = row.drop(['material','t_sisso', 't', 'tau','p_t_sisso','exp_label'], axis=1).values[0]
        return features
    else:
        print("Composition not found in the dataset.")
        return

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        composition = request.form['composition']
        return render_template('index.html', composition=composition)
    else:
        return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    composition = request.form['composition']
    features = get_features(composition)
    if features is not None:
        features_scaled = std_scaler.transform(features.reshape(1, -1))
        features_dict = {column: round(value, 4) for column, value in zip(data.columns[1:], features_scaled[0])}
        
        prediction = predict_stability(features_scaled)
        stability = "Stable" if prediction[0] == 1 else "Unstable"
        
        # Printing actual features
        print("Actual Features:", features)
        
        # Pass actual and selected features to the template
        return render_template('result.html', composition=composition, stability=stability, prediction=prediction, t_sisso=features[0], t=features[1], tau=features[2],
                               actual_features=dict(zip(data.columns[1:], features)))
    else:
        # If composition not found, still pass an empty dictionary for actual_features
        return render_template('result.html', composition=composition, stability="Composition not found in the dataset.", actual_features={})

def predict_stability(features_scaled):
    prediction = model.predict(features_scaled)
    print("Prediction:", prediction)  # Print the prediction
    return prediction

if __name__ == "__main__":
    app.run(debug=True)
