import pandas as pd
import json
import sqlalchemy

# Load extracted data
with open("transaction_data.json", "r") as file:
    transaction_data = json.load(file)

# Convert to pandas DataFrame
df = pd.DataFrame(transaction_data)

# Process data (example: convert timestamps, handle missing values)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df.fillna(0, inplace=True)

# Define database connection
database_url = "postgresql://username:password@localhost:5432/educhain"
engine = sqlalchemy.create_engine(database_url)

# Store processed data in the database
df.to_sql('transactions', engine, if_exists='replace', index=False)

print("Data processing and storage complete.")
