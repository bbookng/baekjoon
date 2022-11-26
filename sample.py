import pandas as pd
import requests

BASE_URL = 'https://api.themoviedb.org/3/'
top_rated_URL = "movie/top_rated?api_key=642cc263c19a3b2f7ab3f2c988a752ab&language=ko-KR&page="
URL = BASE_URL + top_rated_URL


response = requests.get(URL+f"{1}")
df = pd.DataFrame(response.json()["results"])
for i in range(2, 3):
    response = requests.get(URL+f"{i}")
    tmp = pd.DataFrame(response.json()["results"])

    df = pd.concat([df, tmp], ignore_index=True)
