import numpy as np
import pandas as pd

###treats each row as its own object, with each column as an object property.
### Allows for more advanced logic on a row by row basis
###expected usage: df["New Column"] =dF.apply(rowLogic,axis = 1)
###Axis denotes horizontal
def rowLogic(row):
    #ex:
    if(row['Column Name']== 'something'):
        return 'something else'
    else:
        return None


def filterDF(df):
    outputData = df[df['Column Name']=='some value']
    return outputData

#takes dataframe, list of columns, and scaleType as string
def normalization(df, scaleType ='',dfColumns=[]):
    #print("NORMALIZING...")
    if len(dfColumns)==0:
        dfColumns=df.columns.to_list()

    #print(scaleType)
    #print(type(dfColumns))

    for dfColumn in dfColumns:
        print(dfColumn)
        if(df[dfColumn].dtype==np.float_ or df[dfColumn].dtype==np.int64):
            print(dfColumn)
            print(df[dfColumn])
            print(df[dfColumn].dtype)
            old = df[dfColumn]
            min = df[dfColumn].min()
            max = df[dfColumn].max()
            mean = df[dfColumn].mean()
            std = df[dfColumn].std()

            values = old
            #print(df[dfColumn].min(),df[dfColumn].max(),df[dfColumn].mean(),df[dfColumn].std())
            print(min,max,mean,std)
            #rescaling to consistent range between 1 and 0
            if scaleType=='SFS':
                #range 0:1
                values = old/max

            if scaleType=='Min-Max':
                #range 0:1
                values = (old-min)/(max-min)

            if scaleType== 'ZSCORE':
                #range ~ -3:3
                values = (old - mean)/std

            if scaleType == 'Mean Normalization':
                #range 0:1
                values = (old-mean)/(max-min)


            df[dfColumn] = values

        else:
            print("NOT NORMALIZING, COLUMN IS dtype:",df[dfColumn].dtype)
        print("COMPLETE---------------------------------------------------------------")
    return df

#takes a dataframe as an argument, removes the empty columns and returns the dataframe
def removeEmptyColumns(df):
    outputDf = df
    for i in outputDf.columns.to_list():
        if outputDf[i].dropna().empty:
            print(i,'IS EMPTY')
            outputDf=outputDf.drop(i,axis=1)
        else:
            print(i,'IS NOT EMPTY')
    return outputDf

def emptyTest():
    dfColumns = np.nan
    dfColumns = None
    dfColumns = ''
    if dfColumns:
        print('Has Value', dfColumns)
    else:
        print('Is Empty', dfColumns)
    print(dfColumns == np.nan)
    print(dfColumns == None)
    print(dfColumns == '')

def dataFormatting(df,subset, dataType):
    outputDf = df
    outputDf[subset]=outputDf[[subset]].astype(dataType)
    return outputDf

#creates a new column with binned values
#binNum = number of subcategories to create
#group names is the names of the new subcategories
def binning(df,binNums,columnName,group_names):
    subset = columnName
    bins = np.linspace(min(df[subset]),max(df[subset]),binNums)
    newColName = subset+'-binned'
    df[newColName]=pd.cut(df[subset],bins,labels=group_names,include_lowest=True)
    #print(df)
    return df

#creates new columns for each unique value with either a 1 or 0 as the value
def categorize(df,subset):
    df = pd.get_dummies(df[subset])

    return df

def filterDF(df):
    outputData = df[df['Column Name']=='some value']
    return outputData
#process missing values
def missingValues(df,dfColumns = [],method="drop",replaceIn=np.NAN,replaceOut=''):

    if len(dfColumns)==0:
        dfColumns=df.columns.to_list()

    for dfColumn in dfColumns:
        if(method=="drop"):
            df= df.dropna(subset=[dfColumn],axis = 0)

        if(method=='replace'):
            df[dfColumn]= df[dfColumn].replace(replaceIn,replaceOut)

    return df

def df_columns_to_float(df,dfColumns =[]):
    if len(dfColumns)==0:
        dfColumns=df.columns.to_list()
    if type(dfColumns) == type([]):
        for dfColumn in dfColumns:
            try:
                df[dfColumn] = df[dfColumn].astype('float')
                #df[dfColumn] = df[dfColumn].replace(np.nan, df[i].mean())
            except:
                #print("NOT A FLOAT")
                x = 1


    return df

#change a column type:
#df['Column] = df['Column'].astype('type')
#df1=df.replace('?',np.NaN)
#df=df1.dropna(subset=["price"], axis=0)