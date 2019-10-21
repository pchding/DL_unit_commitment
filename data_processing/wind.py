# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 14:01:13 2019

@author: Zeinilima
"""

import pandas as pd
import random

def wind_recale(file_name):
    wind_df = pd.read_csv(file_name)
    wind_df["Month"] = "m"+ wind_df["Month"].astype(str)
    wind_df["Day"] = "d" + wind_df["Day"].astype(str)
    wind_df["Period"]= "t"+wind_df["Period"].astype(str)
    
    wind_df["309_WIND_1"] = wind_df["309_WIND_1"]*(150/wind_df["309_WIND_1"].max())
    wind_df["317_WIND_1"] = wind_df["317_WIND_1"]*(300/wind_df["317_WIND_1"].max())
    wind_df["303_WIND_1"] = wind_df["303_WIND_1"]*(600/wind_df["303_WIND_1"].max())
    wind_df["122_WIND_1"] = wind_df["122_WIND_1"]*(600/wind_df["122_WIND_1"].max())
    
    ##New wind
    random.seed(100)
    wind_df["309_WIND_2"] = wind_df["309_WIND_1"].apply(lambda x: x + x*random.uniform(-0.05,0.05))
    random.seed(101)
    wind_df["309_WIND_3"] = wind_df["309_WIND_1"].apply(lambda x: 2*x + 2*x*random.uniform(-0.05,0.05))
    random.seed(102)
    wind_df["309_WIND_4"] = wind_df["309_WIND_1"].apply(lambda x: 3*x + 3*x*random.uniform(-0.05,0.05))
    
    random.seed(103)
    wind_df["317_WIND_2"] = wind_df["317_WIND_1"].apply(lambda x: x + x*random.uniform(-0.05,0.05))
    random.seed(104)
    wind_df["317_WIND_3"] = wind_df["317_WIND_1"].apply(lambda x: 2*x + 2*x*random.uniform(-0.05,0.05))
    
    random.seed(105)
    wind_df["303_WIND_2"] = wind_df["303_WIND_1"].apply(lambda x: 0.5*x + 0.5*x*random.uniform(-0.05,0.05))
    random.seed(106)
    wind_df["303_WIND_3"] = wind_df["303_WIND_1"].apply(lambda x: 0.25*x + 0.25*x*random.uniform(-0.05,0.05))
    random.seed(107)
    wind_df["303_WIND_4"] = wind_df["303_WIND_1"].apply(lambda x: x + x*random.uniform(-0.05,0.05))
    
    random.seed(107)
    wind_df["122_WIND_2"] = wind_df["122_WIND_1"].apply(lambda x: x + x*random.uniform(-0.05,0.05))
    random.seed(108)
    wind_df["122_WIND_3"] = wind_df["122_WIND_1"].apply(lambda x: 0.5*x + 0.5*x*random.uniform(-0.05,0.05))
    
    wind_df["dot1"] = len(wind_df)*["."]
    wind_df["dot2"] = len(wind_df)*["."]
    wind_df["dot3"] = len(wind_df)*["."]
    
    wind_df = wind_df[["Year","dot1","Month","dot2","Day","dot3","Period",
                       "309_WIND_1","309_WIND_2","309_WIND_3","309_WIND_4",
                       "317_WIND_1","317_WIND_2","317_WIND_3",
                       "303_WIND_1","303_WIND_2","303_WIND_3","303_WIND_4",
                       "122_WIND_1","122_WIND_2","122_WIND_3"]]
    return wind_df

if __name__ == '__main__':
    wind_df = wind_recale("RTS_wind_raw.csv")
    wind_df.to_csv("RTS_wind_rescaled.csv",index=False,header=True,na_rep="")
    
    windd_df = wind_recale("DAY_AHEAD_wind.csv")
    windd_df.to_csv("RTS_dhwind_rescaled.csv",index=False,header=True,na_rep="")
