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
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

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
if st.button('Show Recommendation'):
    recommended_movies = get_results(movie_id)
    for lst in recommended_movies:
        st.text(lst[1])
        st.image(fetch_poster(lst[0]))
    

    # recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    # col1, col2, col3, col4, col5 = st.beta_columns(5)
    # with col1:
    #     st.text(recommended_movie_names[0])
    #     st.image(recommended_movie_posters[0])
    # with col2:
    #     st.text(recommended_movie_names[1])
    #     st.image(recommended_movie_posters[1])

    # with col3:
    #     st.text(recommended_movie_names[2])
    #     st.image(recommended_movie_posters[2])
    # with col4:
    #     st.text(recommended_movie_names[3])
    #     st.image(recommended_movie_posters[3])
    # with col5:
    #     st.text(recommended_movie_names[4])
    #     st.image(recommended_movie_posters[4])