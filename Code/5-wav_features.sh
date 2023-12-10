#!/bin/bash

# Function to extract features and append to the CSV file
extract_features() {
    # Declare the function's parameters
    folder="$1"
    output_csv="$2"

    # Iterate through all the WAV files in the specified folder
    for file in wav/"$folder"/*; do
        # Extract 'dia#_utt#' from the full file name
        filename=$(basename "$file" | sed 's/dia\([0-9]\+\)_utt\([0-9]\+\)\.wav/\1_\2/')

        # Extract the IS13_compare features using SMILExtract and append them to the CSV file
        ../opensmile/bin/SMILExtract -C ../opensmile/config/is09-13/IS13_ComParE.conf \
        -I "$file" -instname "$filename" -appendcsv 1 -csvoutput "$output_csv" 
    done
}

# Change to the MELD.Raw directory
cd MELD.Raw

# Extract the features from the test WAV files and append them to the 'test_features.csv' file
extract_features "test_wav" "test_features.csv"

# Extract the features from the test WAV files and append them to the 'test_features.csv' file
extract_features "dev_wav" "dev_features.csv"

# Extract the features from the test WAV files and append them to the 'test_features.csv' file
extract_features "train_wav" "train_features.csv"