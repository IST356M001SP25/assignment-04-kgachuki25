'''
A Library of useful pandas helper functions
SOLUTION FILE!!!!
'''
import pandas as pd

def get_column_names(df : pd.DataFrame) -> list[str]:
    '''
    Get all column names of a pandas dataframe df
    Returns the names as a list of string
    '''
    col_names = list(df.columns)
    return col_names


def get_columns_of_type(df : pd.DataFrame, numpy_type: any) -> list[str]:
    '''
    Return the column names of a pandas dataframe only when 
    the values in the column match the numpy_type
    '''
    newDF = df.select_dtypes(include = numpy_type)
    col_names = list(newDF.columns)
    return col_names


def get_unique_values(df : pd.DataFrame, column_name: str) -> list:
    '''
    Get a list of unique values of a column in a pandas dataframe
    '''
    unique_list = list(df[column_name].unique())
    return unique_list

def get_file_extension(file_path : str) -> str:
    '''
    Return the file extension of a file_path for example:
    '/some/file/data.csv' -> 'csv'
    '/home/important_grades.xlsx' -> 'xlsx'
    'countries.json' -> 'json'

    '''
    file_split = file_path.split(".")
    file_extension = file_split[1]
    return file_extension

def load_file(file_path: str, ext: str) -> pd.DataFrame:
    '''
    Load a file into a pandas dataframe assumed the file type from the extension
    return a pandas dataframe
    only suppose csv, excel and json file extensions
    - when csv assume first row is header
    - when json assume record-oriented data
    '''
    if ext == "csv":
        newDF = pd.read_csv(file_path, header = 0)
    elif ext == "json":
        newDF = pd.read_json(file_path, orient = "records")
    elif ext == "xlsx" or ext == "xls":
        newDF = pd.read_excel(file_path)
    else:
        print("Unrecognized file type, unable to read")
    
    return newDF

if __name__ == '__main__':
    df = pd.DataFrame({ 
        "name": ["Alice", "Bob", "Chris", "Dee", "Eddie", "Fiona"],
        "age": [25, 30, 35, 40, 45, 50],
        "state": ["NY", "PA", "NY", "NY", "PA", "NJ"],
        "balance": [100.0, 200.0, 250.0, 310.0, 100.0, 60.0]
        })
    cols = get_column_names(df)
    print(f"Columns: {cols}")
    cols = get_columns_of_type(df, 'object')
    print(f"Object Columns: {cols}")
    cols = get_columns_of_type(df, 'int64')
    print(f"Int64 Columns: {cols}")
    cols = get_columns_of_type(df, 'float64')
    print(f"Float64 Columns: {cols}")
    unique = get_unique_values(df, 'state')
    print(f"Unique States: {unique}")

    assert get_file_extension("example.csv") == "csv"
    assert get_file_extension("data/files/idk/example.json") == "json"
    assert get_file_extension("askdsajdaslkj/example.xls") == "xls"

    test_file_path = "data/car_owners.csv"
    test_df = load_file(test_file_path, "csv")
    print(test_df.head())

    test_file_path2 = "data/car_owners.json"
    test_df2 = load_file(test_file_path2, "json")
    print(test_df2.head())
