import folium
import streamlit as st
from bokeh.models import Button, CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
from streamlit_folium import st_folium
from get_curr_loc import get_curr_loc
import requests
from streamlit_modal import Modal
from gallery import gallery

import folium
from jinja2 import Template

# def home_page():
#     # center on Liberty Bell, add marker
#     m = folium.Map(location=get_curr_loc(), zoom_start=16)
#     folium.Marker(
#         get_curr_loc(), popup="Your location", tooltip="Your location"
#     ).add_to(m)

#     # call to render Folium map in Streamlit
#     st_data = st_folium(m, width=725)

# if __name__ == '__main__':
#     home_page()

st.set_page_config(
        page_title="My Page Title",
        layout="wide"
)


def location():
    loc_button = Button(label="Get Location")
    loc_button.js_on_event("button_click", CustomJS(code="""
        navigator.geolocation.getCurrentPosition(
            (loc) => {
                document.dispatchEvent(new CustomEvent("GET_LOCATION", {detail: {lat: loc.coords.latitude, lon: loc.coords.longitude}}))
            }
        )
        """))
    result = streamlit_bokeh_events(
        loc_button,
        events="GET_LOCATION",
        key="get_location",
        refresh_on_update=False,
        override_height=75,
        debounce_time=0)
    # st.bokeh_chart(result)
    if(result):
        latlong = [result['GET_LOCATION']['lat'], result['GET_LOCATION']['lon']]
        # print(latlong)
        return latlong
    else:
        return [0,0]
    
def home_page():
    # center on Liberty Bell, add marker
    latlong = location()

    m = folium.Map(location=latlong, zoom_start=16)
    # folium.Marker(
    #     app(), popup="Your location", tooltip="Your location"
    # ).add_to(m)

    # call to render Folium map in Streamlit
    

    # Modify Marker template to include the onClick event
    
    count = 0
    response = requests.get("http://localhost:3000/get_markers")
    # print("Response: ", response.text)
    # print("Type: ", type(response.text))
    json_list = eval(response.text)
    # print("Json list: ", json_list)
    # print(type(json_list) , "wrong")
    
    # Current Location
    print(folium.Marker(latlong, popup="Your location", tooltip="Your location").add_to(m)) 
    
    for ele in json_list:
        coords = eval(ele['location'])
        coords = list(coords)
        folium.Marker(coords, popup="Location", tooltip="location").add_to(m)
    
    
    st_data = st_folium(m, width=725)
    print(st_data["last_object_clicked_popup"])
    modal = Modal(key="Demo Key",title="Pop-up")
    if(st_data["last_object_clicked_popup"] == "Your location"):
        gallery()
# with modal.container():
#     st.markdown('testtesttesttesttesttesttesttest')

if __name__ == '__main__':
    home_page()

