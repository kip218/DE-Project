'''
Utility functions
'''
import requests
import re
import duckdb

def get_file_ids() -> dict:
	"""
	Get all files from Oracle's Elixir Google Drive folder.

	Returns:
		dict: dictionary of years and file IDs for that year
	"""
	url = 'https://drive.google.com/drive/u/1/folders/1gLSw0RLjBbtaNy0dgnGQDAZOHIgCe-HH'
	r = requests.get(url).content.decode()
	pattern = re.compile('([12][0-9]{3}_LoL_esports_match_data_from_OraclesElixir.csv).{0,2000}https://drive.google.com/file/d/(.*?)/view?')
	files = set(pattern.findall(r))	# set() to remove duplicates

	files_by_year = {}
	for filename, fileID in files:
		year = filename.split('_')[0]
		files_by_year[year] = fileID
	
	return files_by_year

def get_csv_file_to_duckdb(file_id: str) -> duckdb.DuckDBPyRelation:
	"""
	Download csv file and load data into DuckDB.
	
	Parameters:
		file_id (str): the Google Drive file ID - files are organized by year
	
	Returns:
		DuckDBPyRelation: contains data for all professional games played for a given year
	"""
	url = 'https://drive.google.com/uc?id=' + file_id
	return duckdb.read_csv(url)