import requests
import json


provider_ids = {
    'watcha': 97,
    'wavve': 356,
    'disney': 337,
    'netflix': 8
}


def make_url(url, params):
    for key, value in params.items():
        url = url + f'&{key}={value}'
    return url


# Create your views here.
def get_movies():
    movies = []
    movie_ids = []
    api_key = "642cc263c19a3b2f7ab3f2c988a752ab"

    # URL에 api_key를 넣어준다.

    page_num = 0
    params = {
        'api_key': api_key,
        'with_watch_providers': 8,
        'watch_region': 'KR',
        'language': 'ko',
        'page': page_num
    }
    URL = f'https://api.themoviedb.org/3/discover/movie?'
    # json으로 데이터를 받고, 결과 dic list를 results변수에 넣는다

    # ott별 검색
    for key, value in provider_ids.items():
        for page_num in range(1, 5):
            params['with_watch_providers'] = value  # 제공사 바꾸기
            params['page'] = page_num
            maked_url = make_url(URL, params)  # ott url 제공

            # 받아오기
            response = requests.get(maked_url).json()  # 받아오기
            print(response)
            results = response.get('results')  # 안에꺼만 추출

            for result in results:
                # 이미 들어있는지 없는지 판별하기

                if result['id'] not in movie_ids:
                    movie_ids.append(result['id'])
                    main_result = dict()
                    main_result['model'] = 'movies.movie'
                    main_result['pk'] = result['id']

                    # 새로운 딕트에 저장 후 append
                    new_result = dict()
                    # 초기화
                    # new_result['pk'] = result['id']
                    new_result['title'] = result['title']
                    new_result['genres'] = result['genre_ids']
                    new_result['overview'] = result['overview']
                    new_result['release_date'] = result['release_date']
                    new_result['popularity'] = result['popularity']
                    new_result['adult'] = result['adult']
                    new_result['vote_count'] = 0  # result['vote_count']
                    new_result['vote_average'] = 0  # result['vote_average']
                    new_result['backdrop_path'] = result['backdrop_path']
                    new_result['poster_path'] = result['poster_path']
                    new_result['original_language'] = result['original_language']
                    new_result['original_title'] = result['original_title']
                    # OTT
                    new_result['otts'] = [value]
                    # new_result['netflix'] = False
                    # new_result['watcha'] = False
                    # new_result['wavve'] = False
                    # new_result['disney'] = False

                    # new_result[key] = True
                    main_result['fields'] = new_result
                    # 저장
                    movies.append(main_result)

                # 들어있는 경우
                else:
                    # OTT
                    for movie in movies:
                        if result.get('id') == movie.get('pk'):
                            if not value in movie['fields']['otts']:
                                print(movie['fields']['title'])
                                movie['fields']['otts'].append(value)

    # # 받아오기
    # maked_url = make_url(URL, params)
    # response = requests.get(maked_url).json()

    # # 데이터 정제
    # results = response.get('results')

    # json 저장하기
    file_path = "../all_2.json"  # 주소

    with open(file_path, 'w', encoding="UTF-8") as outfile:
        json.dump(movies, outfile, indent=4, ensure_ascii=False)
    print(len(movies))
    return


get_movies()