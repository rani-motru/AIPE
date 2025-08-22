from transformers import pipeline

#classifier = pipeline("sentiment-analysis")

classifier = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

result = classifier("The food is really great")
print(result)