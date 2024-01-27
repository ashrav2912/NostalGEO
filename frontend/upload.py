import streamlit as st
import os

def upload_page():
    uploaded_files = st.file_uploader(label = "submit", accept_multiple_files=True, type=['png', 'jpg', 'jpeg', 'mp4', 'mp3', 'wav', 'gif'])
    for uploaded_file in uploaded_files:
        # bytes_data = uploaded_file.read()
        # st.write("filename:", uploaded_file.name)
        # st.write(bytes_data)
        print(type(uploaded_files))
        print(uploaded_files)
        for uploaded_file in uploaded_files:
            print(type(uploaded_file))
        if uploaded_file.type == "image/jpeg":
            st.write("Image: ", uploaded_file.name)
        elif uploaded_file.type == "video/mp4":
            st.write("Video", uploaded_file.name)
        elif uploaded_file.type == "audio/mp3":
            st.write("Audio", uploaded_file.name)

        save_dir = "uploads"
  
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        path_array = []
        for uploaded_file in uploaded_files:
            save_path = os.path.join(save_dir, uploaded_file.name)
            path_array.append(save_path)
            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success(f"File saved successfully at: {save_path}")
        print(path_array)

if __name__ == '__main__':
    upload_page()