# Iron Bars
A Handy utility to provide some small useful functions, which can be easily imported and provides speed and efficiency in your program.

# Requirements
- Any Operating System with python installed.
- Python's Version must be >= 3.10

## Installation
Installation process is simple, You can install the library easily via pip.
```bash
pip install ironbars
```

## IronSheets
IronSheets provides functions to handle CSV files, like importing them from google drive directly or from any other location like github(added in future versions).

### Usage
So, using IronSheets is an easy process. It provides the following function :-
- **gsheet_load(url:[str or list], as_df=False)** - This function takes a google drive's shared url of a csv file which can be automatically transformed into a usable CSV link or loaded into memory as a DataFrame, making data access seamless.
- When we use **gsheet_load({your_url}, as_df=True)** - It returns the pandas dataframe of that csv directly.
- When we set **as_df=False** - It returns the transformed url of the CSV file.
- **We can pass list of urls** - Instead of passing a single url, we can pass a list of urls & it will return list of transformed urls.
- If we use **list of urls** along with **as_df = True** then it will return list of dataframes.
```bash
import ironSheets

url = "https://docs.google.com/spreadsheets/d/1qBIPJ_W_CV3DEU4NxklnJaSeJo5wzRIPabAdCUgtCtQ/edit?usp=sharing"
corrected_url = ironSheets.gsheet_load(url)
print(corrected_url) # This is the direct download link of the csv file

# if we want the dataframe
df = ironSheets.gsheet_load(url, as_df=True) # this will return the dataframe made from the csv

urls = [url1, url2, etc] # list containing urls
corrected_urls = ironSheets.gsheet_load(urls) # it will return list of transformed urls
data_frames = ironSheets.gsheet_load(urls, as_df=True) # it will return list of dataframes
```