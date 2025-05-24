SEARCH_KEY = "AIzaSyBhSpqrgWH2Ny39qPuU-lUDvacBJKt3AIw"
SEARCH_ID = "1066c988d47814d22"
COUNTRY = "INDIA"
SEARCH_URL = "https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&q={query}&start={start}&num=10&gl=" + COUNTRY
RESULT_COUNT = 20

#Storing our results with sqlite3
import os
if os.path.exists("private.py"):
    from private import *