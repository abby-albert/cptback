from flask import Flask, request, jsonify
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

app = Flask(__name__)

# Dummy attention data
attention_data = pd.DataFrame({
    'subject': ['Math', 'Science', 'History', 'English'],
    'attention': ['focused', 'divided', 'focused', 'divided'],
    'solutions': [2, 1, 3, 0],
    'score': [8.5, 9.2, 7.8, 9.5]  # Assuming scores for each subject
})

# Train a decision tree regressor (this is just a placeholder)
X = attention_data.drop(['subject', 'attention', 'score'], axis=1)
y = attention_data['attention']
dt = DecisionTreeRegressor()
dt.fit(X, y)

@app.route('/predict_probability', methods=['POST'])
def predict_probability():
    if request.method == 'POST':
        data = request.json
        
        # Use the provided solutions input
        solutions_input = int(data['solutionsInput'])
        
        # Dummy prediction for attention (this is just a placeholder)
        predicted_attention = dt.predict([[solutions_input]])[0]
        
        # Calculate the probability (this is just a placeholder)
        probability = len(attention_data[(attention_data['solutions'] == solutions_input) & 
                                         (attention_data['attention'] == predicted_attention) & 
                                         (attention_data['score'] > 9.0)]) / len(attention_data) * 100
        
        return jsonify({'probability': probability})

if __name__ == '__main__':
    app.run(debug=True)

dt.fit(X_train, y_train)

# Test the model
y_pred = dt.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)

# Fetch: In the frontend JavaScript code, fetch() is used to send a POST request to the /predict_probability
# endpoint of the Flask server. This request includes data about the subject, attention, and solutions input
# provided by the user. The server processes this data and returns a response containing the calculated probability.

# Endpoint (/predict_probability): This Flask endpoint listens for POST requests. When it receives a POST request, 
# it extracts the data from the request's JSON payload. It then uses this data to calculate the probability of getting 
# a score above 9.0/10.0. This probability is calculated based on the dummy data stored in attention_data. Finally, 
# it returns the calculated probability as a JSON response.