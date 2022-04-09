import pandas as pd
import numpy as np
import random
import csv
import openpyxl as op
import tkinter.filedialog as fd
import os
from csv import writer
from os import listdir
from os.path import isfile
import xlrd
from tkinter import *
from tkinter import ttk

#test

#takes 2 columns, turns into a dictionary with 1st / 2nd column as Key / Value
### Can be used to create xlats
def dataframeColumnsToDict(dfCol1,dfCol2):
    keyList = dfCol1.to_list()
    valueList = dfCol2.to_list()
    return{keyList[i]: valueList[i] for i in range(len(keyList))}

### takes a source file with full path converts to dictionary with key and dataframe
##
def convertFileToDF(sourceFile, sourceDirectory='',good2go = True):
    if(sourceDirectory==''):
        sourceDirectory=os.path.dirname(sourceFile)
    ###If the data is already in a traditional table format, set below value to true
    if(good2go):
        inputData=[]
        name, ext = os.path.splitext(sourceFile)
        print("Name = ", name)
        print('EXT = ', ext)
        if (ext == '.csv'):
            #print('CSV')
            inputData = pd.read_csv(sourceFile, dtype= str, low_memory=False)

        if (ext == '.xlsx'):
            #print('XLSX')
            #inputData = pd.read_excel(sourceFile, dtype= str,low_memory=False)
            inputData=pd.read_excel(sourceFile, dtype= str,sheet_name=None)
        return inputData
    else:
        #first select the whole book
        wb = op.load_workbook(sourceFile,read_only=True)
        #then select a sheet from within the book,
        ws = wb['Sheet Name']
        data_rows=[]
        #select rows and columns in traditional excel style ie:['A3':'D20']
        for row in ws['Top left cell':'Bottom Right Cell']:
            ### now it loops through each row, and starts building a giant list to form the dataframe
            data_cols=[]
            for cell in row:
                data_cols.append(cell.value)
                #print(data_cols)
            data_rows.append(data_cols)
        df=pd.DataFrame(data_rows[1:len(data_rows)],columns=data_rows[0])
        #print(df.head(20).to_string())
        return df


###Saves a dataframe to either a .xlsx or .csv.
###If no name is provided, it will prompt the user for one.
def file_save(df,saveName = ''):
    ###check if name is given when function is called, if no name then a prompt will be given
    if (saveName ==''):
        saveName = fd.asksaveasfilename(defaultextension='.csv',filetypes=(("Excel files", "*.xlsx"),('Comma Seperated File',"*.csv") ))
    print(saveName)
    name, ext = os.path.splitext(saveName)
    if (ext == '.csv'):
        df.to_csv(saveName,index=False)
    if (ext == '.xlsx'):
        df.to_excel(saveName,index=False)
    print("File Saved: ",saveName )
#takes array dataframes, and concatenates them
def concatFiles(arrayOfDFs):
    return pd.concat(arrayOfDFs,ignore_index=True)

###Merge 2 Dataframes, similar to a SQL join, select the join type and where matches
def mergeDFs(mergerMasterDf,toBeMergedDf):
    mergerMasterDf = pd.merge(
        mergerMasterDf,
        toBeMergedDf,
        how="left",### will accept‘left’, ‘right’, ‘outer’, ‘inner’, ‘cross’, default ‘inner’
        on= ['List of Columns to be merged on']
    )

    return mergerMasterDf

### Limits data output based on checking each row in a column against a logic check
def filterDF(inputData):
    outputData = inputData[inputData['Column Name']=='some value']
    return outputData

###Prints data for observation
def printDataStructure(inputData):
    print(type(inputData))
    ### if data is a straight up Dataframe, just print out the dataframe
    if(type(inputData)==pd.DataFrame):
        print(inputData.head(10).to_string())
    ### if data is a traditional dictionary with keys / Datframes. Print out each dataframe individually
    if(type(inputData)== dict):
        if (len(inputData)>0):
            print(inputData.keys())
            for sheet_name, sheet_data in inputData.items():
                print(sheet_name, sheet_data)
                print(sheet_data.head(10).to_string())

    return



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


### code to perform a pivot, and force some vertical columns into a Horizontal format
def pivotTable(df):
    ### isolate the old headers, and the column you want to be the additional headers with the values pivoted on
    df = df.pivot(index=['Some list of all the columns you dont want touched'], columns='Column to pivot on, will become the additional headers')
    ### the output will have a bunch of sub headers corresponding to each additional column, we need to select the one column we want to keep
    df=df['value column name'].reset_index()
    return df


### takes a dataframe, sets some columns as
def meltTable(df):
    return pd.melt(df, id_vars=['List of Columns to remain untouched'], var_name='Code', value_name='Values')

### Performs translate comparison and output
### Will compare a column to a translate, and output the corresponding value
def dictCompareKey2Value(df,xlat):
    ### this will take the old column
    df['New Column or old column to overwrite'] = df['comparison column'].map(xlat)
    return df

def readTxtFile(sourceFile,sourceDirectory=''):
    if(sourceDirectory==''):
        sourceDirectory=os.path.dirname(sourceFile)
    fileName = sourceDirectory+r'/'+sourceFile
    print(fileName)
    file = open(fileName, "r")
    lines = (file.readlines())
    print(lines)
    return lines

#takes a dictionary and converts it to a dataframe with the keys as columns
def convertDict2DF(items):
    return pd.DataFrame({k: [v] for k, v in items})

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
def readCSVfromPath():
    path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'
    df = pd.read_csv(path, header=None)
    print(df)

#takes dataframe, list of columns, and scaleType as string
def scaleData(df,dfColumns='',scaleType=''):
    if dfColumns=='':
        dfColumns=df.columns.to_list()

    if scaleType=='SFS':
        for dfColumn in dfColumns:
            df[dfColumn]= df[dfColumn]/df[dfColumn].max()

    if scaleType=='Min-Max':
        for dfColumn in dfColumns:
            df[dfColumn] = (df[dfColumn]-df[dfColumn].min())/(df[dfColumn].max()-df[dfColumn].min())
    if scaleType== 'ZSCORE':
        for dfColumn in dfColumns:
            df[dfColumn] = (df[dfColumn] - df[dfColumn].mean())/df[dfColumn].std()

    return df


    return 0

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

#prints a list with a index
def printListWCount(enList,counterStart=None):
    if counterStart== None:
        for count, ele in enumerate(enList):
            print (count,ele)
    else:
        for count, ele in enumerate(enList,counterStart):
            print (count,ele)

def binColumn(df, columnName, binNum,groupNames):
    bins = np.linspace(
        min(df[columnName]),
        max(df[columnName]),
        binNum
    )
    df[columnName]=pd.cut(
        df[columnName],
        bins,
        labels=groupNames,
        include_lowest=True
    )
    return df

#change a column type:
#df['Column] = df['Column'].astype('type')
#df1=df.replace('?',np.NaN)
#df=df1.dropna(subset=["price"], axis=0)

### STARTING POINT!

###If you need just a file
sourceFile = fd.askopenfilename()
#sourceFile=r''
print(sourceFile)
df = convertFileToDF(sourceFile)
print(df)
###If you need a directory
sourceDirectory =fd.askdirectory()
#sourceDirectory=r''
print(sourceDirectory)
sourceFiles = listdir(sourceDirectory)
print(sourceFiles)
for sourceFile in sourceFiles:
    print(sourceFile)
    df = convertFileToDF(sourceFile)

printDataStructure(df)

