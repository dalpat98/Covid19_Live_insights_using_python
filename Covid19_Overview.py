# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 12:44:15 2020

@author: Dalpat I
"""

from Covid19_Api import API_overview

def overview():
    print('overview of Covid19 Cases'.center(70,'-'))
    
    df_overview = API_overview.overview_exe()
    
    confirmed=df_overview['confirmed'].sum()
    
    dead=df_overview['dead'].sum()
    
    recovered=df_overview['recovered'].sum()
    
    print("Total Confirmed :- ",confirmed)
    print("Total Deaths :- ",dead)
    print("Total Recovered :- ",recovered)
    
    API_overview.overview_bar(confirmed,dead,recovered)

overview()