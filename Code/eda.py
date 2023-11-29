import pandas as pd
import os

base = "MELD.Raw/"
dev_df = pd.read_csv(base+"dev.csv")
test_df = pd.read_csv(base+"test.csv")
train_df = pd.read_csv(base+"train.csv")




def count_files_starting_with(folder_path, prefix):
    count = 0

    # Iterate through files in the directory
    for file in os.listdir(folder_path):
        if file.startswith(prefix):
            count += 1

    return count

# Replace 'folder_path' with the path to your folder and 'specific_prefix_' with the specific prefix you're looking for
test_path = 'MELD.Raw/test_raw/'

finals = count_files_starting_with(test_path, 'final')
raws = count_files_starting_with(test_path, 'dia')
print("Shape test:",test_df.shape)
print(f"Finals in test:{finals}, RAws: {raws}")

train_path = 'MELD.Raw/train_raw/'

finals = count_files_starting_with(train_path, 'final')
raws = count_files_starting_with(train_path, 'dia')

print("Shape train:",train_df.shape)
print(f"Finals in train:{finals}, RAws: {raws}")

dev_path = 'MELD.Raw/dev_raw/'

finals = count_files_starting_with(dev_path, 'final')
raws = count_files_starting_with(dev_path, 'dia')

print("Shape dev:",dev_df.shape)
print(f"Finals in dev:{finals}, RAws: {raws}")

