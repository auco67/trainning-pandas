# trainning-pandas
- pandasの使い方を学ぶ
- Pythonのデータ可視化ライブラリであるPlotly（プロットリー）を用いてデータ抽出を行う

## データ

使用するデータは、Plotlyに最初から用意されている練習・デモ用の有名なデータセットgapminderを利用する

main.py
```
import pandas as pd
import numpy as np
import plotly.express as px

def main():
    df = px.data.gapminder()
    print(df)

if __name__ == "__main__":
    main()
```

`main.py`実行結果
```
          country continent  year  lifeExp       pop   gdpPercap iso_alpha  iso_num
0     Afghanistan      Asia  1952   28.801   8425333  779.445314       AFG        4
1     Afghanistan      Asia  1957   30.332   9240934  820.853030       AFG        4
2     Afghanistan      Asia  1962   31.997  10267083  853.100710       AFG        4
3     Afghanistan      Asia  1967   34.020  11537966  836.197138       AFG        4
4     Afghanistan      Asia  1972   36.088  13079460  739.981106       AFG        4
...           ...       ...   ...      ...       ...         ...       ...      ...
1699     Zimbabwe    Africa  1987   62.351   9216418  706.157306       ZWE      716
1700     Zimbabwe    Africa  1992   60.377  10704340  693.420786       ZWE      716
1701     Zimbabwe    Africa  1997   46.809  11404948  792.449960       ZWE      716
1702     Zimbabwe    Africa  2002   39.989  11926563  672.038623       ZWE      716
1703     Zimbabwe    Africa  2007   43.487  12311143  469.709298       ZWE      716

[1704 rows x 8 columns]
```

### データ型

- `df.dtypes`：データフレームの型を確認する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df.dtypes)

    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
    continent        str
    year           int64
    lifeExp      float64
    pop            int64
    gdpPercap    float64
    iso_alpha        str
    iso_num        int64
    dtype: object
    ```

- `df.info()`：データフレーム情報を確認する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df.info())

    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
    <class 'pandas.DataFrame'>
    RangeIndex: 1704 entries, 0 to 1703
    Data columns (total 8 columns):
    #   Column     Non-Null Count  Dtype  
    ---  ------     --------------  -----  
    0   country    1704 non-null   str    
    1   continent  1704 non-null   str    
    2   year       1704 non-null   int64  
    3   lifeExp    1704 non-null   float64
    4   pop        1704 non-null   int64  
    5   gdpPercap  1704 non-null   float64
    6   iso_alpha  1704 non-null   str    
    7   iso_num    1704 non-null   int64  
    dtypes: float64(2), int64(3), str(3)
    memory usage: 106.6 KB
    None
    ```

### 列の抽出

1. `df[column_name]`：カラム名lifeExpから一列抽出する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df["lifeExp"])

    if __name__ == "__main__":
        main()
    ```
    
    `main.py`実行結果
    ```
    0       28.801
    1       30.332
    2       31.997
    3       34.020
    4       36.088
            ...  
    1699    62.351
    1700    60.377
    1701    46.809
    1702    39.989
    1703    43.487
    Name: lifeExp, Length: 1704, dtype: float64
    ```

2. `df.loc[:, column_name]`：カラム名lifeExpから一列抽出する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df.loc[:,"lifeExp"])

    if __name__ == "__main__":
        main()
    ```

3. `df.iloc[:, column_num]`：カラム番号から一列抽出する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        pprint(df.iloc[:,3])

    if __name__ == "__main__":
        main()
    ```
    
    `main.py`実行結果
    ```
    0       28.801
    1       30.332
    2       31.997
    3       34.020
    4       36.088
            ...  
    1699    62.351
    1700    60.377
    1701    46.809
    1702    39.989
    1703    43.487
    Name: lifeExp, Length: 1704, dtype: float64
    ```

### 列行の抽出

1. `df.loc[:, [column_name]]`：リスト型のカラム名から複数列抽出する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df.loc[:,["lifeExp","pop"]])

    if __name__ == "__main__":
        main()
    ```
    
    `main.py`実行結果
    ```
          lifeExp       pop
    0      28.801   8425333
    1      30.332   9240934
    2      31.997  10267083
    3      34.020  11537966
    4      36.088  13079460
    ...       ...       ...
    1699   62.351   9216418
    1700   60.377  10704340
    1701   46.809  11404948
    1702   39.989  11926563
    1703   43.487  12311143

    [1704 rows x 2 columns]
    ```

2. `df.iloc[:, [column_num]]`：List型のカラム番号から複数列抽出する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        pprint(df.iloc[:,[3,4]])

    if __name__ == "__main__":
        main()
    ```
    
    `main.py`実行結果
    ```
          lifeExp       pop
    0      28.801   8425333
    1      30.332   9240934
    2      31.997  10267083
    3      34.020  11537966
    4      36.088  13079460
    ...       ...       ...
    1699   62.351   9216418
    1700   60.377  10704340
    1701   46.809  11404948
    1702   39.989  11926563
    1703   43.487  12311143
    [1704 rows x 2 columns]
    ```

3. `df.iloc[:, start_column_num:end_column_num]`：開始カラム番号、終了カラム番号から複数列抽出する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df.iloc[:,3:5])

    if __name__ == "__main__":
        main()
    ```
    
    `main.py`実行結果
    ```
          lifeExp       pop
    0      28.801   8425333
    1      30.332   9240934
    2      31.997  10267083
    3      34.020  11537966
    4      36.088  13079460
    ...       ...       ...
    1699   62.351   9216418
    1700   60.377  10704340
    1701   46.809  11404948
    1702   39.989  11926563
    1703   43.487  12311143
    [1704 rows x 2 columns]
    ```

