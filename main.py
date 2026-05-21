import pandas as pd
import numpy as np
import plotly.express as px

def main():
    df_gapminder = px.data.gapminder()
    file_path = "./dataset/countries_codes_and_coordinates.csv"
    df = pd.read_csv(file_path, sep=",", usecols=[2,4,5])
    for col in df.columns:
        df[col] = df[col].apply(lambda x: x.strip()[1:-1])
    print(pd.merge(df_gapminder, df, left_on="iso_alpha", right_on="Alpha-3 code", how="inner"))

if __name__ == "__main__":
    main()