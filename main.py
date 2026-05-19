import pandas as pd
import numpy as np
import plotly.express as px

def main():
    df = px.data.gapminder()
    print(df.sort_values(["year","lifeExp"], ascending=False))

if __name__ == "__main__":
    main()