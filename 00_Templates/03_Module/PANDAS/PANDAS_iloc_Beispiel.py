# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html
import pandas as pd #(Pandas ist so etwas wie excel in Pyhton)
mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
          {'a': 100, 'b': 200, 'c': 300, 'd': 400},
          {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000}]

df = pd.DataFrame(mydict)
print(df)


a = df.iloc[0]
print(a)
print(type(df.iloc[0]))

b = df.iloc[0]["a"]
print(b)