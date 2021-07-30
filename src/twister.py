# API.py
# Main class for twister library
# Created at: May 29, 2021
# Author: Thyago M.

import requests
import base64

class API:

    _TWITTER_API_ENDPOINT = 'https://api.twitter.com/'

    def __init__(self, consumer_key, consumer_secret):
        key_secret = '{}:{}'.format(consumer_key, consumer_secret).encode('ascii')
        key_secret = base64.b64encode(key_secret)
        key_secret = key_secret.decode('ascii')
        headers = {
            'Authorization': 'Basic {}'.format(key_secret),
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
        data = {
            'grant_type': 'client_credentials'
        }
        url = '{}oauth2/token'.format(API._TWITTER_API_ENDPOINT)
        response = requests.post(
            url, 
            headers = headers, 
            data = data
        )
        if response.status_code == 200:
            self.bearer_token = response.json()['access_token']
        else:
            print("Authentication Error. Check your Twitter Credentials!")
            raise Exception("Authentication Error. Check your Twitter Credentials!")

    def get(self, op, params):
        headers = {
            'Authorization': 'Bearer {}'.format(self.bearer_token)    
        }
        url = '{}{}'.format(API._TWITTER_API_ENDPOINT, op)
        response = requests.get(
            url, 
            headers = headers, 
            params = params
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Invalid Request! Check Twitter's API documentation!\n" + response.text)        

    def post(self, op, data):
        headers = {
            'Authorization': 'Bearer {}'.format(self.bearer_token)    
        }
        url = '{}{}'.format(API._TWITTER_API_ENDPOINT, op)
        response = requests.post(
            url, 
            headers = headers, 
            data = data
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Invalid Request! Check Twitter's API documentation!\n" + response.text)        