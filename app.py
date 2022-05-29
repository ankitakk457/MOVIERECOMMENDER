import pickle
import pandas as pd
import streamlit as st
import requests
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_0yfsb3a1.json")


with st.container():
    st.subheader("Hi, I am Ankita Kumari :wave:")
    st.title("Welcome to my Movie Recommender System")
    st.write(
        ""
    )

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Lets learn about how this system works: ")
        st.write("##")
        st.write(
            """
            The main goal of this machine learning project was to build a recommendation engine that recommends movies to users.We had developed an Content Based Recommendation System.
            """
        )
        st.write("##")
        st.write("##")
        st.header("What is a Recommendation System?")
        st.write("##")
        st.write(
            """
            A recommendation system is a subclass of Information filtering Systems that seeks to predict the rating or the preference a user might give to an item. In simple words, it is an algorithm that suggests relevant items to users. Eg: In the case of Netflix which movie to watch, In the case of e-commerce which product to buy, or In the case of kindle which book to read, etc.
            """
        )
        st.write("##")
        st.write("##")
        st.write("##")



    with right_column:
        st.write("##")
        st.write("##")
        st.write("##")
        st.write("##")

        st_lottie(lottie_coding, height=300, key="coding")

        st.write("##")
        st.write("##")

        st.header("Content Based Filtering")
        st.write("##")
        st.write(
            """
            This type of filter does not involve other users if not ourselves. Based on what we like, the algorithm will simply pick items with similar content to recommend us.

In this case there will be less diversity in the recommendations, but this will work either the user rates things or not. If we compare this to the example above, maybe user B potentially likes dark comedy but he/she will never know, unless he/she decides to give it a try autonomously, because this filter will only keep recommending dystopian movies or similar. Of course there are many categories we can calculate the similarity on: in the case of movies we can decide to build our own recommender system based on genre only, or maybe we want to include director, main actors and so on.
        """
        )



def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
       movie_index = movies[movies['title'] == movie].index[0]
       distances = similarity[movie_index]
       movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]


       recommended_movies = []
       recommended_movies_posters = []

       for i in movies_list:
           movie_id = movies.iloc[i[0]].movie_id

           recommended_movies.append(movies.iloc[i[0]].title)

           recommended_movies_posters.append(fetch_poster(movie_id))
       return recommended_movies,recommended_movies_posters


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)


similarity = pickle.load(open('similarity.pkl','rb'))
st.write("##")
st.write("##")
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
'How would you like to be contracted?',
movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

