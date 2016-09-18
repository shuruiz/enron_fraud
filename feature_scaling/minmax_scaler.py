#!/usr/bin/python

from sklearn.preprocessing import MinMaxScaler
import numpy

weights=numpy.array([[115.],[156.],[148.]]) #floating numbers required
scaler=MinMaxScaler()
rescaler_weight=scaler.fit_transform(weights)#2 steps inside 1.find min or max 2.transform

print rescaler_weight