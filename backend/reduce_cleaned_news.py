import pandas as pd

# Load the CSV
input_path = 'backend/cleaned_news.csv'
output_path = 'backend/cleaned_news_sampled.csv'

# 1. Keep only the necessary columns
df = pd.read_csv(input_path)
columns_to_keep = ['title', 'text', 'label']
df = df[columns_to_keep]

# 2. Remove duplicate rows
df = df.drop_duplicates()

# 3. Randomly sample 10% of the data
df_sampled = df.sample(frac=0.1, random_state=42)

# 4. Save the result
df_sampled.to_csv(output_path, index=False)

print(f"Reduced CSV saved as {output_path}") 