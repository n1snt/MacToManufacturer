"""
This method downloads the manuf file.
"""
import urllib.request

def downloadManuf(fileName):
    urllib.request.urlretrieve("https://gitlab.com/wireshark/wireshark/-/raw/master/manuf", fileName)