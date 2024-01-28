import streamlit as st
import os
from geopy.geocoders import Nominatim
from get_curr_loc import get_loc
import requests

def upload_page():
    uploaded_files = st.file_uploader(label = "submit", accept_multiple_files=True, type=['png', 'jpg', 'jpeg', 'mp4', 'mp3', 'wav', 'gif'])
    save_dir = "uploads"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    path_array = []
    for uploaded_file in uploaded_files:
        save_path = os.path.join(save_dir, uploaded_file.name)
        path_array.append(save_path)
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.image(save_path, width=300)
        #st.success(f"File saved successfully at: {save_path}")
    print(path_array)
    location = st.chat_input("Enter location")
    print("Location: ", location)
    if location:
        lat = Nominatim(user_agent="NostalGEO").geocode(location).raw['lat']
        long = Nominatim(user_agent="NostalGEO").geocode(location).raw['lon']
        print("Latlong: ", [lat, long])
        response = requests.get("http://localhost:3000/create_marker?location="+str(lat)+","+str(long))
        print(response)
if __name__ == '__main__':
    upload_page()