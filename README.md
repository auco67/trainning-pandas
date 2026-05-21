# trainning-pandas
- pandasの使い方を学ぶ
- Pythonのデータ可視化ライブラリであるPlotly（プロットリー）を用いてデータ抽出を行う

## 目次
1. [使用するデータ](#01)
1. [データ型](#02)
1. [型変換](#03)
1. [列の抽出](#04)
1. [列行の抽出](#05)
1. [その他の抽出](#06)
1. [データフレームの複製](#07)
1. [データの生成・削除](#08)
1. [データのカウント・並び替え](#09)
1. [演算・統計量の計算](#10)
1. [条件による抽出](#11)
1. [null値の処理](#12)
1. [重複の処理](#13)
1. [インデックス・カラムの操作](#14)
1. [関数の適用](#15)
1. [groupby](#16)
1. [pivod table](#17)
1. [ファイル読み込み](#18)
1. [merge](#19)

<a id="01"></a>

## 使用するデータ

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

<a id="02"></a>

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

<a id="03"></a>

### 型変換

- `df[column_name].astype(type)`：`year`の`int`を`str`に変換する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        df["year"] = df["year"].astype(str)
        print(df["year"])

    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
    0       1952
    1       1957
    2       1962
    3       1967
    4       1972
            ... 
    1699    1987
    1700    1992
    1701    1997
    1702    2002
    1703    2007
    Name: year, Length: 1704, dtype: str
    ```

<a id="04"></a>

### 列の抽出

- `df[column_name]`：カラム名lifeExpから一列抽出する

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

- `df.loc[:, column_name]`：カラム名lifeExpから一列抽出する

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

- `df.iloc[:, column_num]`：カラム番号から一列抽出する

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

<a id="05"></a>

### 列行の抽出

- `df.loc[:, [column_name]]`：リスト型のカラム名から複数列抽出する

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

- `df.iloc[:, [column_num]]`：List型のカラム番号から複数列抽出する

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

- `df.iloc[:, start_column_num:end_column_num]`：開始カラム番号、終了カラム番号から複数列抽出する

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

- `df.loc[start_row:end_row, [column_name]]`：リスト型のカラム名から複数列１行から１０行までを抽出する

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

<a id="06"></a>

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

- 特定の型を抽出する

    `df.select_dtypes(include=type)`：object型のデータのみ抽出する場合

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df.select_dtypes(include="object"))

    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
              country continent iso_alpha
    0     Afghanistan      Asia       AFG
    1     Afghanistan      Asia       AFG
    2     Afghanistan      Asia       AFG
    3     Afghanistan      Asia       AFG
    4     Afghanistan      Asia       AFG
    ...           ...       ...       ...
    1699     Zimbabwe    Africa       ZWE
    1700     Zimbabwe    Africa       ZWE
    1701     Zimbabwe    Africa       ZWE
    1702     Zimbabwe    Africa       ZWE
    1703     Zimbabwe    Africa       ZWE

    [1704 rows x 3 columns]
    ```

- `df.select_dtypes(type).columns`：特定の型のカラム名を抽出する

    int型のデータのみのカラム名を抽出する場合
    
    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df.select_dtypes(int).columns)

    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
    Index(['year', 'pop', 'iso_num'], dtype='str')
    ```

- `df.describe()`：数値型のカラムに対して合計値などを返す

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df.describe())

    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
                 year      lifeExp           pop      gdpPercap      iso_num
    count  1704.00000  1704.000000  1.704000e+03    1704.000000  1704.000000
    mean   1979.50000    59.474439  2.960121e+07    7215.327081   425.880282
    std      17.26533    12.917107  1.061579e+08    9857.454543   248.305709
    min    1952.00000    23.599000  6.001100e+04     241.165876     4.000000
    25%    1965.75000    48.198000  2.793664e+06    1202.060309   208.000000
    50%    1979.50000    60.712500  7.023596e+06    3531.846989   410.000000
    75%    1993.25000    70.845500  1.958522e+07    9325.462346   638.000000
    max    2007.00000    82.603000  1.318683e+09  113523.132900   894.000000
    ```

<a id="07"></a>

### データフレームの複製

`df.copy()`：データフレームを複製し、元のデータフレームを残しておきたい場合

main.py
```
import pandas as pd
import numpy as np
import plotly.express as px

def main():
    df = px.data.gapminder()
    df_copy = df.copy()
    print(df_copy)

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

<a id="08"></a>

### データの生成・削除

- `df[new_colum_name] = new_value`：データフレームに新しくカラム（flag）を作成する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        df_copy = df.copy()
        df_copy["flag"] = False
        print(df_copy.head())
        print(df_copy.dtypes)


    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
        country continent  year  lifeExp       pop   gdpPercap iso_alpha  iso_num   flag
    0  Afghanistan      Asia  1952   28.801   8425333  779.445314       AFG        4  False
    1  Afghanistan      Asia  1957   30.332   9240934  820.853030       AFG        4  False
    2  Afghanistan      Asia  1962   31.997  10267083  853.100710       AFG        4  False
    3  Afghanistan      Asia  1967   34.020  11537966  836.197138       AFG        4  False
    4  Afghanistan      Asia  1972   36.088  13079460  739.981106       AFG        4  False
    country          str
    continent        str
    year           int64
    lifeExp      float64
    pop            int64
    gdpPercap    float64
    iso_alpha        str
    iso_num        int64
    flag            bool
    dtype: object
    ```

- `df_copy.drop(column_name, axis=1, inplace=True)`：データフレームのカラム（flag）を削除する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        df_copy = df.copy()
        df_copy["flag"] = False
        print(df_copy.head())
        df_copy.drop("flag", axis=1, inplace=True)
        print(df_copy.head())

    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
        country continent  year  lifeExp       pop   gdpPercap iso_alpha  iso_num   flag
    0  Afghanistan      Asia  1952   28.801   8425333  779.445314       AFG        4  False
    1  Afghanistan      Asia  1957   30.332   9240934  820.853030       AFG        4  False
    2  Afghanistan      Asia  1962   31.997  10267083  853.100710       AFG        4  False
    3  Afghanistan      Asia  1967   34.020  11537966  836.197138       AFG        4  False
    4  Afghanistan      Asia  1972   36.088  13079460  739.981106       AFG        4  False
        country continent  year  lifeExp       pop   gdpPercap iso_alpha  iso_num
    0  Afghanistan      Asia  1952   28.801   8425333  779.445314       AFG        4
    1  Afghanistan      Asia  1957   30.332   9240934  820.853030       AFG        4
    2  Afghanistan      Asia  1962   31.997  10267083  853.100710       AFG        4
    3  Afghanistan      Asia  1967   34.020  11537966  836.197138       AFG        4
    4  Afghanistan      Asia  1972   36.088  13079460  739.981106       AFG        4
    ```

- `df_copy.loc[add_row,:] = value`：データフレームに新しく行を追加する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        df_copy = df.copy()
        df_copy.loc[1704,:] = pd.NA
        print(df_copy.tail())

    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
           country continent    year  lifeExp         pop   gdpPercap iso_alpha  iso_num
    1700  Zimbabwe    Africa  1992.0   60.377  10704340.0  693.420786       ZWE    716.0
    1701  Zimbabwe    Africa  1997.0   46.809  11404948.0  792.449960       ZWE    716.0
    1702  Zimbabwe    Africa  2002.0   39.989  11926563.0  672.038623       ZWE    716.0
    1703  Zimbabwe    Africa  2007.0   43.487  12311143.0  469.709298       ZWE    716.0
    1704       NaN       NaN     NaN      NaN         NaN         NaN       NaN      NaN
    ```

- `df.drop(row_num, axis=0, inplace=True)`：データフレームの行を削除する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        df_copy = df.copy()
        df_copy.loc[1704,:] = pd.NA
        print(df_copy.tail())
        df_copy.drop(1704, axis=0, inplace=True)
        print(df_copy.tail())

    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
        country continent    year  lifeExp         pop   gdpPercap iso_alpha  iso_num
    1700  Zimbabwe    Africa  1992.0   60.377  10704340.0  693.420786       ZWE    716.0
    1701  Zimbabwe    Africa  1997.0   46.809  11404948.0  792.449960       ZWE    716.0
    1702  Zimbabwe    Africa  2002.0   39.989  11926563.0  672.038623       ZWE    716.0
    1703  Zimbabwe    Africa  2007.0   43.487  12311143.0  469.709298       ZWE    716.0
    1704       NaN       NaN     NaN      NaN         NaN         NaN       NaN      NaN
        country continent    year  lifeExp         pop   gdpPercap iso_alpha  iso_num
    1699  Zimbabwe    Africa  1987.0   62.351   9216418.0  706.157306       ZWE    716.0
    1700  Zimbabwe    Africa  1992.0   60.377  10704340.0  693.420786       ZWE    716.0
    1701  Zimbabwe    Africa  1997.0   46.809  11404948.0  792.449960       ZWE    716.0
    1702  Zimbabwe    Africa  2002.0   39.989  11926563.0  672.038623       ZWE    716.0
    1703  Zimbabwe    Africa  2007.0   43.487  12311143.0  469.709298       ZWE    716.0
    ```

<a id="09"></a>

### データのカウント・並び替え

- `df.unique(column_name)`：カラム内のユニークなデータを抜きだす

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df["country"].unique())


    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
    <StringArray>
    [       'Afghanistan',            'Albania',            'Algeria',
                'Angola',          'Argentina',          'Australia',
                'Austria',            'Bahrain',         'Bangladesh',
                'Belgium',
    ...
                'Uganda',     'United Kingdom',      'United States',
                'Uruguay',          'Venezuela',            'Vietnam',
    'West Bank and Gaza',        'Yemen, Rep.',             'Zambia',
            'Zimbabwe']
    Length: 142, dtype: str
    ```

- `df.nunique(column_name)`：カラム内のユニークなデータを数を調べる

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df["country"].nunique())


    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
    142
    ```

- `df[column_name].value_counts()`：カラムデータの登場回数を調べる

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df["continent"].value_counts())


    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
    continent
    Africa      624
    Asia        396
    Europe      360
    Americas    300
    Oceania      24
    Name: count, dtype: int64
    ```

- `df.sort_values(by=column_name, ascending=False)`：特定のカラムを降順に並び替える

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df.sort_values("year", ascending=False))

    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
                     country continent  year  lifeExp        pop     gdpPercap iso_alpha  iso_num
    1679         Yemen, Rep.      Asia  2007   62.698   22211743   2280.769906       YEM      887
    35               Algeria    Africa  2007   72.301   33333216   6223.367465       DZA       12
    1139             Nigeria    Africa  2007   46.859  135031164   2013.977305       NGA      566
    1127               Niger    Africa  2007   56.867   12894865    619.676892       NER      562
    575              Germany    Europe  2007   79.406   82400996  32170.374420       DEU      276
    ...                  ...       ...   ...      ...        ...           ...       ...      ...
    828     Korea, Dem. Rep.      Asia  1952   50.056    8865488   1088.277758       KOR      410
    48             Argentina  Americas  1952   62.485   17876956   5911.315053       ARG       32
    1656  West Bank and Gaza      Asia  1952   43.160    1030585   1515.592329       PSE      275
    24               Algeria    Africa  1952   43.077    9279525   2449.008185       DZA       12
    0            Afghanistan      Asia  1952   28.801    8425333    779.445314       AFG        4

    [1704 rows x 8 columns]
    ```

- `df.sort_values(by=[column_name], ascending=False)`：複数条件のカラムを降順に並び替える

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df.sort_values(["year","lifeExp"], ascending=False))

    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
                   country continent  year  lifeExp        pop     gdpPercap iso_alpha  iso_num
    803              Japan      Asia  2007   82.603  127467972  31656.068060       JPN      392
    671   Hong Kong, China      Asia  2007   82.208    6980412  39724.978670       HKG      344
    695            Iceland    Europe  2007   81.757     301931  36180.789190       ISL      352
    1487       Switzerland    Europe  2007   81.701    7554661  37506.419070       CHE      756
    71           Australia   Oceania  2007   81.235   20434176  34435.367440       AUS       36
    ...                ...       ...   ...      ...        ...           ...       ...      ...
    1032        Mozambique    Africa  1952   31.286    6446316    468.526038       MOZ      508
    1344      Sierra Leone    Africa  1952   30.331    2143249    879.787736       SLE      694
    36              Angola    Africa  1952   30.015    4232095   3520.610273       AGO       24
    552             Gambia    Africa  1952   30.000     284320    485.230659       GMB      270
    0          Afghanistan      Asia  1952   28.801    8425333    779.445314       AFG        4

    [1704 rows x 8 columns]
    ```

<a id="10"></a>

## 演算・統計量の計算

- `df[column_name] + 3`：特定のカラムの値にプラス３する（ベクトル演算）

    ※注意：ベクトル演算はリスト型には対応していないためエラーとなる

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df["lifeExp"] + 3)

    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
    0       31.801
    1       33.332
    2       34.997  
    3       37.020
    4       39.088
            ...  
    1699    65.351
    1700    63.377
    1701    49.809
    1702    42.989
    1703    46.487
    Name: lifeExp, Length: 1704, dtype: float64
    ```

- `df[column_name].mean()`：特定のカラムの平均値を取得する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df["lifeExp"].mean())

    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
    59.474439366197174
    ```

- `df[column_name].median()`：特定のカラムの中央値を取得する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df["lifeExp"].median())

    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
    60.7125
    ```

- `df[column_name].min()`：特定のカラムの最小値を取得する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df["lifeExp"].min())

    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
    23.599
    ```

- `df[column_name].max()`：特定のカラムの最大値を取得する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df["lifeExp"].max())

    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
    82.603
    ```

- `df[column_name].std()`：特定のカラムの標準値を取得する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df["lifeExp"].std())

    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
    12.917107415241192
    ```

- `df[column_name].quantile(float)`：特定のカラムの割合値を取得する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df["lifeExp"].quantile(0.90))

    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
    75.097
    ```

<a id="11"></a>

## 条件による抽出

- `df[df[column_name]==value]`：特定のカラムを特定の値で抽出する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df[df["year"]==1952])

    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
                     country continent  year  lifeExp       pop    gdpPercap iso_alpha  iso_num
    0            Afghanistan      Asia  1952   28.801   8425333   779.445314       AFG        4
    12               Albania    Europe  1952   55.230   1282697  1601.056136       ALB        8
    24               Algeria    Africa  1952   43.077   9279525  2449.008185       DZA       12
    36                Angola    Africa  1952   30.015   4232095  3520.610273       AGO       24
    48             Argentina  Americas  1952   62.485  17876956  5911.315053       ARG       32
    ...                  ...       ...   ...      ...       ...          ...       ...      ...
    1644             Vietnam      Asia  1952   40.412  26246839   605.066492       VNM      704
    1656  West Bank and Gaza      Asia  1952   43.160   1030585  1515.592329       PSE      275
    1668         Yemen, Rep.      Asia  1952   32.548   4963829   781.717576       YEM      887
    1680              Zambia    Africa  1952   42.038   2672000  1147.388831       ZMB      894
    1692            Zimbabwe    Africa  1952   48.451   3080907   406.884115       ZWE      716

    [142 rows x 8 columns]
    ```

- `df[column_name].isin[column_name_values]`：特定のカラムの特定の値群を抽出する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        target_contients = ["Asia", "Europe","Africa"]
        print(df[df["continent"].isin(target_contients)])
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

    [1380 rows x 8 columns]
    ```

- `df[column_name].str.contain(char)`：str型のカラムの特定の文字を含むデータを抽出する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df[df["continent"].str.contains("A")])
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

    [1320 rows x 8 columns]
    ```

- 複雑な条件による抽出

    `gdpPercap`の中央値より高い`gdpPercap`であり、`year`が`2000`以降の場合のデータを抽出する場合

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        gdp_per_cap_med = df["gdpPercap"].median()
        print(f"gdpPercap_median={gdp_per_cap_med}")
        cond1 = df["gdpPercap"] > gdp_per_cap_med
        cond2 = df["year"] >= 2000
        print(df[cond1 & cond2])

    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
    gdpPercap_median=3531.8469885000004
                     country continent  year  lifeExp       pop     gdpPercap iso_alpha  iso_num
    22               Albania    Europe  2002   75.651   3508512   4604.211737       ALB        8
    23               Albania    Europe  2007   76.423   3600523   5937.029526       ALB        8
    34               Algeria    Africa  2002   70.994  31287142   5288.040382       DZA       12
    35               Algeria    Africa  2007   72.301  33333216   6223.367465       DZA       12
    47                Angola    Africa  2007   42.731  12420476   4797.231267       AGO       24
    ...                  ...       ...   ...      ...       ...           ...       ...      ...
    1630             Uruguay  Americas  2002   75.307   3363085   7727.002004       URY      858
    1631             Uruguay  Americas  2007   76.384   3447496  10611.462990       URY      858
    1642           Venezuela  Americas  2002   72.766  24287670   8605.047831       VEN      862
    1643           Venezuela  Americas  2007   73.747  26084662  11415.805690       VEN      862
    1666  West Bank and Gaza      Asia  2002   72.370   3389578   4515.487575       PSE      275

    [173 rows x 8 columns]
    ```

- `df.query(conditions)`：query関数を使って複雑な条件でデータを抽出する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df.query('(year >= 2000) & (continent in ["Asia", "Europe","Africa"])'))

    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
              country continent  year  lifeExp       pop    gdpPercap iso_alpha  iso_num
    10    Afghanistan      Asia  2002   42.129  25268405   726.734055       AFG        4
    11    Afghanistan      Asia  2007   43.828  31889923   974.580338       AFG        4
    22        Albania    Europe  2002   75.651   3508512  4604.211737       ALB        8
    23        Albania    Europe  2007   76.423   3600523  5937.029526       ALB        8
    34        Algeria    Africa  2002   70.994  31287142  5288.040382       DZA       12
    ...           ...       ...   ...      ...       ...          ...       ...      ...
    1679  Yemen, Rep.      Asia  2007   62.698  22211743  2280.769906       YEM      887
    1690       Zambia    Africa  2002   39.193  10595811  1071.613938       ZMB      894
    1691       Zambia    Africa  2007   42.384  11746035  1271.211593       ZMB      894
    1702     Zimbabwe    Africa  2002   39.989  11926563   672.038623       ZWE      716
    1703     Zimbabwe    Africa  2007   43.487  12311143   469.709298       ZWE      716

    [230 rows x 8 columns]
    ```

<a id="12"></a>

## null値の処理

- `df.fillna()`：NaN（null値）を置き換える

    NaNを0に置き換える場合

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        df.loc[1704,:] = pd.NA
        print(df)
        print(df.fillna(0))
    if __name__ == "__main__":
        main()
    ```

     `main.py`実行結果
    ```
              country continent    year  lifeExp         pop   gdpPercap iso_alpha  iso_num
    0     Afghanistan      Asia  1952.0   28.801   8425333.0  779.445314       AFG      4.0
    1     Afghanistan      Asia  1957.0   30.332   9240934.0  820.853030       AFG      4.0
    2     Afghanistan      Asia  1962.0   31.997  10267083.0  853.100710       AFG      4.0
    3     Afghanistan      Asia  1967.0   34.020  11537966.0  836.197138       AFG      4.0
    4     Afghanistan      Asia  1972.0   36.088  13079460.0  739.981106       AFG      4.0
    ...           ...       ...     ...      ...         ...         ...       ...      ...
    1700     Zimbabwe    Africa  1992.0   60.377  10704340.0  693.420786       ZWE    716.0
    1701     Zimbabwe    Africa  1997.0   46.809  11404948.0  792.449960       ZWE    716.0
    1702     Zimbabwe    Africa  2002.0   39.989  11926563.0  672.038623       ZWE    716.0
    1703     Zimbabwe    Africa  2007.0   43.487  12311143.0  469.709298       ZWE    716.0
    1704          NaN       NaN     NaN      NaN         NaN         NaN       NaN      NaN

    [1705 rows x 8 columns]
              country continent    year  lifeExp         pop   gdpPercap iso_alpha  iso_num
    0     Afghanistan      Asia  1952.0   28.801   8425333.0  779.445314       AFG      4.0
    1     Afghanistan      Asia  1957.0   30.332   9240934.0  820.853030       AFG      4.0
    2     Afghanistan      Asia  1962.0   31.997  10267083.0  853.100710       AFG      4.0
    3     Afghanistan      Asia  1967.0   34.020  11537966.0  836.197138       AFG      4.0
    4     Afghanistan      Asia  1972.0   36.088  13079460.0  739.981106       AFG      4.0
    ...           ...       ...     ...      ...         ...         ...       ...      ...
    1700     Zimbabwe    Africa  1992.0   60.377  10704340.0  693.420786       ZWE    716.0
    1701     Zimbabwe    Africa  1997.0   46.809  11404948.0  792.449960       ZWE    716.0
    1702     Zimbabwe    Africa  2002.0   39.989  11926563.0  672.038623       ZWE    716.0
    1703     Zimbabwe    Africa  2007.0   43.487  12311143.0  469.709298       ZWE    716.0
    1704            0         0     0.0    0.000         0.0    0.000000         0      0.0

    [1705 rows x 8 columns]
    ```

    NaNに各カラムに対する値を設定する場合

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        df.loc[1704,:] = pd.NA
        print(df)
        print(df.fillna({
            "country":"Japan",
            "contient":"Asia",
            "year":1952,
            "lifeExp":0,
            "pop":0,
            "gdpPercap":0,
            "iso_alpha":"JP",
            "iso_num": 1
        }))

    if __name__ == "__main__":
        main()
    ```

     `main.py`実行結果
    ```
              country continent    year  lifeExp         pop   gdpPercap iso_alpha  iso_num
    0     Afghanistan      Asia  1952.0   28.801   8425333.0  779.445314       AFG      4.0
    1     Afghanistan      Asia  1957.0   30.332   9240934.0  820.853030       AFG      4.0
    2     Afghanistan      Asia  1962.0   31.997  10267083.0  853.100710       AFG      4.0
    3     Afghanistan      Asia  1967.0   34.020  11537966.0  836.197138       AFG      4.0
    4     Afghanistan      Asia  1972.0   36.088  13079460.0  739.981106       AFG      4.0
    ...           ...       ...     ...      ...         ...         ...       ...      ...
    1700     Zimbabwe    Africa  1992.0   60.377  10704340.0  693.420786       ZWE    716.0
    1701     Zimbabwe    Africa  1997.0   46.809  11404948.0  792.449960       ZWE    716.0
    1702     Zimbabwe    Africa  2002.0   39.989  11926563.0  672.038623       ZWE    716.0
    1703     Zimbabwe    Africa  2007.0   43.487  12311143.0  469.709298       ZWE    716.0
    1704          NaN       NaN     NaN      NaN         NaN         NaN       NaN      NaN

    [1705 rows x 8 columns]
              country continent    year  lifeExp         pop   gdpPercap iso_alpha  iso_num
    0     Afghanistan      Asia  1952.0   28.801   8425333.0  779.445314       AFG      4.0
    1     Afghanistan      Asia  1957.0   30.332   9240934.0  820.853030       AFG      4.0
    2     Afghanistan      Asia  1962.0   31.997  10267083.0  853.100710       AFG      4.0
    3     Afghanistan      Asia  1967.0   34.020  11537966.0  836.197138       AFG      4.0
    4     Afghanistan      Asia  1972.0   36.088  13079460.0  739.981106       AFG      4.0
    ...           ...       ...     ...      ...         ...         ...       ...      ...
    1700     Zimbabwe    Africa  1992.0   60.377  10704340.0  693.420786       ZWE    716.0
    1701     Zimbabwe    Africa  1997.0   46.809  11404948.0  792.449960       ZWE    716.0
    1702     Zimbabwe    Africa  2002.0   39.989  11926563.0  672.038623       ZWE    716.0
    1703     Zimbabwe    Africa  2007.0   43.487  12311143.0  469.709298       ZWE    716.0
    1704        Japan       NaN  1952.0    0.000         0.0    0.000000        JP      1.0

    [1705 rows x 8 columns]
    ```

- `df.dropna()`：NaNが存在するレコードを削除する

    main.py
    ```
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
    ```

     `main.py`実行結果
    ```
              country continent    year  lifeExp         pop   gdpPercap iso_alpha  iso_num
    0     Afghanistan      Asia  1952.0   28.801   8425333.0  779.445314       AFG      4.0
    1     Afghanistan      Asia  1957.0   30.332   9240934.0  820.853030       AFG      4.0
    2     Afghanistan      Asia  1962.0   31.997  10267083.0  853.100710       AFG      4.0
    3     Afghanistan      Asia  1967.0   34.020  11537966.0  836.197138       AFG      4.0
    4     Afghanistan      Asia  1972.0   36.088  13079460.0  739.981106       AFG      4.0
    ...           ...       ...     ...      ...         ...         ...       ...      ...
    1700     Zimbabwe    Africa  1992.0   60.377  10704340.0  693.420786       ZWE    716.0
    1701     Zimbabwe    Africa  1997.0   46.809  11404948.0  792.449960       ZWE    716.0
    1702     Zimbabwe    Africa  2002.0   39.989  11926563.0  672.038623       ZWE    716.0
    1703     Zimbabwe    Africa  2007.0   43.487  12311143.0  469.709298       ZWE    716.0
    1704          NaN       NaN     NaN      NaN         NaN         NaN       NaN      NaN

    [1705 rows x 8 columns]
              country continent    year  lifeExp         pop   gdpPercap iso_alpha  iso_num
    0     Afghanistan      Asia  1952.0   28.801   8425333.0  779.445314       AFG      4.0
    1     Afghanistan      Asia  1957.0   30.332   9240934.0  820.853030       AFG      4.0
    2     Afghanistan      Asia  1962.0   31.997  10267083.0  853.100710       AFG      4.0
    3     Afghanistan      Asia  1967.0   34.020  11537966.0  836.197138       AFG      4.0
    4     Afghanistan      Asia  1972.0   36.088  13079460.0  739.981106       AFG      4.0
    ...           ...       ...     ...      ...         ...         ...       ...      ...
    1699     Zimbabwe    Africa  1987.0   62.351   9216418.0  706.157306       ZWE    716.0
    1700     Zimbabwe    Africa  1992.0   60.377  10704340.0  693.420786       ZWE    716.0
    1701     Zimbabwe    Africa  1997.0   46.809  11404948.0  792.449960       ZWE    716.0
    1702     Zimbabwe    Africa  2002.0   39.989  11926563.0  672.038623       ZWE    716.0
    1703     Zimbabwe    Africa  2007.0   43.487  12311143.0  469.709298       ZWE    716.0

    [1704 rows x 8 columns]
    ```

    その他、特定のカラムがNaNであったらレコード削除する場合の`df.dropna(subset=[column_name])`や、全カラムがNaNであったらレコード削除する場合の`df.dropna(how='all)`などある

<a id="13"></a>

## 重複の処理

- `df.drop_duplicates()`：重複のレコードが存在した場合、削除する

    main.py
    ```
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
    ```

     `main.py`実行結果
    ```
              country continent    year  lifeExp         pop   gdpPercap iso_alpha  iso_num
    0     Afghanistan      Asia  1952.0   28.801   8425333.0  779.445314       AFG      4.0
    1     Afghanistan      Asia  1957.0   30.332   9240934.0  820.853030       AFG      4.0
    2     Afghanistan      Asia  1962.0   31.997  10267083.0  853.100710       AFG      4.0
    3     Afghanistan      Asia  1967.0   34.020  11537966.0  836.197138       AFG      4.0
    4     Afghanistan      Asia  1972.0   36.088  13079460.0  739.981106       AFG      4.0
    ...           ...       ...     ...      ...         ...         ...       ...      ...
    1700     Zimbabwe    Africa  1992.0   60.377  10704340.0  693.420786       ZWE    716.0
    1701     Zimbabwe    Africa  1997.0   46.809  11404948.0  792.449960       ZWE    716.0
    1702     Zimbabwe    Africa  2002.0   39.989  11926563.0  672.038623       ZWE    716.0
    1703     Zimbabwe    Africa  2007.0   43.487  12311143.0  469.709298       ZWE    716.0
    1704     Zimbabwe    Africa  2007.0   43.487  12311143.0  469.709298       ZWE    716.0

    [1705 rows x 8 columns]
            country continent    year  lifeExp         pop   gdpPercap iso_alpha  iso_num
    0     Afghanistan      Asia  1952.0   28.801   8425333.0  779.445314       AFG      4.0
    1     Afghanistan      Asia  1957.0   30.332   9240934.0  820.853030       AFG      4.0
    2     Afghanistan      Asia  1962.0   31.997  10267083.0  853.100710       AFG      4.0
    3     Afghanistan      Asia  1967.0   34.020  11537966.0  836.197138       AFG      4.0
    4     Afghanistan      Asia  1972.0   36.088  13079460.0  739.981106       AFG      4.0
    ...           ...       ...     ...      ...         ...         ...       ...      ...
    1699     Zimbabwe    Africa  1987.0   62.351   9216418.0  706.157306       ZWE    716.0
    1700     Zimbabwe    Africa  1992.0   60.377  10704340.0  693.420786       ZWE    716.0
    1701     Zimbabwe    Africa  1997.0   46.809  11404948.0  792.449960       ZWE    716.0
    1702     Zimbabwe    Africa  2002.0   39.989  11926563.0  672.038623       ZWE    716.0
    1703     Zimbabwe    Africa  2007.0   43.487  12311143.0  469.709298       ZWE    716.0

    [1704 rows x 8 columns]
    ```

    ※`df.drop_duplicates`関数に`subset`引数に`column_name`を指定すれば、その`column_name`が重複しているレコードを削除することができる

<a id="14"></a>

## インデックス・カラムの操作

- `df.rename({ column_name: new_column_name })`：カラム名をリネームする

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(df)
        print(df.rename(columns={
            "country":"国名",
            "continent":"大陸",
            "year":"西暦",
            "lifeExp":"平均寿命",
            "pop":"人口",
            "depPercap":"一人当たりGDP",
            "iso_alpha":"3文字の国コード",
            "iso_num":"数字の国コード"
        }))
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
          国名      大陸    西暦    平均寿命        人口   gdpPercap 3文字の国コード  数字の国コード
    0     Afghanistan    Asia  1952  28.801   8425333  779.445314      AFG        4
    1     Afghanistan    Asia  1957  30.332   9240934  820.853030      AFG        4
    2     Afghanistan    Asia  1962  31.997  10267083  853.100710      AFG        4
    3     Afghanistan    Asia  1967  34.020  11537966  836.197138      AFG        4
    4     Afghanistan    Asia  1972  36.088  13079460  739.981106      AFG        4
    ...           ...     ...   ...     ...       ...         ...      ...      ...
    1699     Zimbabwe  Africa  1987  62.351   9216418  706.157306      ZWE      716
    1700     Zimbabwe  Africa  1992  60.377  10704340  693.420786      ZWE      716
    1701     Zimbabwe  Africa  1997  46.809  11404948  792.449960      ZWE      716
    1702     Zimbabwe  Africa  2002  39.989  11926563  672.038623      ZWE      716
    1703     Zimbabwe  Africa  2007  43.487  12311143  469.709298      ZWE      716

    [1704 rows x 8 columns]
    ```

- `df.set_index(column_name)`：インデックスを特定のカラムに指定する

    main.py
    ```
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
                continent  year  lifeExp       pop   gdpPercap iso_alpha  iso_num
    country                                                                      
    Afghanistan      Asia  1952   28.801   8425333  779.445314       AFG        4
    Afghanistan      Asia  1957   30.332   9240934  820.853030       AFG        4
    Afghanistan      Asia  1962   31.997  10267083  853.100710       AFG        4
    Afghanistan      Asia  1967   34.020  11537966  836.197138       AFG        4
    Afghanistan      Asia  1972   36.088  13079460  739.981106       AFG        4
    ...               ...   ...      ...       ...         ...       ...      ...
    Zimbabwe       Africa  1987   62.351   9216418  706.157306       ZWE      716
    Zimbabwe       Africa  1992   60.377  10704340  693.420786       ZWE      716
    Zimbabwe       Africa  1997   46.809  11404948  792.449960       ZWE      716
    Zimbabwe       Africa  2002   39.989  11926563  672.038623       ZWE      716
    Zimbabwe       Africa  2007   43.487  12311143  469.709298       ZWE      716

    [1704 rows x 7 columns]
        index      country continent  year  lifeExp       pop   gdpPercap iso_alpha  iso_num
    0         0  Afghanistan      Asia  1952   28.801   8425333  779.445314       AFG        4
    1         1  Afghanistan      Asia  1957   30.332   9240934  820.853030       AFG        4
    2         2  Afghanistan      Asia  1962   31.997  10267083  853.100710       AFG        4
    3         3  Afghanistan      Asia  1967   34.020  11537966  836.197138       AFG        4
    4         4  Afghanistan      Asia  1972   36.088  13079460  739.981106       AFG        4
    ...     ...          ...       ...   ...      ...       ...         ...       ...      ...
    1699   1699     Zimbabwe    Africa  1987   62.351   9216418  706.157306       ZWE      716
    1700   1700     Zimbabwe    Africa  1992   60.377  10704340  693.420786       ZWE      716
    1701   1701     Zimbabwe    Africa  1997   46.809  11404948  792.449960       ZWE      716
    1702   1702     Zimbabwe    Africa  2002   39.989  11926563  672.038623       ZWE      716
    1703   1703     Zimbabwe    Africa  2007   43.487  12311143  469.709298       ZWE      716

    [1704 rows x 9 columns]
    ```

    ※インデックスをリセットする場合は、`df.reset_index()`を使用する

<a id="15"></a>

## 関数の適用

- `df[column_name].apply(function_name)`：関数を適用する

    `pop`（人口）の中央値を算出しその中央値と比較して値が大きい場合は`greater`小さい場合は`smaller`を新しいカラム`pop_median_stats`に設定する

    main.py
    ```
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
    ```

     `main.py`実行結果
    ```
              country continent  year  lifeExp       pop   gdpPercap iso_alpha  iso_num pop_median_status
    0     Afghanistan      Asia  1952   28.801   8425333  779.445314       AFG        4           greater
    1     Afghanistan      Asia  1957   30.332   9240934  820.853030       AFG        4           greater
    2     Afghanistan      Asia  1962   31.997  10267083  853.100710       AFG        4           greater
    3     Afghanistan      Asia  1967   34.020  11537966  836.197138       AFG        4           greater
    4     Afghanistan      Asia  1972   36.088  13079460  739.981106       AFG        4           greater
    ...           ...       ...   ...      ...       ...         ...       ...      ...               ...
    1699     Zimbabwe    Africa  1987   62.351   9216418  706.157306       ZWE      716           greater
    1700     Zimbabwe    Africa  1992   60.377  10704340  693.420786       ZWE      716           greater
    1701     Zimbabwe    Africa  1997   46.809  11404948  792.449960       ZWE      716           greater
    1702     Zimbabwe    Africa  2002   39.989  11926563  672.038623       ZWE      716           greater
    1703     Zimbabwe    Africa  2007   43.487  12311143  469.709298       ZWE      716           greater

    [1704 rows x 9 columns]
    ```

- `df[column_name].apply(lambda x)`：lambda関数を用いて適用する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        pop_median = df["pop"].median()
        df["pop_median_status"] = df["pop"].apply(lambda x: 'greater' if x >= pop_median else 'smaller')
        print(df)
    if __name__ == "__main__":
        main()
    ```

     `main.py`実行結果
    ```
              country continent  year  lifeExp       pop   gdpPercap iso_alpha  iso_num pop_median_status
    0     Afghanistan      Asia  1952   28.801   8425333  779.445314       AFG        4           greater
    1     Afghanistan      Asia  1957   30.332   9240934  820.853030       AFG        4           greater
    2     Afghanistan      Asia  1962   31.997  10267083  853.100710       AFG        4           greater
    3     Afghanistan      Asia  1967   34.020  11537966  836.197138       AFG        4           greater
    4     Afghanistan      Asia  1972   36.088  13079460  739.981106       AFG        4           greater
    ...           ...       ...   ...      ...       ...         ...       ...      ...               ...
    1699     Zimbabwe    Africa  1987   62.351   9216418  706.157306       ZWE      716           greater
    1700     Zimbabwe    Africa  1992   60.377  10704340  693.420786       ZWE      716           greater
    1701     Zimbabwe    Africa  1997   46.809  11404948  792.449960       ZWE      716           greater
    1702     Zimbabwe    Africa  2002   39.989  11926563  672.038623       ZWE      716           greater
    1703     Zimbabwe    Africa  2007   43.487  12311143  469.709298       ZWE      716           greater

    [1704 rows x 9 columns]
    ```

<a id="16"></a>

## groupby

- `df.groupby(column_name).get_group(column_value)`：カラム名の特定の値でグループ集計する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        continent_grp = df.groupby("continent")
        print(continent_grp.get_group("Asia"))
    if __name__ == "__main__":
        main()
    ```

     `main.py`実行結果
    ```
              country continent  year  lifeExp       pop    gdpPercap iso_alpha  iso_num
    0     Afghanistan      Asia  1952   28.801   8425333   779.445314       AFG        4
    1     Afghanistan      Asia  1957   30.332   9240934   820.853030       AFG        4
    2     Afghanistan      Asia  1962   31.997  10267083   853.100710       AFG        4
    3     Afghanistan      Asia  1967   34.020  11537966   836.197138       AFG        4
    4     Afghanistan      Asia  1972   36.088  13079460   739.981106       AFG        4
    ...           ...       ...   ...      ...       ...          ...       ...      ...
    1675  Yemen, Rep.      Asia  1987   52.922  11219340  1971.741538       YEM      887
    1676  Yemen, Rep.      Asia  1992   55.599  13367997  1879.496673       YEM      887
    1677  Yemen, Rep.      Asia  1997   58.020  15826497  2117.484526       YEM      887
    1678  Yemen, Rep.      Asia  2002   60.308  18701257  2234.820827       YEM      887
    1679  Yemen, Rep.      Asia  2007   62.698  22211743  2280.769906       YEM      887

    [396 rows x 8 columns]
    ```

- `df.groupby(column_name)[column_name].median().reset_index()`：特定のカラムの中央値を算出し特定のカラム名でグルーピングする

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        continent_grp = df.groupby("continent")
        print(continent_grp["pop"].median().reset_index())
    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
      continent         pop
    0    Africa   4579311.0
    1  Americas   6227510.0
    2      Asia  14530830.5
    3    Europe   8551125.0
    4   Oceania   6403491.5
    ```

- `df.groupby(column_name)[column_name_a,column_name_b].agg({column_name_a:"median", column_name_b:"mean"}).reset_index()`：あるカラムには中央値を算出し、あるカラムは平均値を算出し、特定のカラム名でグルーピングする

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        continent_grp = df.groupby("continent")
        print(continent_grp[["pop", "gdpPercap"]].agg({"pop":"median","gdpPercap":"mean"}).reset_index())
    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
      continent         pop     gdpPercap
    0    Africa   4579311.0   2193.754578
    1  Americas   6227510.0   7136.110356
    2      Asia  14530830.5   7902.150428
    3    Europe   8551125.0  14469.475533
    4   Oceania   6403491.5  18621.609223
    ```

<a id="17"></a>

## pivot table

クロス集計する際にpivot tableを用いる

- `pd.pivot_table(index=[column_name] columns=[column_name] value=[column_name], aggfunc=function_name)`：インデックス（行）を`year`に、カラム（列）を`continent`で、`pop`の平均値をクロス集計する

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        print(pd.pivot_table(df, index=["year"], columns=["continent"], values=["pop"], aggfunc="mean"))
    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
                        pop                                                     
    continent        Africa     Americas          Asia        Europe     Oceania
    year                                                                        
    1952       4.570010e+06  13806097.84  4.228356e+07  1.393736e+07   5343003.0
    1957       5.093033e+06  15478156.64  4.735699e+07  1.459635e+07   5970988.0
    1962       5.702247e+06  17330810.16  5.140476e+07  1.534517e+07   6641759.0
    1967       6.447875e+06  19229864.92  5.774736e+07  1.603930e+07   7300207.0
    1972       7.305376e+06  21175368.40  6.518098e+07  1.668784e+07   8053050.0
    1977       8.328097e+06  23122707.96  7.225799e+07  1.723882e+07   8619500.0
    1982       9.602857e+06  25211636.80  7.909502e+07  1.770890e+07   9197425.0
    1987       1.105450e+07  27310158.84  8.700669e+07  1.810314e+07   9787207.5
    1992       1.267464e+07  29570964.16  9.494825e+07  1.860476e+07  10459825.5
    1997       1.430448e+07  31876016.40  1.025238e+08  1.896480e+07  11120715.0
    2002       1.603315e+07  33990910.48  1.091455e+08  1.927413e+07  11727414.5
    2007       1.787576e+07  35954847.36  1.155138e+08  1.953662e+07  12274973.5
    ```

- `pd.pivot_table().divide()`：クロス集計した`pop`の平均値を`year`においての割合を求める

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df = px.data.gapminder()
        pop_pivot = pd.pivot_table(df, index=["year"], columns=["continent"], values=["pop"], aggfunc="mean")
        print(pop_pivot.divide(pop_pivot.sum(axis=1), axis=0) * 100)
    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
                    pop                                           
    continent    Africa   Americas       Asia     Europe   Oceania
    year                                                          
    1952       5.716798  17.270569  52.894097  17.434772  6.683764
    1957       5.755132  17.490330  53.513435  16.493882  6.747221
    1962       5.913676  17.973404  53.310755  15.914142  6.888023
    1967       6.039337  18.011461  54.088488  15.023049  6.837666
    1972       6.169945  17.884208  55.050289  14.094145  6.801413
    1977       6.427632  17.846125  55.768773  13.304934  6.652537
    1982       6.819444  17.903979  56.169122  12.575927  6.531528
    1987       7.212828  17.819298  56.770016  11.811913  6.385945
    1992       7.623459  17.786143  57.108828  11.190265  6.291305
    1997       8.000724  17.828765  57.343199  10.607318  6.219993
    2002       8.430908  17.873854  57.393319  10.135150  6.166769
    2007       8.886520  17.874115  57.424973   9.712175  6.102217
    ```

<a id="18"></a>

## ファイル読み込み

- `pd.read_csv(file_path, sep=',' usecols=[1,2,3])`：CSVファイルを特定のカラムのみ読み込む

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        file_path = "./dataset/countries_codes_and_coordinates.csv"
        df = pd.read_csv(file_path, sep=",", usecols=[2,4,5])
        for col in df.columns:
            df[col] = df[col].apply(lambda x: x.strip()[1:-1])
        print(df)
    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
        Alpha-3 code Latitude (average) Longitude (average)
    0            AFG                 33                  65
    1            ALB                 41                  20
    2            DZA                 28                   3
    3            ASM           -14.3333                -170
    4            AND               42.5                 1.6
    ..           ...                ...                 ...
    251          WLF              -13.3              -176.2
    252          ESH               24.5                 -13
    253          YEM                 15                  48
    254          ZMB                -15                  30
    255          ZWE                -20                  30

    [256 rows x 3 columns]
    ```

<a id="19"></a>

## merge

２つデータフレームを結合させる

- `pd.merge(data_frame_1, data_frame_2, left_on=data_frame_1_column, right_on=data_frame_1_column), how="inner`：２つのデータフレーム`df`と`df_gapminder`を`Alpha-3 code`と``iso_alpha`をキーに内部結合させる

    main.py
    ```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    def main():
        df_gapminder = px.data.gapminder()
        file_path = "./dataset/countries_codes_and_coordinates.csv"
        df = pd.read_csv(file_path, sep=",", usecols=[2,4,5])
        for col in df.columns:
            df[col] = df[col].apply(lambda x: x.strip()[1:-1])
        print(pd.merge(df_gapminder, df, left_on="iso_alpha", right_on="Alpha-3 code", how="inner"))

    if __name__ == "__main__":
        main()
    ```

    `main.py`実行結果
    ```
            country continent  year  lifeExp       pop  ...  iso_alpha iso_num  Alpha-3 code Latitude (average) Longitude (average)
    0     Afghanistan      Asia  1952   28.801   8425333  ...        AFG       4           AFG                 33                  65
    1     Afghanistan      Asia  1957   30.332   9240934  ...        AFG       4           AFG                 33                  65
    2     Afghanistan      Asia  1962   31.997  10267083  ...        AFG       4           AFG                 33                  65
    3     Afghanistan      Asia  1967   34.020  11537966  ...        AFG       4           AFG                 33                  65
    4     Afghanistan      Asia  1972   36.088  13079460  ...        AFG       4           AFG                 33                  65
    ...           ...       ...   ...      ...       ...  ...        ...     ...           ...                ...                 ...
    1807     Zimbabwe    Africa  1987   62.351   9216418  ...        ZWE     716           ZWE                -20                  30
    1808     Zimbabwe    Africa  1992   60.377  10704340  ...        ZWE     716           ZWE                -20                  30
    1809     Zimbabwe    Africa  1997   46.809  11404948  ...        ZWE     716           ZWE                -20                  30
    1810     Zimbabwe    Africa  2002   39.989  11926563  ...        ZWE     716           ZWE                -20                  30
    1811     Zimbabwe    Africa  2007   43.487  12311143  ...        ZWE     716           ZWE                -20                  30

    [1812 rows x 11 columns]
    ```