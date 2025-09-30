# Author -> Sevrus b25bs1304@iitj.ac.in, GITHUB -> sevruscorporations@gmail.com
import os
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

def gsheet_load(url, as_df=False, max_workers=None):
    """
    Convert a Google Sheets share link to a CSV export link and optionally load as DataFrame(s).

    Parameters:
        url (str | list): Google Sheet URL(s).
        as_df (bool): If True, return pandas DataFrame(s) instead of URL(s).
        max_workers (int | None): Max threads for parallel downloading (only for list of URLs).

    Returns:
        str | list | pd.DataFrame | list[pd.DataFrame]
    """

    def convert(single_url):
        if not single_url.startswith("https://docs.google.com/spreadsheets/"):
            raise ValueError(f"Invalid Google Sheet URL: {single_url}")
        # Handle different URL formats robustly
        if "/edit" in single_url:
            return single_url.split("/edit")[0] + "/gviz/tq?tqx=out:csv"
        return single_url  # Already CSV export link

    def fetch_csv(single_url):
        csv_url = convert(single_url)
        try:
            return pd.read_csv(csv_url)
        except Exception as e:
            raise RuntimeError(f"Failed to read CSV from {single_url}: {e}")

    # Handle single URL vs list
    if isinstance(url, list):
        if as_df:
            # Parallel download of multiple URLs
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                return list(executor.map(fetch_csv, url))
        else:
            return [convert(u) for u in url]
    else:
        converted = convert(url)
        return pd.read_csv(converted) if as_df else converted


def gsheet_save(data_frames, auto_name=True, name_series="Sheet", save_dir=".", filename=None):
    """
    Save one or more DataFrames as CSV files.

    Parameters:
        data_frames (pd.DataFrame | list[pd.DataFrame]): Single dataframe or list of dataframes to save.
        auto_name (bool): If True, generates filenames automatically using name_series + index (only for multiple frames).
        name_series (str | list): Base name (str) or list of names (required if auto_name=False and multiple frames).
        save_dir (str): Directory to save CSV files. Defaults to current directory.
        filename (str | None): Filename for single dataframe. Required if saving a single DataFrame.
    """
    # Normalize input to list
    single_input = False
    if isinstance(data_frames, pd.DataFrame):
        data_frames = [data_frames]
        single_input = True

    assert data_frames, "DATA FRAMES must not be empty!"

    # Ensure absolute save directory path
    save_dir = os.path.abspath(save_dir)
    os.makedirs(save_dir, exist_ok=True)

    # Handle single dataframe case
    if single_input:
        assert filename, "Must provide 'filename' when saving a single DataFrame"
        if not filename.lower().endswith(".csv"):
            filename += ".csv"
        fpath = os.path.join(save_dir, filename)
        data_frames[0].to_csv(fpath, index=False)
        return  # Nothing to return

    # Handle multiple dataframes
    if auto_name:
        if isinstance(name_series, list):
            raise RuntimeError("Auto Name -> True but name_series is a list! Provide a string base name instead.")
    else:
        if not isinstance(name_series, list):
            raise RuntimeError("Auto Name -> False. Provide a list of filenames as name_series.")
        if len(name_series) < len(data_frames):
            raise ValueError("Number of filenames provided is less than number of data frames.")

    for idx, frame in enumerate(data_frames):
        if auto_name:
            fname = f"{name_series}{idx}.csv"
        else:
            fname = f"{name_series[idx]}.csv"
        fpath = os.path.join(save_dir, fname)
        frame.to_csv(fpath, index=False)
