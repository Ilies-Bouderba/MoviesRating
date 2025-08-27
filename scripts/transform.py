import pandas as pd
from config import CLEANED_DATA_PATH


def clean_data(market: pd.DataFrame) -> pd.DataFrame:
    print("Cleaning data...")
    market['date_added'] = pd.to_datetime(market['date_added'], errors='coerce')
    market['salary'] = pd.to_numeric(market['salary'], errors='coerce')
    
    market['date_added'] = market['date_added'].fillna(pd.Timestamp('2023-01-01'))
    market['organization'] = market['organization'].fillna('Unknown')
    market['salary'] = market['salary'].fillna(0)
    market['sector'] = market['sector'].fillna('Unknown')
    market['location'] = market['location'].str.replace(r'\s+\d{5}(-\d{4})?$', '', regex=True)
    market['location'] = market['location'].str.strip()
    market['city'] = market['location'].str.extract(r'^([^,]+)')
    market['state'] = market['location'].str.extract(r',\s*([A-Z]{2})')
    market['state'] = market['state'].fillna('Unknown')
    market['has_expired'] = market['has_expired'].map({'Yes': True, 'No': False})
    market['job_type'] = market['job_type'].apply(standardize_job_type)
    
    
    market['city'] = market['location'].str.extract(r'^([^,]+)')
    market['state'] = market['location'].str.extract(r',\s*([A-Z]{2})')
    market['job_title'] = market['job_title'].str.strip()
    dirty_titles = market['job_title'].str.contains('>|<|=|var', regex=True, case=False, na=False)
    market.loc[dirty_titles, 'job_title'] = market.loc[dirty_titles, 'job_title'].str.split('|').str[0].str.split('{').str[0].str.strip()
    market['organization'] = market['organization'].str.strip()
    
    market.drop(columns=['location', 'job_board', 'country', 'country_code'])
    
    market = market[["uniq_id", "job_title", "job_description", "job_type", "sector", "organization", "city", "state", "date_added", "salary", "has_expired"]]
    
    market.to_csv("../data/cleaned/CLEANED_DATA_PATH.csv", index=False)
    return market

def standardize_job_type(job_type):
    if pd.isna(job_type):
        return 'Unknown'
    job_type = job_type.lower()
    if 'full' in job_type:
        return 'Full-time'
    elif 'part' in job_type:
        return 'Part-time'
    elif 'contract' in job_type:
        return 'Contract'
    elif 'intern' in job_type:
        return 'Internship'
    elif 'temp' in job_type or 'temporary' in job_type:
        return 'Temporary'
    else:
        return 'Other'