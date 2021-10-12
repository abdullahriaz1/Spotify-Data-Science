import requests
import json

class Connect(object):
    def __init__(self, auth):
        self.auth = auth #creates a class associated with an authorization bearer
        self.user_id = "ariaz988"
    
    def convertURIs(self, URIList):
        #takes a list of spotify artist uri's and returns one api url for all artists
        if len(URIList) == 1:
            return "https://api.spotify.com/v1/artists?ids=" + URIList[0]

        for i in range(len(URIList)):
            URIList[i] = URIList[i].replace("spotify:artist:", "")
        url = "https://api.spotify.com/v1/artists?ids="
        for i in range(len(URIList)):
            if i < len(URIList) - 1:
                url += URIList[i] + "%2C"
            else:
                url += URIList[i]
        return url
    
    def convertURI(self, URI):
        return "https://api.spotify.com/v1/artists/" + URI

    def getArtists(self, URIList):
        #returns json info of multiiple artists
        artistURLs = self.convertURIs(URIList)
        response = requests.get(
            artistURLs,
            headers={"Authorization": "Bearer " + self.auth}
        )
        response = response.json()
        for i in response["artists"]:
            print(i["name"])
    
    def getAnArtistsTopTracks(self, URI):
        topTracksURL = "https://api.spotify.com/v1/artists/" + URI + "/top-tracks?market=US"
        response = requests.get(
            topTracksURL,
            headers={"Authorization": "Bearer " + self.auth}
        )
        response = response.json()
        songs = []
        for i in response["tracks"]:
            songs.append([i["name"], i["uri"]])
        return songs
    
    def getMyTopArtists(self):
        response = requests.get(
            "https://api.spotify.com/v1/me/top/artists?time_range=medium_term&limit=10&offset=5",
            headers={"Authorization": "Bearer " + self.auth}
        )
        response = response.json()
        myTopArtists = []
        for i in response["items"]:
            myTopArtists.append([i["name"], i["uri"].replace("spotify:artist:", "")])
        return myTopArtists

    def createPlaylist(self):
        request_body = json.dumps(
            {
                "name": "Abdullah's New Playlist",
                "description": "Made with Spotify API",
                "public": True,
            }
        )
        response = requests.post(
            "https://api.spotify.com/v1/users/{}/playlists".format(self.user_id),
            data = request_body,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer " + self.auth
            },
        )
        response = response.json()
        return response["id"]

    def addSongsToPlaylist(self, playlistID, songs):
        uris = []
        for songList in songs:
            for song in songList:
                uris.append(song[1])
        request_data = json.dumps(
            uris
            )

        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(playlistID)
        response = requests.post(
            query,
            data = {
                request_data
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer " + self.auth
            }
        )
        response = response.json()
        print
