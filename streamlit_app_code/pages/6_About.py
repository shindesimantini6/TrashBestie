import streamlit as st

st.set_page_config(
    page_title="TrashBestie",
    page_icon="🗑️",
)

st.sidebar.image("trashbestie.png", use_column_width=True)

st.header("Who are we?")

st.write("""
         We are [My](https://www.linkedin.com/in/my-huynh/) ([![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/VanMyHu)), 
         [Helge](https://www.linkedin.com/in/helge-r%C3%B6lleke-a3474a135/) ([![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/helge1991)) and [Simantini](https://www.linkedin.com/in/simantini-shinde-60b23a47/) ([![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/shindesimantini6/)).
         
         Ethusiatic Data Scientists, wanting to bring about positive change with data and machine learning.
                 """)

st.header("Why TrashBestie 🗑️?")

st.write("""
    We created TrashBestie as a part of [GirlsInTech Hackathon](https://hackfortheenvironmentwith-git.devpost.com/). We were inspired by the positive impact topics presented by the hackathon and wanted to 
         explore our abilities by creating a project which had the potential to create positive change.          
""")


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
