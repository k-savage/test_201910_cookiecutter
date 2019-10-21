from .hash_str import get_csci_salt, get_user_id, hash_str
from .atomic_writer import atomic_write
from .parquet import convert_excel_to_parquet, read_parquet_columns
import pandas as pd
import os


if __name__ == "__main__":
    print("example atomic write: ")
    with atomic_write('foo.txt') as f:
        f.write('Hello world1.')

    print("hashing: ")
    for user in ["gorlins", "k-savage"]:
        print("Id for {}: {}".format(user, get_user_id(user)))

        

    