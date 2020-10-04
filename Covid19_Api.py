'''
 Author : Dalpat I
'''
import requests
import pandas as pd
from pandas.io.json import json_normalize 
import numpy as np
import matplotlib.pyplot as plt

class API_travel:
    
    def travel_exe():
        response = requests.get("https://www.trackcorona.live/api/travel")
        
        a = response.json()['data'] #taking only "data" part of json file
        
        df = json_normalize(a)  #normalize json format data to dataframe format data
        
        df['data'].replace('', np.nan, inplace=True) # replace all blank values with 'NaN'
        
        df.dropna(subset=['data'], inplace=True) #remove all the rows containing 'NaN' values
        
        df.sort_values(by ='location', axis=0, ascending=True, inplace=True, kind='quicksort')
        #sort based on location
        
        df.reset_index(drop=True,inplace=True)
        #reset index from random no. to 0,1,2,3... series
        
        return df
    
class API_overview:
    
    def overview_exe():
        response = requests.get("https://www.trackcorona.live/api/countries")
        
        a = response.json()['data']
        
        df = json_normalize(a)
        
        df.sort_values(by ='confirmed', axis=0, ascending=False, inplace=True, kind='quicksort', na_position='last')
        df.reset_index(drop=True,inplace=True)
        
        return df
    
    def overview_bar(c,d,r):
        y=[c,d,r]
        label=['Confirmed','Dead','Recovered']
        plt.bar([0,1,2],y,color=['yellow','red','green'])
        plt.xticks([0,1,2],label,rotation=90)
        plt.title('Overview of Covid19 Cases')
        plt.show()
        
class CountryWise:
    
    def CountryWise_exe():
        df = API_overview.overview_exe()
        df=df[['location','confirmed','dead','recovered']]
        pd.set_option('display.max_rows', None)
        print(df)
    #graphs starts from here:-
    
    #Confirmed
        y=[i for i in df.confirmed[:30]]
        x=[i for i in df.location[:30]]
        plt.bar(x,y,color='yellow')
        plt.xticks(x,x,rotation=90)
        plt.title('Total Confirmed Cases Based on Countries')
        plt.show()
        
    #dead
        y=[i for i in df.dead[:30]]
        x=[i for i in df.location[:30]]
        plt.bar(x,y,color='red')
        plt.xticks(x,x,rotation=90)
        plt.title('Total Death Cases Based on Countries')
        plt.show()
        
    #recovered
        y=[i for i in df.recovered[:30]]
        x=[i for i in df.location[:30]]
        plt.bar(x,y,color='green')
        plt.xticks(x,x,rotation=90)
        plt.title('Total Recovered Cases Based on Countries')
        plt.show()
        
        
        
