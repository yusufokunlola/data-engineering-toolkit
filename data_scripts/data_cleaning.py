# import library
import pandas as pd

# function to clean data
def clean_data(input_file, output_file):
    """
    Performs basic data cleaning:
    - Loads data from a CSV file
    - Removes duplicate rows
    - Fills missing values (strings with 'Unknown', numbers with 0)
    - Saves the cleaned output to a new CSV file.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the cleaned CSV file.
    """

    # load dataset
    df = pd.read_csv(input_file)

    # Drop duplicates
    df = df.drop_duplicates()

    # Fill missing values
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].fillna("Unknown")
        else:
            df[col] = df[col].fillna(0)

    # save file as csv
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")