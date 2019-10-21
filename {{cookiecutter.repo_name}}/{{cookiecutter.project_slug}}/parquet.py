import pandas as pd
from .atomic_writer import (
    atomic_write
)
def convert_excel_to_parquet(data_source):
    """Converts an excel file to an equivalent parquet file that gets saved
    :param data_source: path to input excel file
    :return: the path to the newly created parquet file
    """
    # read excel file
    df = pd.read_excel(data_source, index_col=0)

    # save dataframe to parquet file
    parquet_file = os.path.splitext(data_source)[0] + ".parquet"
    with atomic_write(parquet_file, as_file=False) as f:
        df.to_parquet(f, engine="pyarrow")

    # return parquet file path
    return parquet_file


def read_parquet_columns(parquet_file, columns):
    """Converts an excel file to an equivalent parquet file that gets saved
    :param parquet_file: path to parquet file
    :param columns: list of columns
    :return: dataframe containing requested columns only
    """
    # read only specified columns and return them
    data = pd.read_parquet(parquet_file, engine="pyarrow", columns=columns)
    return data