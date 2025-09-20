# import library
import pandas as pd

# function to transform data
def load_data(input_file, output_file):
    """
    Performs basic data loading:
    - Reads data from a CSV file
    - Saves the data to a new CSV file
    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the output CSV file.
    """

    # load dataset
    df = pd.read_csv(input_file)

    # Write to CSV
    df.to_csv(output_file, index=False)
    print(f"Data loaded and saved to {output_file}")