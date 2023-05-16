import pandas as pd
import xlrd

# To create dataframe from excel file
df = pd.read_excel("D:\\sampledata.xlsx", "Sheet1")
print(df)

# To create dataframe from csv file
# dfcsv = pd.read_csv("D:\\sampledata.csv")
# print(dfcsv)

# Operations on dataframe
# To determine number of rows and columns
shape = df.shape
print(shape)  # rows and columns

# To access row and columns
r, c = df.shape
print("Rows: ", r)
print("Columns", c)

# to get first N rows
top3 = df.head(3)
print(top3)

# to get last N rows
last2 = df.tail(2)
print(last2)

# to retrieve range of records
rn = df[2:4]
print(rn)

# To get column names
print("Column Names using df.columns")
cols = df.columns
print(cols)

# to retrive content for a particular column
print(df.Name)
# to retrive selected columns
print("To retrieve selected columns")
selcols = df[['Name', 'Salary']]
print(selcols)

# To find minimum and maximum
print("Minimum and Maximum Salary")
min = df['Salary'].min()
print("Minimum Salary is ", min)
max = df['Salary'].max()
print("Maximum Salary is", max)

# To get statistical details
print("Statistical details")
statDetails = df.describe()
print(statDetails)

# Querying datas
print("Display records having salary > 5000")
queryresult = df[df.Salary > 5000]
print(queryresult)

# display record who are getting minumum salary
print("Display records having Mininum Salary")
queryresult = df[df.Salary == df.Salary.min()]
print(queryresult)

# display record who are getting maximum salary
print("Display records having Maximum Salary")
queryresult = df[df.Salary == df.Salary.max()]
print(queryresult)

# display employee name and salary having salary >5000
queryresult = df[['Name', 'Salary']][df.Salary > 5000]
print(queryresult)

# Sort by Salary
dfbysal = df.sort_values('Salary')
print(dfbysal)

# Sort by Salary in descending order
dfbysal = df.sort_values('Salary', ascending=False)
print(dfbysal)

# Handling missing values/data
# df1=df.fillna(0)
# print(df1)

df1 = df.fillna({'Designation': 'N/A',  'Commission': 0})
print(df1)

#To remove missing data
dffullrecordsonly = df.dropna()
print(dffullrecordsonly)

#to locate particular row
row0 = df.loc[0]
print(row0)

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
dfdata = pd.DataFrame(data)

print(dfdata)

