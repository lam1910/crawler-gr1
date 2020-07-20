import json
from bs4 import BeautifulSoup

with open('new-data.json') as fp:
    text = json.load(fp)

for item in text:
    old_label = ''
    try:
        old_text = item['info']
        old_label = 'info'
    except KeyError:
        try:
            old_text = item['section']
            old_label = 'section'
        except KeyError:
            old_text = item['subsection']
            old_label = 'subsection'

    if '\u2019' in old_text:
        old_text.replace('\u2019', '\'')

    new_text = BeautifulSoup(old_text).text
    item[old_label] = new_text

new_list = []
ske_dict = {'section': '', 'subsection': '', 'info': ''}

new_list.append(ske_dict)
for item in text:
    old_label = ''
    try:
        old_text = item['info']
        old_label = 'info'
    except KeyError:
        try:
            old_text = item['section']
            old_label = 'section'
        except KeyError:
            old_text = item['subsection']
            old_label = 'subsection'

    if old_label == 'section':
        new_list.append(ske_dict)
        new_list[-1]['section'] += old_text

    elif old_label == 'subsection':
        this_section = new_list[-1]['section']
        new_list.append(ske_dict)
        new_list[-1]['section'] += this_section
        new_list[-1]['subsection'] += old_text
    else:
        new_list[-1]['info'] += old_text

    ske_dict = {'section': '', 'subsection': '', 'info': ''}

# will need to clean the data by hand. Read and select what we need. Or can filter the information at
# the pandas dataframe. Not recommend put all the thing you crawl into database as postgresql
# varchar max at 10485760 chars. This example it can fit

# out as json
with open('world-travel-family.json', 'w') as fp:
    json.dump(new_list, fp)

# read using pandas
import pandas as pd
final_data = pd.read_json('world-travel-family.json')

# already clean data by hand only, if not comment this section
final_data = pd.read_csv('clean-text-note.txt', names=['Section', 'Subsection', 'Info'])

# back to csv for import to db
final_data.to_csv('world-travel-family.csv', header=False)
