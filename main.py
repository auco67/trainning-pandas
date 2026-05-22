import openpyxl
import pandas as pd
import matplotlib.pyplot as plt

def main():
    file_path = "./dataset/sales_transactions.xlsx"
    df_xls = pd.read_excel(file_path,"Sheet1", index_col=0)
    df_xls["quantity"] = df_xls["quantity"].fillna(1)
    df_xls["sale"] = df_xls["revenue"] * df_xls["quantity"]
    df_daily_sales = df_xls.groupby("ymd")["sale"].sum().reset_index()
    plt.plot(df_daily_sales["ymd"], df_daily_sales["sale"])
    plt.title("Daily Sales")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    # plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()