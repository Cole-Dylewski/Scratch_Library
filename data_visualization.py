import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd



def chart(df, xLabel,xData,yLabel,yData,chartType='',chartTitle=''):
    if chartType== 'scatter':
        x =xData
        y = yData
        plt.scatter(x=x, y=y)



    if chartType=='regplot':
        sns.regplot(x=xData.name,y=yData.name,data=df)
        plt.ylim(0,)

    if chartType == 'boxplot':
        x = xData
        y = yData
        sns.set_style("whitegrid")
        sns.boxplot(x=xData,y=yData,data = df)

    plt.title(chartTitle)
    plt.xlabel(xlabel=xLabel)
    plt.ylabel(ylabel=yLabel)
    plt.show()