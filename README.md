# Monster.com Job Postings Analysis

This project analyzes job postings data from Monster.com, focusing on data cleaning, exploration, and insights into job trends by location, type, and sector.

## Project Structure

```
.
├── DATA_CATALOG.md
├── data/
│   ├── cleaned/
│   │   └── cleaned_monster_com_job_sample.csv
│   ├── final/
│   │   ├── location_with_the_most_jobs.csv
│   │   ├── most_job_posting_type.csv
│   │   └── most_sector_jobs.csv
│   └── raw/
│       └── monster_com-job_sample.csv
└── notebooks/
    ├── 01_python_basics.ipynb
    ├── 02_cleaning_and_inspectation.ipynb
    └── 02_final_analyst.ipynb
```

## Getting Started

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Install dependencies:**
   - Open the notebooks in [notebooks/](notebooks/) and install any required Python packages (e.g., pandas, numpy, matplotlib, seaborn).

3. **Explore the data:**
   - See [DATA_CATALOG.md](DATA_CATALOG.md) for a detailed description of each dataset.
   - Start with [`notebooks/01_python_basics.ipynb`](notebooks/01_python_basics.ipynb) for basic exploration.
   - Use [`notebooks/02_cleaning_and_inspectation.ipynb`](notebooks/02_cleaning_and_inspectation.ipynb) for data cleaning steps.
   - Analyze results in [`notebooks/02_final_analyst.ipynb`](notebooks/02_final_analyst.ipynb).

## Data Sources

- Raw data: [`data/raw/monster_com-job_sample.csv`](data/raw/monster_com-job_sample.csv) (originally from Kaggle)
- Cleaned and processed datasets: See [DATA_CATALOG.md](DATA_CATALOG.md)

## Results

- Aggregated results are available in [`data/final/`](data/final/):
  - [`location_with_the_most_jobs.csv`](data/final/location_with_the_most_jobs.csv)
  - [`most_job_posting_type.csv`](data/final/most_job_posting_type.csv)
  - [`most_sector_jobs.csv`](data/final/most_sector_jobs.csv)

## License

This project is for educational and research purposes. Please refer to the original data source for licensing details.

---

**See [DATA_CATALOG.md](DATA_CATALOG.md) for