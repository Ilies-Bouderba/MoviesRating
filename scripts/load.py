import pandas as pd
from config import SECTOR_JOB_PATH, TOP_ORGS_PATH, ANALYZE_JOB_PATH

def analyze_jobs(df: pd.DataFrame) -> pd.DataFrame:
    print("🔹 Analyzing jobs by sector...")
    sector_counts = df['sector'].value_counts().head(10)
    sector_counts.columns = ['sector', 'job_count']
    print("✅ Analysis complete")
    sector_counts.to_csv(SECTOR_JOB_PATH, index=False)
    print(f"📂 Saved analysis → {SECTOR_JOB_PATH}")
    return sector_counts

def top_10_organizations(df: pd.DataFrame) -> pd.DataFrame:
    print("🔹 Identifying top 10 organizations...")
    top_orgs = df['organization'].value_counts().head(10)
    top_orgs.columns = ['organization', 'job_count']
    print("✅ Top 10 organizations identified")
    top_orgs.to_csv(TOP_ORGS_PATH, index=False)
    print(f"📂 Saved top organizations → {TOP_ORGS_PATH}")
    return top_orgs