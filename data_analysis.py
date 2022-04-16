import numpy as np
import pandas as pd

#print dataframe statistics
def dfInfo(df):
    print(df.describe(include="all").to_string())
    print(df.info())
    print(df.dtypes())

#get a list of all empty columns in a dataframe
def getEmptys(df):
    f