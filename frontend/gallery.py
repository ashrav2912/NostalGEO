from streamlit_elements import dashboard, elements, mui, html
import streamlit as st


st.title("Nostalgeo")


with elements("dashboard"):
   
    mui.Container()

    images = [
        "https://picsum.photos/300",
        "https://picsum.photos/301",
        "https://picsum.photos/302",
        "https://picsum.photos/303",
        "https://picsum.photos/304",
        "https://picsum.photos/305",
        "https://picsum.photos/306",
        "https://picsum.photos/307",
        "https://picsum.photos/308",
        "https://picsum.photos/309",
        "https://picsum.photos/310",
        "https://picsum.photos/311",
        "https://picsum.photos/312",
        "https://picsum.photos/313",
        "https://picsum.photos/314",
        "https://picsum.photos/315"
    ]



    width = 2
    height = 2
    iteration = 0
    layout = [    dashboard.Item("https://picsum.photos/300", 0, 0, 2, 2),
        dashboard.Item("https://picsum.photos/301", 2, 0, 2, 2),
        dashboard.Item("https://picsum.photos/302", 0, 2, 1, 1),]
    
    # for i in range(4):
    #     for j in range(4):
    #         x_pos = i 
    #         y_pos = j
    #         layout.append(dashboard.Item(images[iteration], i, j, width, height))
    #         iteration += 1
    
    print(layout)



    def handle_layout_change(updated_layout):
        print(updated_layout)

    with dashboard.Grid(layout, onLayoutChange=handle_layout_change):

        # for lay in layout:

        with mui.Box(
            key=layout[0]["i"],
            sx={
                "boxShadow": 1,
                "borderRadius": 2,
                "p": 2,
                "minWidth": 300,
                },
            ):
            with mui.Typography:
                html.img(src=layout[0]["i"])

        with mui.Box(
            key=layout[1]["i"],
            sx={
                "boxShadow": 1,
                "borderRadius": 2,
                "p": 2,
                "minWidth": 300,
                },
            ):
            with mui.Typography:
                html.img(src=layout[1]["i"])

#         with mui.Box(
#             key="second_item",
#             variant="outlined",
#             sx={
#             # "bgcolor": "background.paper",
#             "boxShadow": 1,
#             "borderRadius": 2,
#             "p": 2,
#             "minWidth": 300,
#             },
#         ):
   
#             with mui.Typography:
#                 html.img(src="https://picsum.photos/302", css={"object-fit": "cover"})
        
#         with mui.Box(
#             key="third_item",
#             variant="outlined",
#             sx={
#             # "bgcolor": "background.paper",
#             "boxShadow": 1,
#             "borderRadius": 2,
#             "p": 2,
#             "minWidth": 300,
#             },
#         ):
    
#             with mui.Typography:
#                 html.img(src="https://picsum.photos/301", css={"object-fit": "cover"})





# st.slider(label = "Choose a value:",
#                                   min_value = 1.0,
#                                   max_value = 10.0,
#                                  value = (3.0,4.0))

# with st.sidebar:
#     st.write("Sidebar Functionality")
#     #create a slider to hold user scores
#     new_score_rating = st.slider(label = "Choose jj value:",
#                                   min_value = 1.0,
#                                   max_value = 10.0,
#                                  value = (3.0,4.0))