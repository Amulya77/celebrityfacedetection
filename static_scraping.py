Download data from wikipedia

#Copyright 2022 Fabian Bosler

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation 
# files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, 
# modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom 
# the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the 
# Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO 
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS 
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import requests
import pandas as pd
from bs4 import BeautifulSoup

# download wikipage
wikipage = "https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_continent_(data_file)"
result = requests.get(wikipage)

# if successful parse the download into a BeautifulSoup object, which allows easy manipulation 
if result.status_code == 200:
    soup = BeautifulSoup(result.content, "html.parser")
    
# find the object with HTML class wikitable sortable
table = soup.find('table',{'class':'wikitable sortable'})

# loop through all the rows and pull the text
new_table = []
for row in table.find_all('tr')[1:]:
    column_marker = 0
    columns = row.find_all('td')
    new_table.append([column.get_text() for column in columns])
    
df = pd.DataFrame(new_table, columns=['ContinentCode','Alpha2','Alpha3','PhoneCode','Name'])
df['Name'] = df['Name'].str.replace('\n','')
df
