import urllib
import os
import requests     
import json
import numpy as np
import pandas as pd

# from penquins import Kowalski

## retreive api_token from secret.txt
with open('secret.txt', 'r') as file:
    api_token = file.read().strip()
# kowalski_token = ""

host = "https://fritz.science/"
headers = {'Authorization': f'token {api_token}'}

# instances = {'kowalski': {'protocol': 'https', 'port': 443, 'host': f'kowalski.caltech.edu', 'token': kowalski_token,}} 
# kowalski = Kowalski(instances=instances)
# if kowalski.ping(name="kowalski"):
#     print("Connected to Kowalski")
# else:
#     print("Unable to connect to Kowalski")
#     exit() 

dataDir = "data/"

# df_bts = pd.read_csv('BTS.csv')
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

    # query = {
    #     "query_type": "find",
    #     "query": {
    #         "catalog": "ZTF_alerts",
    #         "filter": {
    #             # take only alerts for specified object
    #             'objectId': objId,
    #         },
    #         # what quantities to recieve 
    #         "projection": {
    #             "_id": 0,
    #             "objectId": 1,

    #             "candidate.candid": 1,
    #             "candidate.programid": 1,
    #             "candidate.fid": 1,
    #             "candidate.isdiffpos": 1,
    #             "candidate.ndethist": 1,
    #             "candidate.ncovhist": 1,
    #             "candidate.sky": 1,
    #             "candidate.fwhm": 1,
    #             "candidate.seeratio": 1,
    #             "candidate.mindtoedge": 1,
    #             "candidate.nneg": 1,
    #             "candidate.nbad": 1,
    #             "candidate.scorr": 1,
    #             "candidate.dsnrms": 1,
    #             "candidate.ssnrms": 1,
    #             "candidate.exptime": 1,

    #             "candidate.field": 1,
    #             "candidate.jd": 1,
    #             "candidate.ra": 1,
    #             "candidate.dec": 1,

    #             "candidate.magpsf": 1,
    #             "candidate.sigmapsf": 1,
    #             "candidate.diffmaglim": 1,
    #             "candidate.magap": 1,
    #             "candidate.sigmagap": 1,
    #             "candidate.magapbig": 1,
    #             "candidate.sigmagapbig": 1,
    #             "candidate.magdiff": 1,
    #             "candidate.magzpsci": 1,
    #             "candidate.magzpsciunc": 1,
    #             "candidate.magzpscirms": 1,

    #             "candidate.distnr": 1,
    #             "candidate.magnr": 1,
    #             "candidate.sigmanr": 1,
    #             "candidate.chinr": 1,
    #             "candidate.sharpnr": 1,

    #             "candidate.neargaia": 1,
    #             "candidate.neargaiabright": 1,
    #             "candidate.maggaia": 1,
    #             "candidate.maggaiabright": 1,

    #             "candidate.drb": 1,
    #             "candidate.classtar": 1,
    #             "candidate.sgscore1": 1,
    #             "candidate.distpsnr1": 1,
    #             "candidate.sgscore2": 1,
    #             "candidate.distpsnr2": 1,
    #             "candidate.sgscore3": 1,
    #             "candidate.distpsnr3": 1,

    #             "candidate.jdstarthist": 1,
    #             "candidate.jdstartref": 1,

    #             "candidate.sgmag1": 1,
    #             "candidate.srmag1": 1,
    #             "candidate.simag1": 1,
    #             "candidate.szmag1": 1,

    #             "candidate.sgmag2": 1,
    #             "candidate.srmag2": 1,
    #             "candidate.simag2": 1,
    #             "candidate.szmag2": 1,

    #             "candidate.sgmag3": 1,
    #             "candidate.srmag3": 1,
    #             "candidate.simag3": 1,
    #             "candidate.szmag3": 1,

    #             "candidate.nmtchps": 1,
    #             "candidate.clrcoeff": 1,
    #             "candidate.clrcounc": 1,
    #             "candidate.chipsf": 1,

    #             "classifications.acai_h": 1,
    #             "classifications.acai_v": 1,
    #             "classifications.acai_o": 1,
    #             "classifications.acai_n": 1,
    #             "classifications.acai_b": 1,

    #             "cutoutScience": 1,
    #             "cutoutTemplate": 1,
    #             "cutoutDifference": 1,
    #         }
    #     }
    # }

    # r = kowalski.query(query)
    # object_alerts = r["kowalski"]['data']
    # alertsFile = os.path.join(objDirectory, 'alerts.npy') 
    # np.save(alertsFile, object_alerts)
