# import folium
# import streamlit as st

# from streamlit_folium import st_folium
# from get_curr_loc import get_curr_loc
# def home_page():
#     # center on Liberty Bell, add marker
#     m = folium.Map(location=get_curr_loc(), zoom_start=16)
#     folium.Marker(
#         get_curr_loc(), popup="Liberty Bell", tooltip="Liberty Bell"
#     ).add_to(m)

#     # call to render Folium map in Streamlit
#     st_data = st_folium(m, width=725)

# if __name__ == '__main__':
#     home_page()

import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events

def app():
    st_button = st.button("Get Location")
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
    print(result)

if __name__ == '__main__':
    app()