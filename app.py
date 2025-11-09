# import streamlit as st
# import pickle
# import pandas as pd

# def recommend(movie):
#         movie_index = movies_list[movies_list['title'] == movie].index[0]
#         distances = similarity[movie_index]
#         movies_list = sorted(list(enumerate(distances)), reverse = True , key = lambda x:x[1])[1:6]
        
#         recommended_movies = []
#         for i in movies_list:
#              recommended_movies.append(movies_list.iloc[i[0]].title)
#         return recommended_movies




# movies_list = pickle.load(open('movies.pkl' , 'rb'))
# movies_list = movies_list['title'].values

# similarity = pickle.load(open('similarity.pkl' , 'rb'))

# st.title('Movie recommendation system')
# selected_Movie_name = st.selectbox(
#     'Search Movies' , movies_list
# )

# if st.button('Recommend'):
#     recommendations = recommend(selected_Movie_name)
#     for i in recommendations:
#         st.write(i)


import streamlit as st
import pickle
import pandas as pd

# Load the movies dataframe
movies_df = pickle.load(open('movies.pkl', 'rb'))

# Load the similarity matrix (make sure this file is not too large)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation function
def recommend(movie):
    try:
        movie_index = movies_df[movies_df['title'] == movie].index[0]
    except IndexError:
        return ["Movie not found. Please try another title."]
    
    distances = similarity[movie_index]
    
    # Get indices of top 5 similar movies (excluding itself)
    movie_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movie_indices:
        recommended_movies.append(movies_df.iloc[i[0]]['title'])
    
    return recommended_movies

# Streamlit UI
st.title('🎬 Movie Recommendation System')

selected_movie_name = st.selectbox(
    '🔍 Search for a movie:',
    movies_df['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    st.subheader("You might also like:")
    for i in recommendations:
        st.write("👉", i)

