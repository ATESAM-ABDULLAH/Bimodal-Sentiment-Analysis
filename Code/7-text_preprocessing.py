"""Import Packages + Move to Data directory"""

import os  # File handling
import pandas as pd  # Reading Csv
import numpy as np  # np.pad for padding our embedings
import pickle  # For saving data

import re  # regex
from nltk.tokenize import word_tokenize  # Tokenize the sentence
import nltk  # NLP library

nltk.download("punkt")

from gensim.models import KeyedVectors  # Read a glove file as a dictionary

# Connect to drive
from google.colab import drive

drive.mount("/content/drive")

# Move to data directory
os.chdir("drive/MyDrive/BSA-data")

"""# Load data"""

sep = ","

print("Max sentence lengths\n")

# Read text data from csv as dataframe
test_df = pd.read_csv("test.csv", sep=sep)
max_test_len = test_df["Utterance"].str.len().max()  # max length of sentence in data
print(f"Test: {max_test_len} words")

dev_df = pd.read_csv("dev.csv", sep=sep)
max_dev_len = dev_df["Utterance"].str.len().max()
print(f"Dev: {max_dev_len} words")

train_df = pd.read_csv("train.csv", sep=sep)
max_train_len = train_df["Utterance"].str.len().max()
print(f"Train: {max_train_len} words")

"""## Download Glove Embeddings
Run only once
"""

# # Download Glove embeddings: Common Crawl (840B tokens, 2.2M vocab, cased, 300d vectors, 2.03 GB download)
# !wget https://huggingface.co/stanfordnlp/glove/resolve/main/glove.840B.300d.zip

# # Unzip file
# !unzip glove.840B.300d.zip

# # Delete the zip
# !rm glove.840B.300d.zip

# Choose your GloVe file path
glove_model_path = "glove.840B.300d.txt"  # Input file

# Vocab length -> pad all to this size
vocab_length = 350

"""## Helper Functions"""


# Function to take a string and return clean list of words
def clean_text(text):
    """
    Lowercase, remove punctuation, stop words, and extra whitespace.
    """
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)  # Remove spaces
    tokens = word_tokenize(text)  # Tokenize sentence -> split into small parts
    return tokens  # return list


# Function to find embeddings and process everything
def preprocess_and_embed_data(df, model, column="Utterance", max_length=350):
    """Preprocesses text data, finds word embeddings, and pads sequences.

    Args:
        df (pd.DataFrame): DataFrame containing the "Utterances" column.
        model (KeyedVectors): Loaded word embedding model.
        max_length (int, optional): Maximum length for padding. Defaults to 50.

    Returns:
        list: List of padded word embedding sequences.
    """

    processed_data = []
    for utterance in df[column]:
        # Preprocess text
        words = clean_text(utterance)

        # Find word embeddings if not return Null filled list
        word_embeddings = [model[word] for word in words if word in model] or (
            [[0] * 300]
        )

        # Pad or truncate sequences
        padded_embeddings = np.pad(
            np.array(word_embeddings),
            [(0, max_length - len(word_embeddings)), (0, 0)],
            mode="constant",
            constant_values=0,
        )
        processed_data.append(padded_embeddings)

    return processed_data


"""# Read The GloVe file and save Model
Run only once
"""

# # Read the glove file we downloaded -> takes several minutes
#  glove_model = KeyedVectors.load_word2vec_format(glove_model_path, binary=False, no_header=True)
# print(f"Loaded GloVe model with {len(glove_model)} words")

# # Save the model for faster usage
# glove_model.save("glove_model.bin")

# # Remove the glove file
# !rm glove.840B.300d.txt

"""## Read saved model"""

# Read the saved Model file -> takes 1-2 mins max
glove_model = KeyedVectors.load("glove_model.bin")
print(f"Loaded GloVe model with {len(glove_model)} words")

"""# Find the Embeddings
Hierarchy: sentence =  350 words x 300 embeddings
- clean_data = all sentences
- clean_data -> sentence -> word -> list[float32]
"""

clean_data = preprocess_and_embed_data(dev_df, glove_model)
dev_df["Word_embeddings"] = clean_data
pickle.dump(dev_df, open("dev_df_processed.pkl", "wb"))  # save df as pickle file
del clean_data

clean_data = preprocess_and_embed_data(test_df, glove_model)
test_df["Word_embeddings"] = clean_data
pickle.dump(test_df, open("test_df_processed.pkl", "wb"))  # save df as pickle file
del clean_data

clean_data = preprocess_and_embed_data(train_df, glove_model)
train_df["Word_embeddings"] = clean_data
pickle.dump(train_df, open("train_df_processed.pkl", "wb"))  # save df as pickle file
del clean_data
