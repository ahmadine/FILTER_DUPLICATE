import os
import pandas as pd

# Directory where your CSV files are located
directory = 'C:/Users/DESTINED/Downloads/2022_2023 RAIN RESULT/SPLITTED/MR_SITA'

# Get a list of all files in the directory
files = os.listdir(directory)

# Loop through each file in the directory
for file in files:
    if file.endswith('.csv'):
        # Load the CSV file into a pandas DataFrame
        df = pd.read_csv(os.path.join(directory, file), delimiter=',')

        # Convert 'Score' column to numeric for proper sorting
        df['Score'] = pd.to_numeric(df['Score'], errors='coerce')

        # Check and upgrade scores below 10 to 10
        df.loc[df['Score'] < 10, 'Score'] = 10

        # Sort DataFrame by 'Username' and 'Score' in descending order
        df = df.sort_values(by=['Username', 'Score'], ascending=[True, False])

        # Drop duplicate 'Username' keeping the first occurrence (highest score)
        df_unique = df.drop_duplicates(subset='Username', keep='first')

        # Save the modified DataFrame to the original CSV file
        df_unique.to_csv(os.path.join(directory, file), index=False)

print("Processing completed!")
