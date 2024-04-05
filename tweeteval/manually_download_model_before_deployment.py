from transformers import AutoModelForSequenceClassification, AutoTokenizer

MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment"
# Download and save the pre-trained model. If you were to fine-tune the model you'd save files as well
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
model.save_pretrained("./model")
# Download and save the tokenizer locally
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
tokenizer.save_pretrained("./model")
