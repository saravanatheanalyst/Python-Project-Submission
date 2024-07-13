Hello Team,

Please find my code explanation.

1) fetch_movie_data(genre)

- Fetched movie data from IMDb based on the specified genre.
- Constructs the URL for the IMDb search page based on the genre.
- Sends a GET request to the URL with appropriate headers.
- Parses the HTML content using BeautifulSoup.
- Extracts movie titles and genres from the JSON data embedded in the HTML.
- Returns a pandas DataFrame containing the movie titles and genres.


2) save_to_csv(movies, filename='movies.csv')

- Saves the fetched movie data to a CSV file.
- Converts the DataFrame to a CSV file.
- Saves the file with the specified filename.


3) load_and_suggest_movies(genre, filename='movies.csv')

- Loads movie data from the CSV file and provides a random movie suggestion.
- Reads the CSV file into a DataFrame.
- Filters the movies based on the specified genre.

4) Introduced suggestion as else to achieve random movie

- Randomly selects a movie from the filtered list and prints the suggestion.

5) main()

-Main function to run the script.

Expected Output :
Prompts the user to enter a movie genre.
Fetches movie data based on the entered genre.
Saves the fetched data to a CSV file.
Provides a random movie suggestion from the fetched data.

Achieved Output : 

Enter a movie genre: thriller
Page fetched successfully
Data saved to movies.csv
Random movie suggestion for the genre 'thriller':
Title: 'Dark Matter', Genre: ['Drama', 'Sci-Fi', 'Thriller']
Movies Fetched Successfully
