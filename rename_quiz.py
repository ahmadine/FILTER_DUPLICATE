import os
import pandas as pd

# Directory where your CSV files are located
import os
import pandas as pd

# Directory where your CSV files are located
directory = 'C:/Users/DESTINED/Downloads/2022_2023 RAIN RESULT/DONE'

# Get a list of all files in the directory
files = os.listdir(directory)

# Loop through each file in the directory
for file in files:
    if file.endswith('.csv'):
        # Load the CSV file into a pandas DataFrame
        df = pd.read_csv(os.path.join(directory, file), delimiter=',')

        # Set 'Quiz Name' column to be the same as the file name (without .csv)
        df['Quiz Name'] = os.path.splitext(file)[0]

        # Save the modified DataFrame to the original CSV file
        df.to_csv(os.path.join(directory, file), index=False)

print("Processing completed!")

