import pandas as pd
# don't use loops for this exercise

data_url = 'http://bit.ly/2cLzoxH'
df = pd.read_csv(data_url)

values = df.lifeExp * df.gdpPercap

df['Values'] = values

# print entire data frame (pycharm will not show all but they are there)
#print(df)

# print row if year 2002
#print(df[df.year == 2002])

# print row if year 2002 or 1952
subsetDataFrame = df[df['year'].isin([2002, 1952])]
#print(subsetDataFrame)


# gdp in australia in 2007
subdf = df[df['country'].isin(["Australia"])]
subdf1 = subdf[subdf['year'].isin([2007])]
val = float(subdf1.lifeExp)
#print(val)

# stats describing life expectancy in australia over the years
aussies = df[df['country'].isin(["Australia"])]
print(aussies.lifeExp.describe())




