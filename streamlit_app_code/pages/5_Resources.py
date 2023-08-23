import streamlit as st

st.set_page_config(
    page_title="Resources",
    page_icon="🗑️",
)

st.sidebar.image("trashbestie.png", use_column_width=True)

st.header("Resources and References")

st.markdown(
    """
    1. [Image Data](https://github.com/AgaMiko/waste-datasets-review)
    2. [Trash Separation in Germany](https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Umwelt/Abfallwirtschaft/_inhalt.html#251602) 
    3. [Yolov8](https://github.com/ultralytics/ultralytics)
    4. [Roboflow](https://roboflow.com/)
    5. [Streamlit](https://streamlit.io/)
    
"""
)

st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css?family=Chewy&display=swap'); 

            h2 {
                font-family: 'Chewy', sans-serif !important;
                font-size: 45px;
                font-weight: 500;
                color: #32CD32;
                padding-bottom: 20px;
            }

            .css-1v0mbdj {
                margin-top:-300px;
                z-index:-100;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
