import os
import pandas as pd

directory = 'C:/Users/DESTINED/Downloads/2022_2023 RAIN RESULT/DONE'

files = os.listdir(directory)

for file in files:
    if file.endswith('.csv'):
        file_path = os.path.join(directory, file)
        
        # Load the CSV file into a pandas DataFrame
        df = pd.read_csv(file_path, delimiter=',')

        # Check if 'Unnamed: 9' column exists in the DataFrame
        if 'Unnamed: 9' in df.columns:
            # Drop the 'Unnamed: 9' column
            df = df.drop(columns=['Unnamed: 9'])

            # Save the modified DataFrame to the same CSV file
            df.to_csv(file_path, index=False)

print("Column removal completed!")
