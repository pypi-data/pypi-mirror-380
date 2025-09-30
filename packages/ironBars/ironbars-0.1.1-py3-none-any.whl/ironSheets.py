# Author -> Sevrus b25bs1304@iitj.ac.in, GITHUB -> sevruscorporations@gmail.com
import pandas as pd

def gsheet_load(url, as_df=False):
    """
    Convert a Google Sheets share link to a CSV export link.
    
    Parameters:
        url (str | list): Google Sheet URL(s).
        as_df (bool): If True, return pandas DataFrame(s) instead of URL(s).
    
    Returns:
        str | list | DataFrame | list[DataFrame]
    """
    
    def convert(single_url):
        return single_url.strip().replace("/edit?usp=sharing", "/gviz/tq?tqx=out:csv")
    
    # Handle single URL vs list
    if isinstance(url, list):
        converted = [convert(u) for u in url]
        return [pd.read_csv(u) for u in converted] if as_df else converted
    else:
        converted = convert(url)
        return pd.read_csv(converted) if as_df else converted
