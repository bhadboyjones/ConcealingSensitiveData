import sys
import numpy as np
import pandas as pd
import random

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

sensitive_dataset = 'sensitive_data.xlsx'
df1 = pd.read_excel(sensitive_dataset , sheet_name='data', skiprows=1, index_col='Unnamed: 0')
# print(df1)

print(df1.shape)
#print(list(enumerate(df1.columns)))
#print(list(enumerate(df1.index)))

df1 = df1.iloc[:85, :5]
#print(df1)
print(df1.shape)
np.prod(df1.shape)
df2 = df1.copy()

# here it works
#random.seed(12)
#print(random.random())
x = random.random()
#print(x)

# f0r loop to generate a random number everytime
random.seed(40)

for index in df1.index:
    for column in df1.columns:

        x = df1.loc[index, column]
        print(f'\n\n*index: {index}, column: {column} -->x={x}')

        if (x != 'x') & (x != '..') & (x != 0) and type(x) == int:

            if x>0:
                df2.loc[index, column] = random.sample(range(x, 2*x), 1)[0]
                # df2.loc[index, column] = np.random.randint(x, 2*x)
                print(f'-------> NOW, since x>0, it is x={df2.loc[index, column]}')

            else:
                df2.loc[index, column] = random.sample(range(2*x, x), 1)[0]
                # df2.loc[index, column] = np.random.randint(2*x,x)
                print(f'-------> NOW, since x<0, it is x={df2.loc[index, column]}')


print(df1)
print(df2)

writer = pd.ExcelWriter('new_dataset.xlsx', engine='xlsxwriter')
print(df1.to_excel(writer, sheet_name='v1'))
print(df2.to_excel(writer, sheet_name='v2'))