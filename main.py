import pandas as pd
import numpy as np
import plotly.express as px

def main():
    df = px.data.gapminder()
    df_copy = df.copy()
    df_copy["flag"] = False
    print(df_copy.head())
    print(df_copy.dtypes)


if __name__ == "__main__":
    main()