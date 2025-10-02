#!/opt/miniconda3/bin/python
# -----------------------------------------------------------------------------
# PyFV: A modern Python FITS Viewer
# Copyright (c) 2025, Pan S. Chai
# Distributed under the BSD 3-Clause License. See LICENSE file for details.
# -----------------------------------------------------------------------------
#   
#  Python FV Project
#
#      module: utility.py
#
#  Version: Ver 1.0 (beta)
#
#-------------------------------------------------------------------------------
#       
# Modification History: 
#
#   - Pan Chai, October 2025
#     Package migrated 
#           
#-------------------------------------------------------------------------------
#
# Description:
#
#   utility routines
#   
#-------------------------------------------------------------------------------
#

import os
import io
import re

from astropy.io import fits
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from pathlib import Path
import sys
import codecs
import os

import time
import traceback, sys


#-------------------------------------------------------------------------------
#
# Description:
#
#   - FITS headers info
#-------------------------------------------------------------------------------

def summarize_hdus(fits_file):
    """
    Display a one-line summary of each HDU in the FITS file.
    """
    if not os.path.isfile(fits_file):
        raise FileNotFoundError(f"No such file: {fits_file}")

    with fits.open(fits_file) as hdulist:
        print(f"File: {fits_file}")
        print("HDU Summary:")
        hdulist.info()  # this prints a summary directly

def summarize_all_table_columns(fits_file):
    """
    Lists names, units, and ranges of all table columns across *all* HDUs.
    """
    if not os.path.isfile(fits_file):
        raise FileNotFoundError(f"No such file: {fits_file}")

    with fits.open(fits_file) as hdulist:
        print(f"\nScanning file: {fits_file}")
        found_table = False

        for idx, hdu in enumerate(hdulist):
            if isinstance(hdu, (fits.BinTableHDU, fits.TableHDU)):
                found_table = True
                print(f"\n Table Columns in HDU[{idx}] - '{hdu.name}':")
                data = hdu.data
                columns = hdu.columns

                for colname in columns.names:
                    col = data[colname]
                    unit = columns[colname].unit or "N/A"
                    try:
                        min_val = col.min()
                        max_val = col.max()
                        print(f"  - {colname} [{unit}]: {min_val} to {max_val}")
                    except Exception as e:
                        print(f"  - {colname} [{unit}]: Unable to compute range ({e})")

        if not found_table:
            print("No table HDUs found in this FITS file.")

def summarize_table_columns(fits_file, hdu_index=None):
    """
    List names, units, and ranges of each column in a table HDU.

    If hdu_index is None, it automatically finds the first table HDU.
    """
    if not os.path.isfile(fits_file):
        raise FileNotFoundError(f"No such file: {fits_file}")

    with fits.open(fits_file) as hdulist:
        # Auto-detect first table HDU if hdu_index is not specified
        if hdu_index is None:
            for i, hdu in enumerate(hdulist):
                if isinstance(hdu, (fits.BinTableHDU, fits.TableHDU)):
                    hdu_index = i
                    break
            else:
                print("No table HDU found in the FITS file.")
                return

        hdu = hdulist[hdu_index]

        if not isinstance(hdu, (fits.BinTableHDU, fits.TableHDU)):
            print(f"HDU[{hdu_index}] is not a table.")
            return

        data = hdu.data
        columns = hdu.columns

        print(f"\nTable Columns in HDU[{hdu_index}]:")
        for colname in columns.names:
            col = data[colname]
            unit = columns[colname].unit or "N/A"
            try:
                min_val = col.min()
                max_val = col.max()
                print(f"- {colname} [{unit}]: {min_val} to {max_val}")
            except Exception as e:
                print(f"- {colname} [{unit}]: Unable to compute range ({e})")

def summarize_all_hdus(fits_file):
    """
    Summarizes all HDUs in a FITS file:
    - For table HDUs: lists column names, units, and value ranges
    - For image HDUs: shows shape, data type, and pixel value range
    """
    if not os.path.isfile(fits_file):
        raise FileNotFoundError(f"No such file: {fits_file}")

    with fits.open(fits_file) as hdulist:
        print(f"\nScanning file: {fits_file}")
        total_hdus = len(hdulist)
        print(f"\nFile: {fits_file}")
        print(f"Total HDUs: {total_hdus}")

        for idx, hdu in enumerate(hdulist):
            # hdu_type = type(hdu).__name__
            # Type override for display
            if isinstance(hdu, fits.PrimaryHDU):
                hdu_type = "Image"
            elif isinstance(hdu, fits.BinTableHDU):
                hdu_type = "Binary"
            elif isinstance(hdu, fits.TableHDU):
                hdu_type = "ASCII"
            else:
                hdu_type = type(hdu).__name__  # fallback

            hdu_name = hdu.name or "UNKNOWN"

            print(f"\nHDU[{idx}] - '{hdu_name}' ({hdu_type})")

            if isinstance(hdu, (fits.BinTableHDU, fits.TableHDU)):
                data = hdu.data
                columns = hdu.columns
                print("  Table Columns:")

                for colname in columns.names:
                    col = data[colname]
                    unit = columns[colname].unit or "N/A"
                    try:
                        min_val = col.min()
                        max_val = col.max()
                        print(f"    - {colname} [{unit}]: {min_val} to {max_val}")
                    except Exception as e:
                        print(f"    - {colname} [{unit}]: Unable to compute range ({e})")

            elif isinstance(hdu, (fits.ImageHDU, fits.PrimaryHDU)):
                if hdu.data is not None:
                    shape = hdu.data.shape
                    dtype = hdu.data.dtype
                    try:
                        min_val = hdu.data.min()
                        max_val = hdu.data.max()
                        print(f"  Image Data: shape={shape}, dtype={dtype}, range=({min_val}, {max_val})")
                    except Exception as e:
                        print(f"  Image Data: shape={shape}, dtype={dtype}, range=Unavailable ({e})")
                else:
                    print("  No image data found in this HDU.")
            else:
                print("  Skipped: Not a recognized image or table HDU.")

def display_hdu_header(fits_file, hdu_index=None):
    """
    Displays the FITS header(s) from the given file.
    
    - If hdu_index is None: prints headers for all HDUs.
    - If hdu_index is specified: prints the header for that HDU only.
    """
    if not os.path.isfile(fits_file):
        raise FileNotFoundError(f"No such file: {fits_file}")

    with fits.open(fits_file) as hdulist:

        if hdu_index is None:
            print(f"\n📂 Scanning all HDU headers in: {fits_file}")
            for idx, hdu in enumerate(hdulist):
                print(f"\n📄 Header for HDU[{idx}] - '{hdu.name}' ({type(hdu).__name__}):\n")
                print(hdu.header.tostring(sep='\n'))
                print("-" * 60)
        else:
            if hdu_index < 0 or hdu_index >= len(hdulist):
                raise IndexError(f"HDU index {hdu_index} is out of range. File contains {len(hdulist)} HDUs.")
            hdu = hdulist[hdu_index]
            print(f"\n📄 Header for HDU[{hdu_index}] - '{hdu.name}' ({type(hdu).__name__}):\n")
            print(hdu.header.tostring(sep='\n'))
            print("-" * 60)

