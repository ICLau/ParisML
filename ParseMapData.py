# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 21:38:11 2018

@author: Isaac
"""

#from bs4 import BeautifulSoup
import bs4 as bs
import matplotlib.pyplot as plt

soup = None
with open('Paris.xml') as sauce:
    soup = bs.BeautifulSoup (sauce,'xml')
    sauce.close()

i=0
coords = []
listLongitudes = []
listLatitudes  = []
listPOInames = []

for placemark in soup.findAll ('Placemark'):
    i+=1
    fLong, fLat, _ = placemark.find('coordinates').text.split(',')
    fLong = float(fLong)
    fLat = float (fLat)
    
    POIname = placemark.find('name').text
    listPOInames.append(POIname)
    listLongitudes.append(fLong)
    listLatitudes.append(fLat)
    
    coords.append([fLong, fLat])
    
    print ("({0})POI: {1} --- Long = {2} / Lat = {3}".format(
                        i,
                        POIname, #placemark.find('name').text,
                        fLong, 
                        fLat))

