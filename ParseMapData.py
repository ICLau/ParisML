# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 21:38:11 2018

@author: Isaac
"""

#from bs4 import BeautifulSoup
import bs4 as bs

soup = None
with open('Paris.xml') as sauce:
    soup = bs.BeautifulSoup (sauce,'xml')
    sauce.close()

i=0
for placemark in soup.findAll ('Placemark'):
    i+=1
    fLong, fLat, _ = placemark.find('coordinates').text.split(',')
    fLong = float(fLong)
    fLat = float (fLat)
    print ("({0})POI: {1} --- Long = {2} / Lat = {3}".format(
                        i,
                        placemark.find('name').text,
                        fLong, 
                        fLat))

# =============================================================================
# i = 1
# for placemark in soup.Placemark.find_next_siblings ():
#     print (i)
#     i += 1
#     print (placemark.find('name').string)
#     fLong, fLat, _ = placemark.find('coordinates').text.split(',')
#     fLong = float(fLong)
#     fLat = float (fLat)
#     print ("Long = {0} / Lat = {1}".format(fLong, fLat))
# =============================================================================
