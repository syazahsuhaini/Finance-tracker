import pandas as pd
import sys

from scripts.data_path import raw_data, processed_folder
from scripts.dict import categories

def preprocess():
    # import data
    file = pd.read_csv(raw_data)

    # create dataframe
    df = pd.DataFrame(file)

    # remove str
    df['Transaction Amount'] = (
    df['Transaction Amount'].str.replace("RM", "", regex=False).str.replace(",", "", regex=False)
    )

    # change data type
    convert_dict = {'Reference 1': str, 'Reference 2': str, 'Transaction Description': str, 'Transaction Amount': float}
    df = df.astype(convert_dict)

    # add new column into df with value
    df['Category'] = 'Uncategorized'

    # assign category
    for category_name, keywords in categories.items():
        pattern = '|'.join(keywords)
        mask = (
            df['Reference 1'].str.contains(pattern, case=False, na=False) |
            df['Reference 2'].str.contains(pattern, case=False, na=False) |
            df['Transaction Description'].str.contains(pattern, case=False, na=False)
        )
        df.loc[mask, 'Category'] = category_name

    # count uncategorized
    uncategorized_records = df[df['Category']=='Uncategorized']
    uncategorized_count = len(uncategorized_records)

    if uncategorized_count > 0:
        print(f'You have {uncategorized_count} Uncategorized records.\nNeed to categorized it manually.')


    # making sure the folder exists
    # parents=True means create all missing parent folders if doesnt exists
    # exist_ok=True means if folder exists then do nothing
    processed_folder.mkdir(parents=True, exist_ok=True)

    # convert the current df into csv
    output_file = processed_folder / "processed.csv"
    df.to_csv(output_file, index=False)


    return

"""
if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: python preprocess.py")
        sys.exit(1)
        
    preprocess()
"""