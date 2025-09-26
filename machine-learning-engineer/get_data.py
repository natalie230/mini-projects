import kaggle
import zipfile
import os

kaggle.api.competition_download_files('playground-series-s5e8', path='data/raw')

zip_path = "data/raw/playground-series-s5e8.zip"
extract_path = "data/raw/"

# Create folder if it doesn't exist
os.makedirs(extract_path, exist_ok=True)

# Extract all files
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print("Dataset extracted to:", extract_path)
