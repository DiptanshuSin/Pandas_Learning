import pandas as pd
data = {
    "NAME" : ['RAM', 'SHYAM', 'RAVI', 'ADITI', 'GG', 'DS', 'BGT'],
    "AGE" : [25,35,22,34,45,34,22],
    "SALARY" : [35000,45000,37000,43000,37800,55410,43090],
    
}

df = pd.DataFrame(data)
print(df)

df.insert(3, "Bonus", [2,3,2,5,1,3,5])
df["BonusAmount"] = df['SALARY'] * df['Bonus']

print(df)

'''
updating elements
.loc[]
'''

df.loc[2, "BonusAmount"] = 75000
print(df)

'''
Nan & None & isnull()
'''
data2 = {
    "NAME" : ['RAM', None, 'RAVI', 'ADITI', 'GG', 'DS', 'BGT'],
    "AGE" : [25,None,22,34,45,34,22],
    "SALARY" : [35000,None,37000,43000,37800,55410,43090],
    
}

df2 = pd.DataFrame(data2)
print(df2.isnull().sum())

'''Handle data
'''

# df2.dropna(axis=0, inplace=True)
# print(df2)

df2.fillna(0, inplace=True)
print(df2)