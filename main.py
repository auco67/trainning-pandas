import pandas as pd
import numpy as np
import plotly.express as px

def main():
    df_gapminder = px.data.gapminder()
    df_1 = df_gapminder.iloc[:100, :]
    df_2 = df_gapminder.iloc[100:200, :]
    print(pd.concat([df_1, df_2]))

if __name__ == "__main__":
    main()