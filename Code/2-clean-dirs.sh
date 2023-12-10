# Navigate to the test directory containing some garbage files and leftover mac build files
cd MELD.Raw/raw/test_raw

# Remove all files and directories that start with 'final'
# These files are larger multi dialogue files
rm -r final* 

# Remove all files that start with a '.'
# These files are created by MacOS
rm ._* 