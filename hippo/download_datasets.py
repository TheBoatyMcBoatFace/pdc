# hippo/download_datasets.py
import requests
import yaml
import pandas as pd
from pathlib import Path
import logging

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Adjust these paths according to your project structure
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
CONFIG_DIR = BASE_DIR / "config"
DATASETS_YAML = CONFIG_DIR / 'datasets.yml'

def load_config():
    with open(DATASETS_YAML, 'r') as file:
        config = yaml.safe_load(file)
    return config['datasets']

def get_dataset_url(dataset_id):
    """Fetch the dataset URL from the API metadata."""
    url = f"https://data.cms.gov/provider-data/api/1/metastore/schemas/dataset/items/{dataset_id}"
    response = requests.get(url)
    if response.status_code == 200:
        dataset_info = response.json()
        if 'distribution' in dataset_info and dataset_info['distribution']:
            download_url = dataset_info['distribution'][0]['downloadURL']
            logging.info(f"Download URL for dataset {dataset_id}: {download_url}")
            return download_url
        else:
            logging.error(f"No download URL found for dataset {dataset_id}")
    else:
        logging.error(f"Failed to retrieve dataset info for {dataset_id}: {response.text}")
    return None

def download_data(download_url, dataset_id):
    """Download data from the provided URL."""
    response = requests.get(download_url)
    if response.status_code == 200:
        try:
            df = pd.read_csv(download_url)
            return df
        except Exception as e:
            logging.error(f"Error loading data into DataFrame for dataset {dataset_id}: {str(e)}")
            return None
    else:
        logging.error("Failed to download data: HTTP {response.status_code} - {response.text[:200]}")
        return None

def save_data(df, path):
    # Ensure the directory exists
    path.parent.mkdir(parents=True, exist_ok=True)
    # Save data as CSV
    df.to_csv(path, index=False)
    logging.info(f"Data saved to {path}")

def main():
    datasets = load_config()
    for topic, entries in datasets.items():
        for entry in entries:
            dataset_id = entry['id']
            logging.info(f"Processing dataset ID: {dataset_id}")
            download_url = get_dataset_url(dataset_id)
            if download_url:
                df = download_data(download_url, dataset_id)
                if df is not None:
                    file_path = DATA_DIR / topic / f"{dataset_id}.csv"
                    save_data(df, file_path)
            else:
                logging.error(f"Could not process dataset ID: {dataset_id}")

if __name__ == "__main__":
    main()
