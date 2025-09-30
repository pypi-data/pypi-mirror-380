# Iron Bars

**Iron Bars** is a lightweight Python utility providing a set of small but powerful functions to simplify common programming tasks. It is designed to be fast, easy to use, and improve efficiency in your projects.

---

## Requirements

- Any operating system with Python installed.
- Python version >= 3.10.

---

## Installation

You can easily install **Iron Bars** via `pip`:

```bash
pip install ironbars
```

---

## IronSheets

**IronSheets** is a module within Iron Bars that simplifies working with CSV files, especially for loading data directly from Google Sheets. Future versions will also include support for other sources like GitHub.

---

### Functions

#### `gsheet_load(url: str | list, as_df: bool = False, max_workers: int | None = None)`

This function takes a Google Sheets share link (or a list of links) and either:

- Converts it to a direct CSV download URL, or  
- Loads it directly as a pandas DataFrame.

**Parameters:**

- `url` (`str` | `list[str]`): Google Sheet URL(s).  
- `as_df` (`bool`): If `True`, returns pandas DataFrame(s) instead of CSV URL(s). Default is `False`.  
- `max_workers` (`int` | `None`): Maximum threads for parallel downloading (used when multiple URLs are provided). Defaults to `None`.

**Returns:**

- `str` | `list[str]` | `pd.DataFrame` | `list[pd.DataFrame]`

**Examples:**

```python
import ironSheets

# Single URL -> transformed CSV link
url = "https://docs.google.com/spreadsheets/d/1qBIPJ_W_CV3DEU4NxklnJaSeJo5wzRIPabAdCUgtCtQ/edit?usp=sharing"
corrected_url = ironSheets.gsheet_load(url)
print(corrected_url)  # Direct CSV download link

# Single URL -> pandas DataFrame
df = ironSheets.gsheet_load(url, as_df=True)
print(df.head())

# Multiple URLs -> list of CSV links
urls = [url1, url2]
corrected_urls = ironSheets.gsheet_load(urls)
print(corrected_urls)

# Multiple URLs -> list of DataFrames (parallel download)
data_frames = ironSheets.gsheet_load(urls, as_df=True)
for df in data_frames:
    print(df.head())
```

---

#### `gsheet_save(data_frames, auto_name=True, name_series="Sheet", save_dir=".", filename=None)`

This function saves one or more pandas DataFrames as CSV files.

**Parameters:**

- `data_frames` (`pd.DataFrame | list[pd.DataFrame]`): Single DataFrame or a list of DataFrames to save.  
- `auto_name` (`bool`): If `True`, generates filenames automatically using `name_series` + index. Only for multiple DataFrames. Default is `True`.  
- `name_series` (`str` | `list[str]`): Base name (string) for auto-naming, or list of filenames when `auto_name=False`.  
- `save_dir` (`str`): Directory to save CSV files. Defaults to the current working directory (`.`).  
- `filename` (`str` | `None`): Required when saving a single DataFrame. Must include `.csv` extension or it will be added automatically.

**Notes:**

- **Single DataFrame**: You must provide the `filename` parameter.  
- **Multiple DataFrames**: You can use `auto_name=True` (e.g., `Sheet0.csv`, `Sheet1.csv`) or provide a list of names with `auto_name=False`.  
- The function ensures the `save_dir` exists.

**Examples:**

```python
# Single DataFrame -> specify filename
df = ironSheets.gsheet_load(url, as_df=True)
ironSheets.gsheet_save(df, filename="my_sheet.csv")

# Multiple DataFrames -> auto name
dfs = ironSheets.gsheet_load([url1, url2], as_df=True)
ironSheets.gsheet_save(dfs, auto_name=True, name_series="Sheet")

# Multiple DataFrames -> custom names
ironSheets.gsheet_save(dfs, auto_name=False, name_series=["First", "Second"])
```

---

### Improvements in the latest version

- Robust URL conversion for various Google Sheets formats.  
- Parallel downloading of multiple Google Sheets using threads.  
- Optional `max_workers` for controlling parallel downloads.  
- Improved error handling for invalid or inaccessible URLs.  
- Absolute `save_dir` handling and automatic directory creation.  
- Single DataFrame saving requires a filename, preventing accidental overwrites.  
- Auto and custom naming for multiple DataFrames with clear assertions and error messages.  

---

**Author:** Sevrus (b25bs1304@iitj.ac.in)  
**GitHub:** [sevruscorporations](https://github.com/sevruscorporations)
