from bs4 import BeautifulSoup
import requests

BASE_URL = "https://www.billboard.com/charts/hot-100/"

bilboardDate = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

response = requests.get(f"{BASE_URL}/{bilboardDate}")
soup = BeautifulSoup(response.text, "html.parser")

# To get the song We get the h3 with css id title-of-a-story under the li tag
items = soup.select("li h3#title-of-a-story")

top100Songs = [item.getText().strip() for item in items]