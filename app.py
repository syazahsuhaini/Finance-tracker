import argparse

from scripts.data_path import *
from scripts.dict import *
from scripts.preprocess import *
from scripts.operation import *
from scripts.visual import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Financial tracker',
        description='Tracking my financial.',
        epilog='by Syaza')
    
    parser.add_argument('--clean',   # -- indicate as flag
                        action='store_true',    # if flag is in the argument, return TRUE for args.sort
                        help='Preprocess data by categorizing the records.')
    
    parser.add_argument('--visual',   # -- indicate as flag
                        action='store_true',    # if flag is in the argument, return TRUE for args.sort
                        help='Visualized the processed data.')
    
    args = parser.parse_args()

    if args.clean:
        preprocess()
    elif args.visual:
        spending_chart, month, spent, income, category_rec = operation()
        visual(spending_chart, month, spent, income, category_rec)
    else:
        print('No flags provided. Nothing will run.')