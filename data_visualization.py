import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd



def chart(df, xLabel,xData,yLabel,yData,chartType='',chartTitle=''):
    if(chartType=='scatter'):
        x =xData
        y = yData
        plt.scatter(x=x, y=y)
        print(xData.name)

        plt.title(chartTitle)
        plt.xlabel(xlabel= xLabel)
        plt.ylabel(ylabel=yLabel)
        plt.show()

    if (chartType=='regplot'):
        sns.regplot(x=xData.name,y=yData.name,data=df)
        plt.ylim(0,)
        plt.show()
