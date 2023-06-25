import requests
from requests.auth import HTTPBasicAuth
import zipfile
from io import BytesIO



def pull(kaggle_username, kaggle_apikey):
    #API bit
    #with kaggle you need to authenticate using basic Auth, which is a type of auth.
    #requests library has objects that helps with this, eg HTTPBasicAuth
    basic = HTTPBasicAuth(kaggle_username, kaggle_apikey)
    #we are going to get a request on this endpoint (URL). 
    #Stream= True is required for unziping the file as it has to be in stream format for the zipfile library to handle
    response = requests.get('https://www.kaggle.com/api/v1/datasets/download/evangower/valorant-esports-top-earnings', auth = basic, stream=True)

    #error checking, exit() exists the program entirely
    if response.status_code == 401:
        print('401 Unauthorised')
        exit()

    #we are using the zipfile library for reading the tresponse stream (content) as a list of bytes.
    z = zipfile.ZipFile(BytesIO(response.content))
    #unzips the file
    z.extractall('data')

