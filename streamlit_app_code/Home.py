import streamlit as st

st.set_page_config(
    page_title="TrashBestie",
    page_icon="🗑️",
)

st.write("# Welcome to TrashBestie! 🗑️")

st.markdown(
    """
This is TrashBestie, your app to sort waste and reach the full potential of waste recycling.
Whether you're passionate about recycling, waste reduction, or simply curious about what's considered garbage, 
our Real-Time Garbage Object Detection app is a fun and educational way to contribute to a cleaner world.

TrashBestie scans your garbage, tells you what kind of garbage it is and which garbage bin should it be thrown into. Currently the
trash sorting follows the sorting system from Germany. TrashBestie is trained on a Yolov8 model and is trained to identify, 
`aluminium cans` 🥫, `toothbrushes` 🪥, 
`batteries` 🔋 and `pens` 🖊️. 

Ready to start? Click on the `Upload Image` or `Webcam` button and see the power of AI in action as it identifies garbage objects and 
helps you become a better waste warrior.

Remember, every step counts toward reducing waste and preserving our environment for future generations. 
Let's work together for a cleaner, greener planet!
"""
)
