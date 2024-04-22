## Python Attention Model, prepared for an attention.py file

# Import the required libraries for the AttentionModel class
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import numpy as np
import seaborn as sns

class AttentionModel:
    """A class used to represent the Attention Model for score prediction.
    """
    # a singleton instance of AttentionModel, created to train the model only once, while using it for prediction multiple times
    _instance = None
    
    # constructor, used to initialize the AttentionModel
    def __init__(self):
        # the attention ML model
        self.model = None
        self.dt = None
        # define ML features and target
        self.features = ['subject', 'attention', 'solutions']
        self.target = 'score'
        # load the attention dataset
        self.attention_data = pd.read_csv('attention.csv')
        # one-hot encoder used to encode 'attention' column
        self.encoder = OneHotEncoder(handle_unknown='ignore')

    # clean the attention dataset, prepare it for training
    def _clean(self):
        # Drop rows with missing values
        self.attention_data.dropna(inplace=True)

    # train the attention model, using decision tree regressor as the model
    def _train(self):
        # split the data into features and target
        X = self.attention_data[self.features]
        y = self.attention_data[self.target]
        
        # perform train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # train the model
        self.model = DecisionTreeRegressor()
        self.model.fit(X_train, y_train)
        
        # train a decision tree regressor
        self.dt = DecisionTreeRegressor()
        self.dt.fit(X_train, y_train)
        
    @classmethod
    def get_instance(cls):
        """ Gets, and conditionally cleans and builds, the singleton instance of the AttentionModel.
        The model is used for prediction on attention data.
        
        Returns:
            AttentionModel: the singleton _instance of the AttentionModel, which contains data and methods for prediction.
        """        
        # check for instance, if it doesn't exist, create it
        if cls._instance is None:
            cls._instance = cls()
            cls._instance._clean()
            cls._instance._train()
        # return the instance, to be used for prediction
        return cls._instance

    def predict_score(self, subject, attention, solutions):
        """ Predict the score based on subject, attention, and solutions.

        Args:
            subject (int): The subject (0: Science, 1: Math, 2: History, 3: English)
            attention (str): The attention type ('focused' or 'divided')
            solutions (int): The number of solutions found (0-4)

        Returns:
           float : predicted score
        """
        # predict the score
        score_prediction = self.model.predict([[subject, attention, solutions]])
        return score_prediction
    
    def feature_weights(self):
        """Get the feature weights
        The weights represent the relative importance of each feature in the prediction model.

        Returns:
            dictionary: contains each feature as a key and its weight of importance as a value
        """
        # extract the feature importances from the decision tree model
        importances = self.dt.feature_importances_
        # return the feature importances as a dictionary, using dictionary comprehension
        return {feature: importance for feature, importance in zip(self.features, importances)} 

def initAttention():
    """ Initialize the Attention Model.
    This function is used to load the Attention Model into memory, and prepare it for prediction.
    """
    AttentionModel.get_instance()
    
def testAttention():
    """ Test the Attention Model
    Using the AttentionModel class, we can predict the score based on subject, attention, and solutions.
    Print output of this test contains method documentation, input data, and predicted score.
    """
     
    # setup data for prediction
    print(" Step 1: Define data for prediction: ")
    subject = 0
    attention = 'focused'
    solutions = 2
    print("\t", f"Subject: {subject}, Attention: {attention}, Solutions: {solutions}")
    print()

    # get an instance of the cleaned and trained Attention Model
    attention_model = AttentionModel.get_instance()
    print(" Step 2:", attention_model.get_instance.__doc__)
   
    # print the predicted score
    print(" Step 3: Predict the score based on subject, attention, and solutions:")
    predicted_score = attention_model.predict_score(subject, attention, solutions)
    print("\t Predicted Score:", predicted_score[0])
    print()
    
    # print the feature weights in the prediction model
    print(" Step 4:", attention_model.feature_weights.__doc__)
    importances = attention_model.feature_weights()
    for feature, importance in importances.items():
        print("\t\t", feature, f"{importance:.2%}") # importance of each feature, each key/value pair
        
if __name__ == "__main__":
    print(" Begin:", testAttention.__doc__)
    testAttention()

