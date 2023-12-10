import pandas as pd
import os


# Load the raw CSV files into separate DataFrames
def load_csv_data(files, sep):
    dataframes = []
    for file in files:
        df = pd.read_csv(file, sep=sep)
        dataframes.append(df)
    return dataframes


# Function to count the number of files in a directory that start with a specific prefix
def count_files_starting_with(folder_path, prefix):
    count = 0

    # Iterate through files in the directory
    for file in os.listdir(folder_path):
        if file.startswith(prefix):
            count += 1

    return count


# Function to check the file distribution in a specific directory
def check_file_distribution(path):
    # Iterate through each dataframe and update counts
    finals = count_files_starting_with(path, "final")
    raws = count_files_starting_with(path, "dia")
    extras = count_files_starting_with(path, "._")

    # Print the file distribution
    print(f"{path}: Raws= {raws}, Finals= {finals}, Extras= {extras}")


# Move to Data directory
base_path = "MELD.Raw/"
os.chdir(base_path)

# CSV files with text data
text_files = ["dev.csv", "test.csv", "train.csv"]

# Load CSV data for each text data file
text_dfs = load_csv_data(text_files, sep=",")

for i, df in enumerate(text_dfs):
    print(f"-----NAME: {text_files[i]}-------")
    print(df.columns)
    print(f"Rows = {df.shape[0]}, Cols = {df.shape[1]}\n")


# Check the audio file distribution for each dataset
print("------------Audio files distribution----------")
check_file_distribution("wav/dev_wav")
check_file_distribution("wav/test_wav")
check_file_distribution("wav/train_wav")

# CSV files with feature data
feature_files = ["dev_features.csv", "test_features.csv", "train_features.csv"]

# Load CSV data for each feature file
feature_dfs = load_csv_data(feature_files, sep=",")

for i, df in enumerate(feature_dfs):
    print(f"\n-----NAME: {feature_files[i]}-------")
    print(f"Rows = {df.shape[0]}, Cols = {df.shape[1]}")
