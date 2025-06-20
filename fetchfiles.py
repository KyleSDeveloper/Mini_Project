import urllib.request
import os

# Create a directory for the data
os.makedirs("data/adult", exist_ok=True)

# Download training and test files
urllib.request.urlretrieve(
    "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data",
    "data/adult/adult.data"
)
urllib.request.urlretrieve(
    "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test",
    "data/adult/adult.test"
    
)
print("Files downloaded.")