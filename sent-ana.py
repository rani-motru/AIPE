# Importing TextBlob library
from textblob import TextBlob

#TO-DO-1
# Sample text for checking TextBlob installation
sample_text = "TextBlob is successfully installed and ready to use!"

# Print confirmation message
print(f"TextBlob library successfully imported. Sample text: {sample_text}")

#from textblob import TextBlob
#TO-DO-2
# Sample text for sentiment analysis
sample_text = "I absolutely love this product! The quality is excellent and it arrived on time."

# Create a TextBlob object
blob = TextBlob(sample_text)

# Perform sentiment analysis
sentiment = blob.sentiment

# Print the original text and sentiment analysis results
print("Original Text:", sample_text)
print("Sentiment Analysis Result:")
print("Polarity:", sentiment.polarity)  # Range from -1 (negative) to 1 (positive)
print("Subjectivity:", sentiment.subjectivity)  # Range from 0 (objective) to 1 (subjective)

#from textblob import TextBlob
#TO-DO-3
# Sample customer feedback comments
feedback_comments = [
    "The service was fantastic and the staff was very helpful.",
    "I am unhappy with the product quality and delivery was delayed.",
    "The product is okay, but it could be improved.",
    "Amazing experience! I am very satisfied with my purchase."
]

# Function to analyze sentiment of each comment
def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

# Analyze and print sentiment for each feedback comment
for comment in feedback_comments:
    sentiment = analyze_sentiment(comment)
    print(f"Feedback: {comment}")
    print(f"Sentiment Polarity: {sentiment}")
    print("-----")