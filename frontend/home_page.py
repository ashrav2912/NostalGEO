import folium
import streamlit as st
from bokeh.models import Button, CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events

from streamlit_folium import st_folium
from get_curr_loc import get_curr_loc
import requests
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
        print(latlong)
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
    count = 0
    response = requests.get("http://localhost:3000/get_markers")
    print("Response: ", response.text)
    print("Type: ", type(response.text))
    folium.Marker(
    latlong, popup="Your location", tooltip="Your location"
).add_to(m) 
    folium.Marker(
    [37.7749, -122.4194], popup="Your location", tooltip="Your location").add_to(m)
    st_data = st_folium(m, width=725)

if __name__ == '__main__':
    home_page()

