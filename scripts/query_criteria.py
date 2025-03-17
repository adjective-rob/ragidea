import pandas as pd

# Load CSV
file_path = "data/business_idea_criteria.csv"
df = pd.read_csv(file_path)

def query_criteria(keyword):
    """Searches for relevant business criteria based on a keyword."""
    results = df[df["Criteria"].str.contains(keyword, case=False, na=False)]
    if results.empty:
        print("No matching criteria found.")
    else:
        print(results)

# Example: Query for scalability-related criteria
query_criteria("scalability")
