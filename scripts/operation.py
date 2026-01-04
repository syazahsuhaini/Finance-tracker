import pandas as pd

from scripts.data_path import processed_data


def operation():
    # import data
    file = pd.read_csv(processed_data)

    # create dataframe
    df = pd.DataFrame(file)

    # count uncategorized
    uncategorized_records = df[df['Category']=='Uncategorized']
    uncategorized_count = len(uncategorized_records)

    if uncategorized_count > 0:
        raise ValueError(f'You have {uncategorized_count} Uncategorized records.\nNeed to categorized it manually.')

    # get month of the records
    # change date data type from str to datetime
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y') # d - 01 b - Oct Y - 2025

    # assuming the records have multiple month
    months = df['Date'].dt.strftime('%B').unique()

    if len(months) != 1:
        raise ValueError(f"Multiple months found: {months}")

    month_name = months[0]

    # sum up the whole expenses transaction of the month
    expenses = df[df['Transaction Amount']<0]
    total_spent = abs(expenses['Transaction Amount'].sum())
    spending_totals = df[df['Transaction Amount'] < 0].groupby('Category')['Transaction Amount'].sum().abs()

    # sum up the whole income of the month
    income = df[df['Transaction Amount']>0]
    total_income = income['Transaction Amount'].sum()

    # sum up Transaction Amount based on Category
    category_totals = df.groupby('Category')['Transaction Amount'].sum().abs()
    category_totals = category_totals.sort_values(ascending=False)

    recs = []
    for cat, val in category_totals.items():
        rec = f"{cat} : RM {val:,.0f}"
        recs.append(rec)

    # make rec list as a string
    by_category_rec = "\n".join(recs)

    return spending_totals, month_name, total_spent, total_income, by_category_rec

"""
if __name__ == "__main__":
    operation()
"""