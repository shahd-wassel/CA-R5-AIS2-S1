from preprocessing import (
    Read_data_file,
    Drop_unnecessary_features,
    Check_data_type
)

from config.config import COLS_TO_DROP


file_path = input("Enter the CSV file path: ")

df = Read_data_file(file_path)

if isinstance(df, str):
    print(df)

else:
    print("\nOriginal Dataset:")
    print(df.head())

    df = Drop_unnecessary_features(df, COLS_TO_DROP)

    if isinstance(df, str):
        print(df)

    else:
        print("\nDataset after removing unnecessary features:")
        print(df.head())

        print("\nData Quality Report:")
        print(Check_data_type(df))