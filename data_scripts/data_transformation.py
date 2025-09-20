# import library
import pandas as pd

# function to transform data
def transform_data(input_file, output_file):
    """
    Performs basic data transformation:
    - Standardizes column names (lowercase, replace spaces with underscores)
    - Creates a new column that doubles the values of the first numeric column (if present)
    - Saves the transformed data to a new CSV file.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the transformed CSV file.
    """

    # load dataset
    df = pd.read_csv(input_file)

    # Make all column names lowercase
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]

    # Create a new column (e.g., double the first numeric column)
    num_cols = df.select_dtypes(include="number").columns
    if len(num_cols) > 0:
        df["double_" + num_cols[0]] = df[num_cols[0]] * 2

    # save as csv file
    df.to_csv(output_file, index=False)
    print(f"Transformed data saved to {output_file}")