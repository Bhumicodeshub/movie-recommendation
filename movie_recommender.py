import pandas as pd

# Load the dataset
movies = pd.read_csv("movies.csv")

# Display basic information
print("Total number of movies:", len(movies))
print("\nFirst 5 movies:\n")
print(movies.head())

# Top rated movies
top_movies = movies.sort_values(by="Rating", ascending=False).head(10)

print("\nTop 10 Rated Movies:\n")
print(top_movies[["Title", "Genre", "Rating"]])
