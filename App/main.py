import pickle
import streamlit as st
import requests
from util import get_results, styled_text
import pandas as pd
from decouple import config
from streamlit_extras.colored_header import colored_header
from streamlit_extras.customize_running import center_running
import time
import gdown
import os

# START CODE FOR BACKGROUND
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://res.cloudinary.com/dlsakk1pf/image/upload/v1713611574/image_vedwte.jpg");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""
st.markdown(background_image, unsafe_allow_html=True)
#END CODE FOR BACKGROUND
api_key = st.secrets["API_KEY"]

def poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    data = requests.get(url)
    data = data.json()
    try:
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    except:
        return None

def example():
    click = st.button("Restart the app")
    if click:
        center_running()
        time.sleep(0)

example()

# st.header('Movie Recommender System')
colored_header(
        label="Movie Recommender System",
        description="",
        color_name="blue-70",
    )

# url = 'https://drive.google.com/file/d/1K7p-14gFeUEvkAUmXXWRpaKsp5btyDly/view?usp=sharing'

# # Download the file to a local path
# output = 'movies.pkl'
# gdown.download(url, output, quiet=False)

# # Load the pickle file
# movies = pickle.load(open(output, 'rb'))
current_dir = os.getcwd()

# Construct the relative path to the pickle file
file_path = os.path.join(current_dir, 'movie.pkl')

# Load the pickle file
with open(file_path, 'rb') as file:
    movies = pickle.load(file)


# movies = pickle.load(open('https://drive.google.com/file/d/1K7p-14gFeUEvkAUmXXWRpaKsp5btyDly/view?usp=sharing','rb'))
movies = pd.DataFrame(movies)
movie_list = movies['title'].values


selected_movie = st.selectbox(
    "Select a movie",
    movie_list
)

movie_id = movies.loc[movies['title'] == selected_movie, 'movieId'].values[0]

link = pd.read_csv('https://raw.githubusercontent.com/Advaitgaur004/PRML_Project/main/Dataset/links.csv')

recommended_movies = get_results(movie_id)[:6]
for i in range(len(recommended_movies)):
    recommended_movies[i][0] = link.loc[link['movieId'] == recommended_movies[i][0], 'tmdbId'].values[0]

if st.button('Show Recommendation'):
    st.write(styled_text('Top Picks For You', 'Scriptina',24,'white'),unsafe_allow_html=True)
    # Create columns for horizontal layout
    top_col1, top_col2, top_col3 = st.columns(3)
    bottom_col1, bottom_col2,bottom_col3 = st.columns(3)

    # Display top row images
    for idx, lst in enumerate(recommended_movies[:3]):
        if poster(lst[0]) is not None:
            with eval(f"top_col{idx + 1}"):
                st.image(poster(lst[0]), width=200)
                st.write(styled_text(lst[1], 'Lobster',20,'white'),unsafe_allow_html=True)
        else:
            continue

    # Display bottom row images
    for idx, lst in enumerate(recommended_movies[3:]):
        if poster(lst[0]) is not None:
            with eval(f"bottom_col{idx + 1}"):
                st.image(poster(lst[0]), width=200)
                st.write(styled_text(lst[1], 'Lobster',20,'white'),unsafe_allow_html=True)
        else:
            continue

    st.balloons()
    st.balloons()
