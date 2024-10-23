import pygsheets
import pyodbc
import pandas as pd

# Set up connection to MS SQL Server
server = '<your_server>'
database = '<your_database>'
username = '<your_username>'
password = '<your_password>'
cnxn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')

# Define SQL query
query = '''
<your_sql_query_here>
'''

# Run query and export results to CSV file
df = pd.read_sql(query, cnxn)
df.to_csv('data/Sales.csv', index=False, na_rep='')

df = pd.read_csv('data/Sales.csv', na_values=['NaN'], keep_default_na=False).fillna('')

# Authenticate with Google Sheets API using service account key file
gc = pygsheets.authorize(service_file='credentials.json')

# Open the spreadsheet and select the worksheet
spreadsheet_url = '<your_google_sheet_url>'
spreadsheet = gc.open_by_url(spreadsheet_url)
worksheet = spreadsheet[0]
worksheet.clear(start='A1')

# Upload the CSV file to the worksheet
worksheet.set_dataframe(df, start='A1')

print('Data posted to Google Sheets successfully!')
