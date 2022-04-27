import numpy as np
import pandas as pd
import statistics as stats
import scipy

#print dataframe statistics
def dfInfo(df):
    print(df.describe(include="all").to_string())
    print(df.info())
    print(df.dtypes())

#get a list of all empty columns in a dataframe
def print_missing_data(df):
    missing_data = df.isnull()
    for column in missing_data.columns.values.tolist():
        print(column)
        print(missing_data[column].value_counts())
        print("")

#Pearson Correlation
# scale of -1 to 1
# -1 = large negative correlation
# 1 = Large positive correlation
# 0 = no Relationship

def get_pearson_corr(df,feature,label):

    pearson_coef, p_value = stats.pearsonr(feature,label)
    return pearson_coef, p_value


def chi_square():

    return

def cross_corr(df):

    return df.corr()

def get_unique_values(df,dfColumn):
    return df[dfColumn].unique()