from connect import Connect
def main():

    myAuth = "BQA_7XiQyCWTmxg8RbacyDJTO4iRY_94DHo-nntmaNKtY02ij5V1CNVNoIfzWk3ApTxIE4vkdty_GBXpjMTkeYRhWufPt92RUL1PJnSAoaUV9cGwqsI5uhZRT1I6yzEdxW5ioJgqdEgsipPQ8MsM4B3i_2HDqbeR1YfGijSgRlPKWR-Ny07B7V84CbHhsHRRknbEA2ANqZVEZBWBHC1Pvkae3w"
    myConnection = Connect(myAuth)
    favoriteArtists = []
    favoriteArtists = myConnection.getMyTopArtists()
    topTracks = []
    for i in favoriteArtists:
        topTracks.append(myConnection.getAnArtistsTopTracks(i[1]))
    newPlaylistId = myConnection.createPlaylist()
    addTopTracks = myConnection.addSongsToPlaylist(newPlaylistId, topTracks)
    print("goodbye world")

if __name__ == "__main__":
    main()