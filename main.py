import requests, os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://www.billboard.com/charts/hot-100/"

SPOTIFY_API_KEY = os.getenv("SPOTIFY_SECRET")
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_USER_ID = os.getenv("USER_ID")

billboardDate = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

response = requests.get(f"{BASE_URL}/{billboardDate}")
soup = BeautifulSoup(response.text, "html.parser")

# To get the song We get the h3 with css id title-of-a-story under the li tag
items = soup.select("li h3#title-of-a-story")

top100Songs = [item.getText().strip() for item in items]

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_API_KEY))

responseSpotify = sp.user_playlist_create(user=SPOTIFY_USER_ID, name=f"Bilboard Top 100 {billboardDate}", public=False, collaborative=False, description=f"Billboard top 100 form {billboardDate}")

print(responseSpotify)