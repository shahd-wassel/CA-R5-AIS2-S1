import pandas as pd


def Read_data_file(file_path):
    """
    Reads a CSV file and returns it as a pandas DataFrame.

    Args:
        file_path (str): The path of the CSV file.

    Returns:
        DataFrame: The data read from the CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        return df

    except FileNotFoundError:
        return f"Error: File '{file_path}' was not found."

    except pd.errors.EmptyDataError:
        return "Error: The file is empty."

    except Exception as e:
        return f"Error: Unable to read the file. {e}"


def Drop_unnecessary_features(df, cols_to_drop):
    """
    Removes unnecessary columns from the DataFrame.

    Args:
        df (DataFrame): The input DataFrame.
        cols_to_drop (list): List of columns to remove.

    Returns:
        DataFrame: The DataFrame after removing the columns.
    """
    try:
        df = df.drop(columns=cols_to_drop)
        return df

    except KeyError as e:
        return f"Error: Column not found. {e}"


def Check_data_type(df):
    """
    Creates a data-quality report for the DataFrame.

    Args:
        df (DataFrame): The input DataFrame.

    Returns:
        DataFrame: A transposed DataFrame containing
        column datatype and number of unique values.
    """
    report = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.values,
        "Unique Values": df.nunique().values
    })

    return report.set_index("Column").T
# t for transpose
 