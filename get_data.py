import urllib
import os
import requests     
import json
import numpy as np
import pandas as pd

with open('secret.txt', 'r') as file:
    api_token = file.read().strip()

host = "https://fritz.science/"
headers = {'Authorization': f'token {api_token}'}

dataDir = "data/"

objIds = [
    "ZTF18abantmh",
    "ZTF20abmvjda",
    "ZTF20abtxwfx",
    "ZTF20abummyz",
    "ZTF20abwysqy",
    "ZTF20achedzl",
    "ZTF20acpjgkt",
    "ZTF20acqehqq",
    "ZTF20acqntkr",
    "ZTF21aabtdut",
    "ZTF21abbvvmf",
    "ZTF22abtonxt",
    "ZTF23aagbipz",
    "ZTF23aatldsz",
    "ZTF23absafzo",
    "ZTF24aagnnor"
]

for ii, objId in enumerate(objIds):
    print(ii, objId, float(ii / len(objIds)))

    objDirectory = os.path.join(dataDir, objId)
    if not os.path.isdir(objDirectory):
        os.makedirs(objDirectory)
    else:
        continue

    endpoint = f"sources/{objId}/photometry"                               
    url = urllib.parse.urljoin(host, f'/api/{endpoint}') 
    r = requests.get(url, headers=headers) 
    photometry = r.json()['data'] 
    photometryFile = os.path.join(objDirectory, 'photometry.json') 
    with open(photometryFile, 'w') as fp:  
        json.dump(photometry, fp)

    endpoint = f"sources/{objId}/spectra"
    url = urllib.parse.urljoin(host, f'/api/{endpoint}')
    r = requests.get(url, headers=headers)
    spectra = r.json()['data']
    spectraFile = os.path.join(objDirectory, 'spectra.json')
    with open(spectraFile, 'w') as fp:
        json.dump(spectra, fp)
