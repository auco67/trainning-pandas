import pandas as pd
import numpy as np
import plotly.express as px

def main():
    df = px.data.gapminder()
    pop_pivot = pd.pivot_table(df, index=["year"], columns=["continent"], values=["pop"], aggfunc="mean")
    print(pop_pivot.divide(pop_pivot.sum(axis=1), axis=0)*100)
if __name__ == "__main__":
    main()