import pandas as pd
import numpy as np
import plotly.express as px

def main():
    df = px.data.gapminder()
    print(df)
    print(df.set_index("country"))
    print(df.reset_index())
if __name__ == "__main__":
    main()