import pickle
import streamlit as st
import requests
from util import get_results
import pandas as pd
from decouple import config

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={config('API_KEY')}&language=en-US"
    data = requests.get(url)
    data = data.json()
    try:
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    except:
        return None

# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     recommended_movie_names = []
#     recommended_movie_posters = []
#     for i in distances[1:6]:
#         # fetch the movie poster
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movie_posters.append(fetch_poster(movie_id))
#         recommended_movie_names.append(movies.iloc[i[0]].title)

#     return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
movies = pickle.load(open('D:\\PRML project\\App\\movie.pkl','rb'))
movies = pd.DataFrame(movies)
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)
movie_id = movies.loc[movies['title'] == selected_movie, 'movieId'].values[0]

link = pd.read_csv('D:\\PRML project\\Dataset\\links.csv')

recommended_movies = get_results(movie_id)
for i in range(len(recommended_movies)):
    recommended_movies[i][0] = link.loc[link['movieId'] == recommended_movies[i][0], 'tmdbId'].values[0]
if st.button('Show Recommendation'):
    for lst in recommended_movies:
        if fetch_poster(lst[0]) is not None:
            print(lst)
            st.image(fetch_poster(lst[0]), width=200)
            st.text(lst[1])
        else:
            print(lst)
            continue
    st.balloons()
    st.balloons()