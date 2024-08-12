import duckdb
import requests
import json
from pprint import pprint
import re
from utils import get_file_ids, get_csv_file_to_duckdb
from datetime import datetime


url = 'https://drive.google.com/uc?id=1IjIEhLc9n8eLKeY-yh_YigKVWbhgGBsN'

FILE_IDS = get_file_ids()

db = get_csv_file_to_duckdb(FILE_IDS['2024'])
print(db)