import pandas as pd

def main():
    csv_file = "./datas/weather.csv"
    df = pd.read_csv(csv_file, sep=",")
    df = df[['年月日','平均気温(℃)','最高気温(℃)', '最低気温(℃)','降水量の合計(mm)','最深積雪(cm)','平均雲量(10分比)','平均蒸気圧(hPa)','平均風速(m/s)', '日照時間(時間)']][1:]
    df.columns = ['年月日','平均気温','最高気温', '最低気温','降水量の合計','最深積雪','平均雲量','平均蒸気圧','平均風速', '日照時間']
    print(df.shape)
    print(df.isnull().sum())
    print(df.dropna(axis=1))

if __name__ == "__main__":
    main()