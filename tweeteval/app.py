import json
from transformers import AutoModelForSequenceClassification, AutoTokenizer, AutoConfig
# Load the model and tokenizer once (for cold start optimization)
MODEL_PATH = "./model"  # Ensure this is the path where you've saved your model in the Docker container
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
config = AutoConfig.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH, config=config)
model.eval()  # Set the model to evaluation mode
from scipy.special import softmax
import numpy as np

def lambda_handler(event, context):
    """
    AWS Lambda function handler for sentiment.
    """
    labels = ['negative', 'neutral', 'positive']
    # Extract text from the incoming event
    text = event['body']['text']
    # Tokenize the text and convert to tensor
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    ranking = np.argsort(scores)
    ranking = ranking[::-1]
    labels_scored = {}
    for i in range(scores.shape[0]):
        l = labels[ranking[i]]
        s = scores[ranking[i]]
        labels_scored[l] = s
    # Return the response
    response = {
        "statusCode": 200,
        "body": str(labels_scored)
    }
    return response
