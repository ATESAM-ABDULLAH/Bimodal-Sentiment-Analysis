#Download Dataset using wget: Use wget command to download the dataset.
wget -c 'https://web.eecs.umich.edu/~mihalcea/downloads/MELD.Raw.tar.gz'

#Extracting to the current directory: extract the contents to the current directory
tar -xzf MELD.Raw.tar.gz && rm MELD.Raw.tar.gz

#Move to extracted folder
cd /MELD.Raw

#Extract each sub directory.
tar -xzf dev.tar.gz && rm dev.tar.gz
tar -xzf test.tar.gz && rm test.tar.gz
tar -xzf train.tar.gz && rm train.tar.gz
