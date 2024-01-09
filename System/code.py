import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies_data=pd.read_csv('F:\Projects\movieRecommendationSystem\System\movies.csv')

selected_features=['genres','keywords','tagline','cast','director']

for feature in selected_features:
  movies_data[feature]=movies_data[feature].fillna('')

combined_features=movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']

def process(movie_name):
    vectorizer = TfidfVectorizer()
    feature_vectors = vectorizer.fit_transform(combined_features)
    similarity = cosine_similarity(feature_vectors)

    list_of_all_titles = movies_data['title'].tolist()

    if movie_name is None:
        print("Error: movie_name is None")
        return []

    if not list_of_all_titles:
        print("Error: list_of_all_titles is empty")
        return []

    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles, n=1)

    if not find_close_match:
        # Handle the case where no close match is found
        temp = []
        return temp

    close_match = find_close_match[0]
    index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
    similarity_score = list(enumerate(similarity[index_of_the_movie]))
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    i = 1
    movieList = []
    for movie in sorted_similar_movies:
        index = movie[0]
        title_from_index = movies_data[movies_data.index == index]['title'].values[0]
        if i < 21:
            movieList.append(title_from_index)
            i += 1

    return movieList

  