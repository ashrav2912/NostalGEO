import streamlit as st
from streamlit_elements import dashboard, elements, mui, html

import random # For testing


def gallery():

    #st.set_page_config(layout="wide") # Smaller margins

    # st.title("Nostalgeo") 

    # Time Slider
    year = st.slider("Please select a rating range", min_value=2000, max_value=2015, value=(2000, 2015))

    print(year)

    # Material UI Dashboard

    with elements("dashboard"):
    
        # Local images for gallery
        images = [
            ["https://picsum.photos/301", 2000],
            ["https://picsum.photos/302", 2001],
            ["https://picsum.photos/303", 2002],
            ["https://picsum.photos/304", 2003],
            ["https://picsum.photos/305", 2004],
            ["https://picsum.photos/306", 2005],
            ["https://picsum.photos/307", 2006],
            ["https://picsum.photos/308", 2007],
            ["https://picsum.photos/309", 2008],
            ["https://picsum.photos/310", 2009],
            ["https://picsum.photos/311", 2010],
            ["https://picsum.photos/312", 2011],
            ["https://picsum.photos/313", 2012],
            ["https://picsum.photos/314", 2013],
            ["https://picsum.photos/315", 2015],
            ["https://picsum.photos/316", 2015],
            ["https://picsum.photos/317", 2015],
        ]

        width = 2
        height = 2
        iteration = 0
        layout = []
        data = []
        
        offset = 0
        y_pos = 0
        
        for iteration in range(len(images)):
            
            print(int(images[iteration][1])) # debugging


            if (images[iteration][1] >= year[0] and images[iteration][1] <= year[1]):
                
                x_pos = offset * width
                
                if (len(layout) % 5 == 0):
                    y_pos += 2
                    x_pos = 0
                    offset = 0

                dash = dashboard.Item(images[iteration][0], x_pos, y_pos, width, height)
                layout.append(dash)
                data.append([dash, round(random.uniform(0, 10), 2)])
                
                offset += 1

        print(layout)

        def handle_layout_change(updated_layout):
            print() # Callback for saving gallery layout.

        with dashboard.Grid(layout, onLayoutChange=handle_layout_change):

            for lay in layout:
                html.img(src=lay["i"], css={"object-fit": "cover"}, key=lay["i"])

