import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
#for Stemming and Lemmatization
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string
# Download NLTK resources if not already present
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
# Function for Tokenization and Preprocessing
def tokenize_and_preprocess(text):
# Tokenize the text
      tokens = word_tokenize(text)
      
      # Remove stop words and punctuation
      stop_words = set(stopwords.words('english'))
      punctuation = set(string.punctuation)
      
      filtered_tokens = [word.lower() for word in tokens if (word.isalpha() and word.lower() not in stop_words and word not in punctuation)]
      
      return filtered_tokens
# Read the external file
file_path = 'SBA927.txt'
with open(file_path, 'r', encoding='utf-8') as file:
      # Read the entire content of the file
      dataset = file.read().splitlines()
# Tokenization and Preprocessing for the entire dataset
processed_dataset = [tokenize_and_preprocess(text) for text in dataset]
# Display the results
for i, text_tokens in enumerate(processed_dataset):
      print(f"Original Text {i + 1}: {dataset[i]}")
      print(f"Processed Tokens {i + 1}: {text_tokens}")
      print("\n")

#STEMMING AND LEMMATIZATION
# Define a function for stemming and lemmatization
def stem_and_lemmatize(tokens):
      # Initialize stemming and lemmatization tools
      stemmer = PorterStemmer()
      lemmatizer = WordNetLemmatizer()
      # Apply stemming
      stemmed_tokens = [stemmer.stem(token) for token in tokens]
      # Apply lemmatization
      lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
      return stemmed_tokens, lemmatized_tokens
# Assume 'processed_dataset' contains the preprocessed text data
# Apply stemming and lemmatization to the entire dataset
stemmed_and_lemmatized_dataset = [stem_and_lemmatize(tokens) for tokens in processed_dataset]
# Display the results
for i, (stemmed_tokens, lemmatized_tokens) in enumerate(stemmed_and_lemmatized_dataset):
      print(f"Original Tokens {i + 1}: {processed_dataset[i]}")
      print(f"Stemmed Tokens {i + 1}: {stemmed_tokens}")
      print(f"Lemmatized Tokens {i + 1}: {lemmatized_tokens}")
      print("\n")
      # Assume 'processed_dataset' contains the preprocessed text data
# Define a function for POS tagging
def pos_tagging(text):
    # Tokenize and process the text
    sentences = sent_tokenize(text)
    pos_tags = []
    # Process each sentence
    for sentence in sentences:
        words = word_tokenize(sentence)
        pos_tags.extend(pos_tag(words))
    return pos_tags
# Apply POS tagging to the entire dataset
pos_tags_dataset = [pos_tagging(text) for text in dataset]
# Display the results
for i, pos_tags in enumerate(pos_tags_dataset):
    print(f"POS Tags in Text {i + 1}: {pos_tags}")
    print("\n")
      
     