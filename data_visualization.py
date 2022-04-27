import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


def chart(df, xLabel,xData,yLabel,yData,chartType='',chartTitle=''):
    if chartType== 'scatter':
        x = xData
        y = yData
        plt.scatter(x=x, y=y)


    #describes the data to identify proper model
    if chartType=='regplot':
        sns.regplot(x=xData.name,y=yData.name,data=df)
        plt.ylim(0,)

    if chartType == 'boxplot':
        x = xData
        y = yData
        sns.set_style("whitegrid")
        sns.boxplot(x=xData,y=yData,data = df)

    if chartType == 'heatmap':
        x = xData
        y = yData
        fig, ax = plt.subplots()
        im = ax.pcolor(df, cmap='RdBu')

        # label names
        row_labels = df.columns.levels[1]
        col_labels = df.index

        # move ticks and labels to the center
        ax.set_xticks(np.arange(df.shape[1]) + 0.5, minor=False)
        ax.set_yticks(np.arange(df.shape[0]) + 0.5, minor=False)

        # insert labels
        ax.set_xticklabels(row_labels, minor=False)
        ax.set_yticklabels(col_labels, minor=False)

        # rotate label if too long
        plt.xticks(rotation=90)

        fig.colorbar(im)

    #predicted vs actual
    if chartType == 'distribution':
        print()
    #helps identify if there is a curve to the data to update regression decisions
    if chartType == 'residual':
        print()

    #compare model to actual data
    if chartType == 'mean squared error':
        print()

    plt.title(chartTitle)
    plt.xlabel(xlabel=xLabel)
    plt.ylabel(ylabel=yLabel)
    plt.show()