4. `df.loc[start_row:end_row, [column_name]]`：リスト型のカラム名から複数列１行から１０行までを抽出する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df.loc[0:9,["lifeExp","pop"]])

    if __name__ == "__main__":
        main()
    ```
    
    `main.py`実行結果
    ```
       lifeExp       pop
    0   28.801   8425333
    1   30.332   9240934
    2   31.997  10267083
    3   34.020  11537966
    4   36.088  13079460
    5   38.438  14880372
    6   39.854  12881816
    7   40.822  13867957
    8   41.674  16317921
    9   41.763  22227415
    ```

### その他の抽出

- `df.T`：DataFrameの行列を転置する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df.T)

    if __name__ == "__main__":
        main()
    ```
    
    `main.py`実行結果
    ```
    0            1            2            3            4     ...        1699        1700       1701        1702        
    country    Afghanistan  Afghanistan  Afghanistan  Afghanistan  Afghanistan  ...    Zimbabwe    Zimbabwe   Zimbabwe    Zimbabwe    Zimbabwe
    continent         Asia         Asia         Asia         Asia         Asia  ...      Africa      Africa     Africa      Africa      Africa
    year              1952         1957         1962         1967         1972  ...        1987        1992       1997        2002        2007
    lifeExp         28.801       30.332       31.997        34.02       36.088  ...      62.351      60.377     46.809      39.989      43.487
    pop            8425333      9240934     10267083     11537966     13079460  ...     9216418    10704340   11404948    11926563    12311143
    gdpPercap   779.445314    820.85303    853.10071   836.197138   739.981106  ...  706.157306  693.420786  792.44996  672.038623  469.709298
    iso_alpha          AFG          AFG          AFG          AFG          AFG  ...         ZWE         ZWE        ZWE         ZWE         ZWE
    iso_num              4            4            4            4            4  ...         716         716        716         716         716

    [8 rows x 1704 columns]
    ```

- `df.head()`：先頭から５行目を取得する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df.head())

    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
            country continent  year  lifeExp       pop   gdpPercap iso_alpha  iso_num
    0  Afghanistan      Asia  1952   28.801   8425333  779.445314       AFG        4
    1  Afghanistan      Asia  1957   30.332   9240934  820.853030       AFG        4
    2  Afghanistan      Asia  1962   31.997  10267083  853.100710       AFG        4
    3  Afghanistan      Asia  1967   34.020  11537966  836.197138       AFG        4
    4  Afghanistan      Asia  1972   36.088  13079460  739.981106       AFG        4
    ```

- `df.tail()`：末頭から５行目を取得する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df.tail())

    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
            country continent  year  lifeExp       pop   gdpPercap iso_alpha  iso_num
    1699  Zimbabwe    Africa  1987   62.351   9216418  706.157306       ZWE      716
    1700  Zimbabwe    Africa  1992   60.377  10704340  693.420786       ZWE      716
    1701  Zimbabwe    Africa  1997   46.809  11404948  792.449960       ZWE      716
    1702  Zimbabwe    Africa  2002   39.989  11926563  672.038623       ZWE      716
    1703  Zimbabwe    Africa  2007   43.487  12311143  469.709298       ZWE      716
    ```

- `df.index`：index情報を表示する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df.index)

    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
    RangeIndex(start=0, stop=1704, step=1)
    ```

- `df.columns`：カラム情報を表示する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df.columns)

    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
    Index(['country', 'continent', 'year', 'lifeExp', 'pop', 'gdpPercap',
       'iso_alpha', 'iso_num'],
      dtype='str')
    ```

- `df.sample(row_num)`：ランダムに複数行を表示する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df.sample(100))

    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
                country continent  year  lifeExp       pop     gdpPercap iso_alpha  iso_num
    1082   Netherlands    Europe  1962   73.230  11805689  12790.849560       NLD      528
    1003      Mongolia      Asia  1987   60.222   2015133   2338.008304       MNG      496
    564        Germany    Europe  1952   67.500  69145952   7144.114393       DEU      276
    1014    Montenegro    Europe  1982   74.101    562548  11222.587620       MNE      499
    1406  South Africa    Africa  1962   49.951  18356657   5768.729717       ZAF      710
    ...            ...       ...   ...      ...       ...           ...       ...      ...
    202   Burkina Faso    Africa  2002   50.650  12251209   1037.645221       BFA      854
    110        Belgium    Europe  1962   70.250   9218400  10991.206760       BEL       56
    982      Mauritius    Africa  2002   71.954   1200206   9021.815894       MUS      480
    1315  Saudi Arabia      Asia  1987   66.295  14619745  21198.261360       SAU      682
    1078         Nepal      Asia  2002   61.340  25873917   1057.206311       NPL      524

    [100 rows x 8 columns]
    (venv) PS C:\Users\use
    ```




