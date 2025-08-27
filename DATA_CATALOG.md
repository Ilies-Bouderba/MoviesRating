# Data Catalog

This document describes the datasets used in this project, including their sources, structure, and purpose.

---

## Table of Contents

- [1. Raw Data](#1-raw-data)
- [2. Cleaned Data](#2-cleaned-data)
- [3. Final Data](#3-final-data)
- [4. Notebooks](#4-notebooks)

---

## 1. Raw Data

### [`data/raw/monster_com-job_sample.csv`](data/raw/monster_com-job_sample.csv)

- **Description:** Original job postings data from Monster.com posted in kaggle.
- **Format:** CSV
- **Columns:**  
  - Country  
  - Country Code  
  - ... (other metadata fields)  
  - Job Description  
  - Job Title  
  - Job Type  
  - Location  
  - ...  
  - Job ID
- **Purpose:** Serves as the primary source for all downstream data cleaning and analysis.

---

## 2. Cleaned Data

### [`data/cleaned/cleaned_monster_com_job_sample.csv`](data/cleaned/cleaned_monster_com_job_sample.csv)

- **Description:** Cleaned and preprocessed version of the raw Monster.com job postings.
- **Format:** CSV
- **Columns:**  
  - Uniq ID  
  - Job Title  
  - Job Description  
  - Job Type  
  - Salary  
  - City  
  - State  
  - Date Posted  
  - ... (additional cleaned fields)
- **Purpose:** Used for analysis and feature extraction in notebooks.

---

## 3. Final Data

### [`data/final/location_with_the_most_jobs.csv`](data/final/location_with_the_most_jobs.csv)

- **Description:** Aggregated data showing locations with the most job postings.
- **Format:** CSV
- **Columns:**  
  - Location  
  - Job Count

### [`data/final/most_job_posting_type.csv`](data/final/most_job_posting_type.csv)

- **Description:** Summary of the most common job posting types.
- **Format:** CSV
- **Columns:**  
  - Job Type  
  - Count

### [`data/final/most_sector_jobs.csv`](data/final/most_sector_jobs.csv)

- **Description:** Aggregated data of job postings by sector.
- **Format:** CSV
- **Columns:**  
  - Sector  
  - Job Count

---

## 4. Notebooks

### [`notebooks/01_python_basics.ipynb`](notebooks/01_python_basics.ipynb)

- **Description:** Introduction to Python basics, used for initial exploration and familiarization.

### [`notebooks/02_cleaning_and_inspectation.ipynb`](notebooks/02_cleaning_and_inspectation.ipynb)

- **Description:** Data cleaning and inspection steps, including transformation from raw to cleaned data.

### [`notebooks/02_final_analyst.ipynb`](notebooks/02_final_analyst.ipynb)

- **Description:** Final analysis and visualization notebook, using cleaned and final datasets.

---

## Notes

- All data files are in CSV format and use UTF-8 encoding.
- Sensitive or personal information has been removed or anonymized