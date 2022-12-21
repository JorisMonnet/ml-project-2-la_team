import streamlit as st
from helper_website import *
import time

getPage("Step 3: Evaluating the model.", False, True)

st.markdown(
    """
You don’t have to know much about machine learning to understand how it works. There are several interpretability techniques that can show what the model is using to make its predictions.

One example is gradCAM"""
) #TODO explain gradcam

st.image(getGradcam("Date_original"))

st.write("""Lets see what gradCAM shows for our model""")

if st.button("Run GradCAM !"):
    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1)

    st.image(getGradcam("Dot"))
    st.markdown(
        """
    WOAH that does not look right.
    The model is “cheating” by using the red dot to determine pneumonia…that would defeat the purpose of the model.

    > TIP: a model with near 100% performance is suspicious.
    """
    )