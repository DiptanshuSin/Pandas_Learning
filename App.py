import pandas as pd

#read data from CSV file into a dataframe
df = pd.read_csv("sales_data_sample.csv", encoding="latin1")
print(df)


#use of head and tail. If no number entered first 5 will be provided
print('Display first 10', df.head(10))
print('Display last 10', df.tail(10))


#info method gives no. of rows and columns ,  names of columns, data types 
print(df.info())

print(df.describe())
print(df.columns)
print(df.shape)

# #Specific column selection and filter rows  and combine multiple rows
# columnOnlyOneselection = df[]
print('Column Name only one')
print(df['ORDERNUMBER'])
print('Column Name multiple')
# print(df["ORDERNUMBER","MSRP"])
subset = df[['ORDERNUMBER','PRICEEACH']]
print(subset)

#filter rows
rowFilter = df[df['PRICEEACH']> 97 ]
print('Row Filteration')
print(rowFilter)
print('count')
print(rowFilter.count())