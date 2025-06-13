import pandas as pd
data = {
    "Name": ['Ram','Shyam','KK'],
    "Age": [10,20,30],
    "City": ['Nagpur','City2','City3']

}
df = pd.DataFrame(data)
print(df)

df.to_csv("ExcelDataSave.csv", index=False)

print(df.describe())
print(df.columns)
print(df.shape)
