#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 17:24:42 2017

@author: Anna Laman
"""

from flask import Flask, request
from flask import render_template
import csv
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("fin_data_news_app2.csv")


#Here we subset the data for the medium range view
df2 = df[df.DJIA_INC == True]
df2 = df2[df2.NIKKEI225_INC == True]
df2 = df2[df2.IPCMexicoOpen_INC == True]
df2 = df2[df2.MervalAregentinaOpen_INC == True]
df2 = df2[df2.CanadaTSXOpen_INC == True]

csv_list = df.T.to_dict().values()

csv_list_medium = df2.T.to_dict().values()


@app.route('/', methods=['GET', 'POST'])
def index():
    return ('This is the homepage for the financial webpage. Please add data_wide, data_medium, or data_narrow to get the views.')

#This contains all of the daily data from 2003 onwards
@app.route('/data_wide', methods=['GET', 'POST'])
def data_wide():
    return render_template("main.html", csv_list=csv_list)

#This contains all of the daily data from 2003 onwards where both the DJIA, Nikkei, IPC Mexico, Merval, and Canadian Indices increased
@app.route('/data_medium', methods=['GET', 'POST'])
def data_medium():
    return render_template("main2.html", csv_list=csv_list_medium)

#This contains all of the daily data from 2003 onwards for only US assets
@app.route('/data_narrow', methods=['GET', 'POST'])
def data_narrow():
    return render_template("main3.html", csv_list=csv_list)

#We can see that as we go from wide to narrow, there are less and less data points for the user to look at

if __name__ == "__main__":
   app.run(debug=True, use_reloader=True)