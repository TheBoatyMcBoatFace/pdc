# CMS PDC Data Archive

Github repository dedicated to the automated daily retrieval of all CMS Provider Data Catalog (PDC) datasets, accompanied by storage handling through DoltHub.

Visit the project's Dolt repo: [CMS PDC on DoltHub](https://www.dolthub.com/repositories/cms-pdc/dkany)

**License:** AGPL-3.0

## Overview

This repository performs daily GET requests to fetch datasets from the CMS Provider Data Catalog (PDC) and stores them systematically. The main objective is to maintain an up-to-date and accessible repository of CMS datasets that are crucial for healthcare analytics and public health informatics.

## CMS Provider Data Themes

The CMS PDC covers various healthcare-related themes. Below are some of the key data themes available:

- [Dialysis Facilities (DF)](https://data.cms.gov/provider-data/search?theme=Dialysis%20facilities)
- [Doctors and Clinicians](https://data.cms.gov/provider-data/search?theme=Doctors%20and%20clinicians)
- [Home Health Services](https://data.cms.gov/provider-data/search?theme=Home%20health%20services)
- [Hospice Care](https://data.cms.gov/provider-data/search?theme=Hospice%20care)
- [Hospitals](https://data.cms.gov/provider-data/search?theme=Hospitals)
- [Inpatient Rehabilitation Facilities](https://data.cms.gov/provider-data/search?theme=Inpatient%20rehabilitation%20facilities)
- [Long-term Care Hospitals](https://data.cms.gov/provider-data/search?theme=Long-term%20care%20hospitals)
- [Nursing Homes Including Rehab Services](https://data.cms.gov/provider-data/search?theme=Nursing%20homes%20including%20rehab%20services)
- [Physician Office Visit Costs](https://data.cms.gov/provider-data/search?theme=Physician%20office%20visit%20costs)
- [Supplier Directory (SD)](https://data.cms.gov/provider-data/search?theme=Supplier%20directory)

## How It Works

The project utilizes Python scripts scheduled via crontab (or your custom scheduler) to pull data from the CMS API using specific dataset identifiers located in `config/datasets.yml`. The datasets are downloaded in CSV format and stored in a directory structure reflecting their respective themes, ensuring easy navigation and access.

### Structure

- **download_datasets.py**: Main Python script that orchestrates the downloading process.
- **config/datasets.yml**: YAML file containing dataset identifiers and themes.
- **data/**: Directory where downloaded datasets are stored by theme and dataset ID.

## Prerequisites

To run the project scripts or contribute, you need:

- Python 3.x
- Dependencies from `requirements.txt`

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-github>/cms-pdc.git
   cd cms-pdc
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the scheduler for daily runs or execute the script manually:
   ```bash
   python3 hippo/download_datasets.py
   ```

## Contributions

Contributions to enhance the functionality, improve data extraction, or refine storage mechanisms are welcome! Please fork the repository, make your changes, and submit a pull request.

## Data Usage

Please ensure that the use of data fetched through CMS PDC is compliant with the data use agreements and legal stipulations provided on the [CMS Data Website](https://data.cms.gov/).

