# Exif-renamer.py

A simple python script that extracts EXIF data from photos
and renames them to YYYY-MM-DD hh:mm:ss-n format used
by Dropbox. 

The original problem was 12000 photos that had to be 
imported from a computer to Dropbox Camera Upload.

This script will work only with Python 3 because it uses
typehints and input() function instead of raw_input()
