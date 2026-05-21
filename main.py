import pandas as pd
import numpy as np
import plotly.express as px

def calc_median(df:pd.DataFrame)-> pd.DataFrame:
    df["pop_median_status"] = pd.NA
    pop_median = df["pop"].median()
    
    df["pop_median_status"] = np.where(
        df["pop"] <= pop_median,
        "smaller",
        "greater"
    )

    return df

def main():
    df = px.data.gapminder()
    df = calc_median(df)
    print(df)
if __name__ == "__main__":
    main()