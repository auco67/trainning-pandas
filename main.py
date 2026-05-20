import pandas as pd
import numpy as np
import plotly.express as px

def main():
    df = px.data.gapminder()
    df.loc[1704,:] = pd.NA
    print(df)
    print(df.dropna())

if __name__ == "__main__":
    main()