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
            print(dfColumn, 'NORMALIZING!!!')
            #print(dfColumn)
            #print(df[dfColumn])
            print(df[dfColumn].dtype)

            min = df[dfColumn].min()
            max = df[dfColumn].max()
            mean = df[dfColumn].mean()
            std = df[dfColumn].std()
            
            #print(df[dfColumn].min(),df[dfColumn].max(),df[dfColumn].mean(),df[dfColumn].std())
            print(min,max,mean,std)
            if scaleType=='SFS':
                #range 0:1

                print(df[dfColumn])
                    #print(df[dfColumn].to_string())
                    #print('values',df[dfColumn]/max)

                values = df[dfColumn]/max
                    #print(values)
                df[dfColumn] = values

            if scaleType=='Min-Max':
                #range 0:1

                df[dfColumn] = (df[dfColumn]-df[dfColumn].min())/(df[dfColumn].max()-df[dfColumn].min())

            if scaleType== 'ZSCORE':
                #range ~ -3:3
                df[dfColumn] = (df[dfColumn] - df[dfColumn].mean())/df[dfColumn].std()
            print(dfColumn, 'NORMALIZED')

        else:
            print("NOT NORMALIZING, COLUMN IS dtype:",df[dfColumn].dtype)
        print("COMPLETE---------------------------------------------------------------")
    return df

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

def binning(df,binNums,subset,group_names):
    print('BINNING')
    bins = np.linspace(min(df[subset]),max(df[subset]),binNums)
    newColName = subset+'-binned'
    df[newColName]=pd.cut(df[subset],bins,labels=group_names,include_lowest=True)
    print(df)
    return df

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

#change a column type:
#df['Column] = df['Column'].astype('type')
#df1=df.replace('?',np.NaN)
#df=df1.dropna(subset=["price"], axis=0)