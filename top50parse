import pandas as pd
from bs4 import BeautifulSoup
import requests
import os


# Use BeautifulSoup to create url object to parse table data from
url = "https://www.ratebeer.com/top/all"

# Use requests module to send http request
r = requests.get(url)

# '.text' to put web content into text for parsing, call BeautifulSoup on text
data = r.text
soup = BeautifulSoup(data,'lxml')


# Find tables and then rows within website html

table = soup.find_all('table')[0]
rows = table.find_all('tr')[1:]

# Create empty dictionary to categorize table values

data = {
    'Rank' : [],
    'Beer Info' : [],
    'Reviews' : [],
    'ABV' : [],
    'Score' : [],
}

# iterate through table rows placing column values in respective keys
for row in rows:
    cols = row.find_all('td')
    data['Rank'].append( cols[0].get_text() )
    data['Beer Info'].append( cols[1].get_text() )
    data['Reviews'].append( cols[2].get_text() )
    data['ABV'].append( cols[3].get_text() )
    data['Score'].append( cols[4].get_text() )

# convert beerdata into pandas DataFrame
beerdata = pd.DataFrame(data)

# Rearrange columns in preferred order
beerdata = beerdata[['Rank','Beer Info','ABV','Score','Reviews']]

# Change directory to desired location
os.chdir('/Users/')

# Export top50 file to csv
beerdata.to_csv('RateBeer_Top.csv', sep=',',index = False)
