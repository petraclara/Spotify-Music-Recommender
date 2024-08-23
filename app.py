import pickle
import streamlit as st
import pandas as pd
from spotify import hybrid_recommendations


music= pickle.load(open('music.pkl', 'rb'))

# Streamlit Interface
st.title("Spotify Song Recommender")
input_song_name = st.selectbox("Type song", music['Track Name'])
num_recommendations = st.number_input("Number of songs",min_value=0,max_value=20,value=5)
if st.button("Get Recommendations"):
        
        recommendations =hybrid_recommendations(input_song_name, num_recommendations = num_recommendations)
        st.write("Recommended Songs:")
        st.write(recommendations)

st.sidebar.title("Playlist:")

playlist = st.sidebar.selectbox("Select a playlist", ["All"])

# if playlist == "All":
           
#         st.dataframe(music)

