# hippo/utils/make_dataset_config.py
import requests
import yaml
from collections import defaultdict
import re
from pathlib import Path

# Folder path setup - adjust path calculation
BASE_DIR = Path(__file__).resolve().parents[1]
CONFIG_DIR = BASE_DIR / 'config'
DATASETS_YAML = CONFIG_DIR / 'datasets.yml'

def fetch_data():
    url = "https://data.cms.gov/provider-data/api/1/metastore/schemas/dataset/items?show-reference-ids=false"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data")
        return []

def snake_case(name):
    name = re.sub(r"[\s/]+", '_', name)
    name = re.sub(r"[^\w\s]", '', name).lower()
    return name[:64] if len(name) > 64 else name

def determine_schema(theme):
    schema_map = {
        "Physician office visit costs": "PPL",
        "Dialysis facilities": "DF",
        "Doctors and clinicians": "DAC",
        "Home health services": "HHS",
        "Hospice care": "HC",
        "Hospitals": "HOS",
        "Inpatient rehabilitation facilities": "IRF",
        "Long-term care hospitals": "LTCH",
        "Nursing homes including rehab services": "NH",
        "Supplier directory": "SUP"
    }
    return schema_map.get(theme, "GEN")

def generate_yaml(data):
    dataset_dict = defaultdict(list)
    for item in data:
        dataset_id = item.get('identifier')
        title = item.get('title', '')
        theme = item.get('theme', [{}])[0].get('data', 'GEN')
        schema = determine_schema(theme)
        table_name = snake_case(title)

        dataset_dict[schema].append({
            'id': dataset_id,
           # 'table': table_name,
            'title': f'"{title}"'  # Enclose title in double quotes
        })

    yaml_data = {'datasets': dict(dataset_dict)}
    # Enhanced YAML formatting with custom dumper for better display
    class CustomDumper(yaml.SafeDumper):
        def increase_indent(self, flow=False, indentless=False):
            return super(CustomDumper, self).increase_indent(flow, False)

    with open(DATASETS_YAML, 'w') as file:
        yaml.dump(yaml_data, file, Dumper=CustomDumper, default_flow_style=False, sort_keys=False, allow_unicode=True)

def main():
    data = fetch_data()
    generate_yaml(data)

if __name__ == "__main__":
    main()
