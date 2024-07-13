import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

def fetch_movie_data(genre):
    url = f"https://www.imdb.com/search/title/?genres={genre}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data from IMDb: {e}")
        return None

    if response.status_code == 200:
        print("Page fetched successfully")
    else:
        print(f"Failed to fetch page: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    # movies = []

    movie_list = []
    genre_list = []

    try:
        # movie_containers = soup.find_all('h3', class_='ipc-title__text')
        # print(movie_containers)
        # if not movie_containers:
        #     print("No movie containers found")
        #     return None

        movie_element = soup.find('script', id='__NEXT_DATA__')
        if movie_element:
            title_data = json.loads(movie_element.contents[0])
            title_text = title_data['props']['pageProps']['searchResults']['titleResults']['titleListItems']

            for movie_entry in title_text:
                movie_list.append(movie_entry['titleText'])
                genre_list.append(movie_entry['genres'])

            # for movie, genre in zip(movie_list, genre_list):
            #     print(f"Movie: {movie}, Genre: {genre}")

            movie_table = pd.DataFrame({'Title': movie_list, 'Genre': genre_list})
            # print(movie_table)

        else:
            print("Title element not found.")

        # for container in movie_containers:
        #     title_element = container.h3.a if container.h3 else None
        #     genre_element = container.find('span', class_='genre')
        #
        #     if title_element and genre_element:
        #         title = title_element.text
        #         genre_text = genre_element.text.strip()
        #         movies.append((title, genre_text))
    except AttributeError as e:
        print(f"Error parsing data: {e}")
        return None

    return movie_table


def save_to_csv(movies, filename='movies.csv'):
    # df = pd.DataFrame(movies, columns=['Title', 'Genre'])
    movies.to_csv(filename, index=False)
    print(f"Data saved to {filename}")


def load_and_suggest_movies(genre, filename='movies.csv'):
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return None
    except pd.errors.EmptyDataError as e:
        print(f"No data: {e}")
        return None

    genre_movies = df[df['Genre'].str.contains(genre, case=False)]
    if genre_movies.empty:
        print(f"No movies found for the genre: {genre}")
    else:
        suggestion = genre_movies.sample().iloc[0]
        print(f"Random movie suggestion for the genre '{genre}':")
        print(f"Title: '{suggestion['Title']}', Genre: {suggestion['Genre']}")


def main():
    genre = input("Enter a movie genre: ").strip().lower()
    movies = fetch_movie_data(genre)

    if not movies.empty:
        save_to_csv(movies)
        load_and_suggest_movies(genre)
        print("Movies Fetched Successfully")
    else:
        print("No movies fetched.")


if __name__ == "__main__":
    main()
