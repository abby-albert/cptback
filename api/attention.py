## Attention Sample API endpoint
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource

# Import the AttentionModel class from the model file
# from model.attention import AttentionModel

attention_api = Blueprint('attention_api', __name__,
                          url_prefix='/api/attention')

api = Api(attention_api)

class AttentionAPI:
    class _Predict(Resource):
        
        def post(self):
            """ Semantics: In HTTP, POST requests are used to send data to the server for processing.
            Sending attention data to the server to get a score prediction fits the semantics of a POST request.
            
            POST requests send data in the body of the request...
            1. which can handle much larger amounts of data and data types than URL parameters
            2. using an HTTPS request, the data is encrypted, making it more secure
            3. a JSON formatted body is easy to read and write between JavaScript and Python, great for Postman testing
            """     
            # Get the attention data from the request
            attention_data = request.get_json()

            # Get the singleton instance of the AttentionModel
            attention_model = AttentionModel.get_instance()
            # Predict the score based on the attention data
            predicted_score = attention_model.predict(attention_data)

            # Return the predicted score as JSON
            return jsonify({'predicted_score': predicted_score})

    api.add_resource(_Predict, '/predict')
