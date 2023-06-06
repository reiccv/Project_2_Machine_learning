import datetime
import json
import boto3
import numpy as np
import tensorflow as tf

def age_verification(intent_request):
    slots = intent_request['currentIntent']['slots']
    user_age = slots['Age']
    
    #format "YYYY-MM-DD"
    birth_date = datetime.datetime.strptime(user_age, '%Y-%m-%d').date()
    today = datetime.date.today()
    
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    
    response = {
        'dialogAction': {
            'fulfillmentState': 'Fulfilled',
            'type': 'Close',
            'message': {
                'contentType': 'PlainText',
                'content': ''
            }
        }
    }
    
    if age < 21:
        response['dialogAction']['message']['content'] = 'Sorry, you must be at least 21 years old.'
    else:
        response['dialogAction']['message']['content'] = 'Great! You meet the age requirement.'
    
    return response


# Load machine learning model
model = tf.keras.models.load_model('Project_2_Machine_learning/nba.ipynb')

def lambda_handler(event, context):
    # Extract the user input from the Lex event
    user_input = event['inputTranscript']
    
    # Preprocess the input if needed
    
    
    # Perform prediction using your machine learning model
    prediction = model.predict(np.array([user_input]))  # Assuming your model expects input as a numpy array
    
    # Postprocess the prediction if needed
    # ...
    
    # Format the prediction response
    response = {
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': 'Fulfilled',
            'message': {
                'contentType': 'PlainText',
                'content': f"The prediction is {prediction}"
            }
        }
    }
    
    # Return the response
    return response
