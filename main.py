# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import plotly.express as px
import pandas as pd
from random import randrange


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


fileName = 'C:/Users/jake/Desktop/耳機孔測試/m8/test.txt'
f = open(fileName, 'r')
str2 = f.read().split()
f.close

dataArr = [int(numeric_string) for numeric_string in str2]  # string array to int array
xAxisValue = [element for element in range(len(str2))]

print(xAxisValue)
print(dataArr)
mDict = {
    "x": xAxisValue,
    "y": dataArr
}

df = pd.DataFrame(dict(mDict))

fig = px.line(df, x="x", y="y", title="Input")
fig.show()
