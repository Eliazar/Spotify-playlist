from bs4 import BeautifulSoup
import requests

BASE_URL = "https://www.billboard.com/charts/hot-100/"

bilboardDate = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

response = requests.get(f"{BASE_URL}/{bilboardDate}")
soup = BeautifulSoup(response.text, "html.parser")