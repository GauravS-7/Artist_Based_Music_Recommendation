artist_retriever = ArtistRetriever()
    artist_retriever.load_artists(Path("LastFM_Data/artists.dat"))
    artist = artist_retriever.get_artist_name_from_id(1)
    print(artist)