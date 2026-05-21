import pandas as pd
import numpy as np
import plotly.express as px

def main():
    df = px.data.gapminder()
    continent_grp = df.groupby("continent")
    print(continent_grp[["pop", "gdpPercap"]].agg({"pop":"median","gdpPercap":"mean"}).reset_index())
if __name__ == "__main__":
    main()