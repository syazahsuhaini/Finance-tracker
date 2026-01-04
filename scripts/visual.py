import matplotlib.pyplot as plt
import sys

from scripts.operation import operation
from scripts.data_path import chart_folder

def visual(spending_chart, month, spent, income, category_rec):
    
    spending_chart.plot(kind='pie', autopct='%1.1f%%')

    plt.title(f'{month} Spending % by Category')

    plt.ylabel('')

    plt.text(
        1.25, 0.95,
        f"Total spent    : RM {spent:,.2f}\n"
        f"Total income : RM {income:,.2f}\n\n"
        f"By category  :\n{category_rec}",
        transform=plt.gca().transAxes,
        ha='left',
        va='top',
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="gray")
    )

    # making sure the folder exists
    # parents=True means create all missing parent folders if doesnt exists
    # exist_ok=True means if folder exists then do nothing
    chart_folder.mkdir(parents=True, exist_ok=True)
    output_file = chart_folder / f"{month}_summary.png"

    # export the pie chart as png
    plt.savefig(output_file, bbox_inches='tight', dpi=300)

    plt.show()
    
    return

"""
if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: python visual.py")
        sys.exit(1)

    spending_chart, month, spent, income, category_rec = operation()
    visual(spending_chart, month, spent, income, category_rec)
"""