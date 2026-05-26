import pandas as pd
import matplotlib.pyplot as plt

def main():
    csv_file = "./datas/weather.csv"
    df = pd.read_csv(csv_file, sep=",")
    df = df[['年月日', '平均気温(℃)', '最高気温(℃)','最低気温(℃)']][1:51]
    print(df)
    plt.plot(df["年月日"], df['平均気温(℃)'], label="average")
    plt.plot(df["年月日"], df['最高気温(℃)'], label="maximum")
    plt.plot(df["年月日"], df['最低気温(℃)'], label="lowest")
    plt.title("50 days")
    plt.xlabel("date")
    plt.ylabel("temp(℃)")
    plt.xticks(range(0,len(df),5),df["年月日"][::5])
    plt.tight_layout()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()