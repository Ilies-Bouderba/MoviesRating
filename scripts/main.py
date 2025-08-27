from extract import extract
import transform
import load

def run_pipeline():
    # Step 1: Extract
    raw_data = extract()
    
    # Step 2: Transform
    cleaned_data = transform.clean_data(raw_data)
    
    # Step 3: Load
    load.analyze_jobs(cleaned_data)
    load.top_10_organizations(cleaned_data)
    print("🎉 Pipeline finished successfully!")
    
if __name__ == "__main__":
    run_pipeline()