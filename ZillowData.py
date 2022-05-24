# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 18:41:29 2020

@author: Haley Harleman
"""
#importing csv file
import pandas as pd
zillow=pd.read_csv("Zip_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_mon_CA modified.csv")
zillow

#filter the data to only show zip code, 2008, and 2020 data using the loc function; save as new df
zillowdf=zillow.loc[:,["RegionName","6/30/2008","6/30/2020"]]

#remove null values -- some 2008 date is missing so we need to delete the row
df1=zillowdf.dropna()
df1

#Calculate Percent Changes and add to dataframe
df6=df1["6/30/2008"].sub(df1["6/30/2020"]).div(df1["6/30/2020"]).mul(100)
df1["Percent Change"]=df6
df1

#sort %change values so the highest increase is on to[]
df2=df1.sort_values(by='Percent Change', ascending=False)
df2

#export to excel
df2.to_excel("Zillow Data 1.xlsx",
             sheet_name='Zillow')

#The top 10 zip codes with growth
print("Top 10 Increases: ", df2.head(10))

#average percent change, quartile ranges, etc
print(df2.describe())
