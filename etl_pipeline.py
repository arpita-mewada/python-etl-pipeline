```python
import pandas as pd
import json

def extract_csv(path):
    return pd.read_csv(path)

def extract_json(path):
    with open(path, "r") as f:
        data = json.load(f)
    return pd.DataFrame(data)

def transform(df):
    df = df.drop_duplicates()
    df = df.fillna(0)
    return df

def load(df, output_path):
    df.to_csv(output_path, index=False)

def run_pipeline():
    try:
        csv_df = extract_csv("data/raw/sample.csv")
        json_df = extract_json("data/raw/sample.json")

        combined_df = pd.concat([csv_df, json_df], ignore_index=True)
        transformed_df = transform(combined_df)

        load(transformed_df, "data/processed/final_data.csv")
        print("ETL pipeline executed successfully")

    except Exception as e:
        print(f"Pipeline failed: {e}")

if __name__ == "__main__":
    run_pipeline()
    
