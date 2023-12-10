# Downloading Dataset using wget: Utilize the wget command to download the dataset.
wget -c 'https://web.eecs.umich.edu/~mihalcea/downloads/MELD.Raw.tar.gz'

# Extracting to the current directory: Unzip the contents of the downloaded file to the current directory.
tar -xzf MELD.Raw.tar.gz && rm MELD.Raw.tar.gz

# Move to extracted folder: Change the current directory to the extracted folder.
cd /MELD.Raw

# Extract each sub directory: Unzip each of the subdirectories (dev, test, train) within the extracted folder.
tar -xzf dev.tar.gz && rm dev.tar.gz
tar -xzf test.tar.gz && rm test.tar.gz
tar -xzf train.tar.gz && rm train.tar.gz
