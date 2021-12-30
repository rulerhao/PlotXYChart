import plotly.express as px
import pandas as pd

# Read data from txt file.
fileName = 'data/5300.txt'
f = open(fileName, 'r')
str2 = f.read().split()
f.close

dataArr = [int(numeric_string) for numeric_string in str2]  # Make string array to int array
xAxisValue = [element for element in range(len(str2))] # Generate XAxis value according to dataArr.index

mDict = {
    "x": xAxisValue,
    "y": dataArr
}

df = pd.DataFrame(dict(mDict))

fig = px.line(df, x="x", y="y", title="Input")
fig.show()
