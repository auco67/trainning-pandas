import pandas as pd
import numpy as np
import plotly.express as px

def main():
    df = px.data.gapminder()
    print(df["lifeExp"].quantile(0.90))

if __name__ == "__main__":
    main()