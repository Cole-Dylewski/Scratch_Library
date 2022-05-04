import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures



def simple_linear_regression(df,features=[],label = ''):
    #create the linear regression object
    lm = LinearRegression()
    x= df[features]
    y = df[label]
    lm.fit(x,y)
    return

def polynomial_regression(feature='', lable='', order = 0):
    if order <2:
        f = np.polyfit(feature,lable,order)
        p = np.poly1d(f)
        print(p)
    else:
        pr = PolynomialFeatures(degree=order, include_bias=False)
        x_polly = pr.fit_transform(feature)

    return