import pickle
import streamlit as st
import requests
from util import get_results, styled_text
import pandas as pd
from decouple import config
from streamlit_extras.colored_header import colored_header
from streamlit_extras.customize_running import center_running
import time



# START CODE FOR BACKGROUND
import base64

@st.cache_data()
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .main {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    background-attachment: local;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('D:\\PRML project\\Img\\image.jpg')
#END CODE FOR BACKGROUND


def poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={config('API_KEY')}&language=en-US"
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
movies = pickle.load(open('D:\\PRML project\\App\\movie.pkl','rb'))
movies = pd.DataFrame(movies)
movie_list = movies['title'].values


selected_movie = st.selectbox(
    "Select a movie",
    movie_list
)



movie_id = movies.loc[movies['title'] == selected_movie, 'movieId'].values[0]

link = pd.read_csv('D:\\PRML project\\Dataset\\links.csv')

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
                st.text(lst[1])
        else:
            continue

    # Display bottom row images
    for idx, lst in enumerate(recommended_movies[3:]):
        if poster(lst[0]) is not None:
            with eval(f"bottom_col{idx + 1}"):
                st.image(poster(lst[0]), width=200)
                st.text(lst[1])
        else:
            continue

    st.balloons()
    st.balloons()
