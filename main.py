import pandas as pd
import numpy as np
import plotly.express as px

def main():
    df = px.data.gapminder()
    df.loc[1704,:] = df.loc[1703,:] 
    print(df)
    print(df.drop_duplicates())

if __name__ == "__main__":
    main()