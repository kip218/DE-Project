import duckdb
import requests
import json
from pprint import pprint
import re


url = 'https://drive.google.com/uc?id=1IjIEhLc9n8eLKeY-yh_YigKVWbhgGBsN'

BASE_URL = 'https://drive.google.com/uc?id='
FILE_ID = '1IjIEhLc9n8eLKeY-yh_YigKVWbhgGBsN'
# db = duckdb.read_csv(BASE_URL + FILE_ID)
# print(db)

url = 'https://drive.google.com/drive/u/1/folders/1gLSw0RLjBbtaNy0dgnGQDAZOHIgCe-HH'
r = requests.get(url)
r = r.content.decode()

pattern = re.compile('([12][0-9]{3}_LoL_esports_match_data_from_OraclesElixir.csv).{0,2000}https://drive.google.com/file/d/(.*?)/view?')
files_data = pattern.findall(r)
pprint(files_data)

# for data in files_data:
# 	print(data[0], data[1])
