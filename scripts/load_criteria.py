
---

### **3️⃣ Python Script: `load_criteria.py`**  
This script **loads the CSV into a Pandas DataFrame** for querying.

```python
import pandas as pd

# Load CSV
file_path = "data/business_idea_criteria.csv"
df = pd.read_csv(file_path)

# Display first few rows
print(df.head())
