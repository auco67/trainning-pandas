import pandas as pd
import matplotlib.pyplot as plt

def main():
    csv_file = './datas/weather.csv'
    csv_output = './datas/export.csv'
    df = pd.read_csv(csv_file, sep=',')
    df = df[['年月日', '平均気温(℃)', '最高気温(℃)', '最低気温(℃)', '降水量の合計(mm)',  '最深積雪(cm)', '平均雲量(10分比)',  '平均蒸気圧(hPa)', '平均風速(m/s)','日照時間(時間)']]
    df = df.fillna(0)
    print(df[1:])
    df.to_csv(csv_output, index=False)

if __name__ == '__main__':
    main()