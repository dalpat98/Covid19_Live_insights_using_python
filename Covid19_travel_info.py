# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 12:12:59 2020

@author: Dalpat I
"""
from Covid19_Api import API_travel

def travel():
    df = API_travel.travel_exe()
    print('Travel Information is Available for Listed Countries'.center(50,'-'))
    for i in list(df.location):
        print(i)
    country=input("Enter country name for travel information :- ")
    country=country.title()
    if country in list(df.location):
        print(df.at[list(df.location).index(country),'data'])
    else:
        print("Information is not Available at the moment")
        
travel()