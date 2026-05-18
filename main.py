import pandas as pd
import numpy as np
import plotly.express as px

def main():
    df = px.data.gapminder()
    print(df.sample(100))

if __name__ == "__main__":
    main()