"""
This module cleans all the files which are not required.
"""
import os

def cleanup(filePath):
    os.remove(filePath)