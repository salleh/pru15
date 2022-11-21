import time
import random
import requests

GENERAL_BASE_FOLDER = 'data/'
PARTY_INFO_URL = 'https://data.pru.astroawani.com/data/party.json'
SEASON_INFO_URL = 'https://data.pru.astroawani.com/data/seasons.json'

GE14_BASE_FOLDER = 'data/pru14/'
GE14_BASE_URL = 'https://data.pru.astroawani.com/data/1/individual/parliament/'

GE15_BASE_FOLDER = 'data/pru15/'
GE15_BASE_URL = 'https://data.pru.astroawani.com/data/11/individual/parliament/'

print('Downloading Party Data...')
response = requests.get(PARTY_INFO_URL)
open(GENERAL_BASE_FOLDER + 'party.json', 'wb').write(response.content)
time.sleep(random.uniform(0.5, 5.0)) # DDoS evasion

print('Downloading Season Data...')
response = requests.get(SEASON_INFO_URL)
open(GENERAL_BASE_FOLDER + 'seasons.json', 'wb').write(response.content)
time.sleep(random.uniform(0.5, 5.0)) # DDoS evasion

print('Downloading PRU14 Result Data...')
for i in range(1,223):
    print('Downloading PRU14 P' + str(i).zfill(3) + ' data...')
    fname = 'P' + str(i).zfill(3) + '.json'
    data_url = GE14_BASE_URL + fname
    response = requests.get(data_url)
    open(GE14_BASE_FOLDER + fname, 'wb').write(response.content)
    time.sleep(random.uniform(0.5, 5.0)) # DDoS evasion

print('Downloading PRU15 Result Data...')
for i in range(1,223):
    print('Downloading PRU14 P' + str(i).zfill(3) + ' data...')
    fname = 'P' + str(i).zfill(3) + '.json'
    data_url = GE15_BASE_URL + fname
    response = requests.get(data_url)
    open(GE15_BASE_FOLDER + fname, 'wb').write(response.content)
    time.sleep(random.uniform(0.5, 5.0)) # DDoS evasion