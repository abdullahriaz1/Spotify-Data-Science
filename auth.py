import requests
import json

class Auth(object):
    def __init__(self):
        self._client_id = "d20a5664636142e4ba58a7cbe3d4f3ea"
        self._client_secret = "5a99d697c466440899e2cb4a94a4f5bb"
        self._redirect_uri = "https://open.spotify.com/user/ariaz988"
        self._scope = "playlist-modify-private%20playlist-modify-public%20user-top-read"
    
    def connect(self):
        response = requests.get(
            "https://accounts.spotify.com/authorize?client_id={}&response_type=code&redirect_uri={}&scope={}".format(self._client_id, self._redirect_uri, self._scope)
        )
