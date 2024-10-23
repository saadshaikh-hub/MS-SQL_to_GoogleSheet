# SQL to Google Sheets Template

This project provides a Python-based template to extract data from an MS SQL Server and upload it directly into Google Sheets. The code handles database connection, data export, and seamless integration with Google Sheets.

## Features
- Query data from MS SQL Server.
- Export query results to a CSV file.
- Upload CSV data to Google Sheets using the Google Sheets API.

## Prerequisites
- Python 3.6+
- Google Sheets API credentials (`credentials.json` file)
- MS SQL Server database

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/SQL_to_GoogleSheets_Template.git
    cd SQL_to_GoogleSheets_Template
    ```

2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Add your database credentials and query in the `SQL_to_GoogleSheets.py` file:
    ```python
    server = '<your_server>'
    database = '<your_database>'
    username = '<your_username>'
    password = '<your_password>'
    query = '''
    <your_sql_query_here>
    '''
    ```

4. Place your Google Sheets API credentials file (`credentials.json`) in the root directory.

5. Replace the Google Sheets URL with your own in the `SQL_to_GoogleSheets.py`:
    ```python
    spreadsheet_url = '<your_google_sheet_url>'
    ```

6. Run the script:
    ```bash
    python SQL_to_GoogleSheets.py
    ```

## Dependencies
This project requires the following libraries:
- `pyodbc`
- `pygsheets`
- `pandas`

You can install them using:
```bash
pip install -r requirements.txt
