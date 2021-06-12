from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth



billboard_url="https://www.billboard.com/charts/hot-100"

date=input("Enter a date : ")
response=requests.get(url=f"{billboard_url}/{date}")
html_code=response.text

soup=BeautifulSoup(html_code,"html.parser")
title=soup.find_all(name="span",class_="chart-element__information__song text--truncate color--primary")
title_list=[name.getText() for name in title]



CLIENT_ID="e4dbf100038741529efb5b8a7930e8a2"
CLIENT_SECRET="1508e3260a674a40b7e439a6777c21ab"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private",
        redirect_uri="https://example.com/",
        client_id="e4dbf100038741529efb5b8a7930e8a2",
        client_secret="1508e3260a674a40b7e439a6777c21ab",
        show_dialog=True,
        cache_path="token.txt"


                                            ))

user_id = sp.current_user()["id"]
# print(user_id)

song_uris=[]

for song in title_list:
        result=sp.search(q=f"track:{song}",type="track")
        try:
                uri = result["tracks"]["items"][0]["uri"]
                song_uris.append(uri)
        except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped.")



output=sp.user_playlist_create(user="315e6heis557hwu7wwvod57w5cja",name=f"{date} - Billboard 100",public=False,)
sp.playlist_add_items(playlist_id=output["id"],items=song_uris)











