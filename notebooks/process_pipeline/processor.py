import pandas as pd
import numpy as np
from pathlib import Path 

def process_csv_file(filepath, output_folder = Path("../data/processed/"), fill_with=np.nan):
    """
    Process a csv file so it's ready for exploratory data analysis.
    
    Parameters
    -----------
    filepath
        Path to the csv file to import.
    output_folder 
        Path to the folder where you want the processed version to reside.
    fill_with 
        Value to substitute for zero.
        
    Returns
    --------
    output_filepath
        Path to the csv file which is output.
    """
    pass