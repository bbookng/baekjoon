import pandas as pd
import requests

URL = 'https://api.themoviedb.org/3/movie/top_rated?api_key=642cc263c19a3b2f7ab3f2c988a752ab&language=ko-KR&page='

response = requests.get(URL+f"{1}")
df = pd.DataFrame(response.json()["results"])


for i in range(2, 3):
    response = requests.get(URL+f"{i}")
    tmp = pd.DataFrame(response.json()["results"])

    df = pd.concat([df, tmp], ignore_index=True)
    print(i)

df = df[['adult', 'backdrop_path', 'genre_ids', 'id', 'original_language', 'overview', 'popularity', 'poster_path',
       'release_date', 'title', 'video', 'vote_average', 'vote_count']]
df.to_csv("data.csv", encoding='cp949')