import streamlit as st
from viz import metrics, image_show
from os import listdir
from os.path import isfile, join
import random
import time


def write():
    """Used to write the page in the app.py file"""

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            # When Random Love Hits

            ### It hits hard
            ### So Reality would look like a order Chaos 
            .
            ### It breaks rules
            ### So an Ostriche can become a Flamingo 🦩

            """
        )

    with col2:
        mypath = "pics"
        onlyfiles = [
            mypath + "/" + f for f in listdir(mypath) if isfile(join(mypath, f))
        ]
        random_path = random.choice(onlyfiles)
        image = image_show(random_path)
        st.plotly_chart(image, theme="streamlit", use_container_width=True)

    st.sidebar.header("Select the Metrics you want to see")
    max = st.sidebar.checkbox("Maximum", value=True)
    min = st.sidebar.checkbox("Minimum", value=True)
    mean = st.sidebar.checkbox("Average", value=True)

    names = ["Perlei", "Love", "Antonio"]
    colors = ["yellow", "red", "blue"]

    # cols = st.columns(3)
    # for idx, col in enumerate(cols):
    #     with col:
    #         title = f"<h1 style='text-align: center; color: {colors[idx]};'>{names[idx]}</h1>"
    #         st.markdown(title, unsafe_allow_html=True)
    #         if max:
    #             max_values = metric_values("max")
    #             max_text = text_format(color=colors[idx],name=max_values[''])
    #             st.markdown(title, unsafe_allow_html=True)

    #         if min:
    #             min_fig = metric("min")
    #             st.plotly_chart(min_fig, theme="streamlit", use_container_width=True)
    #         if mean:
    #             mean_fig = metric("mean")
    #             st.plotly_chart(mean_fig, theme="streamlit", use_container_width=True)

    col11, col12, col13 = st.columns(3)

    with col11:
        title = "<h1 style='text-align: center; color: yellow;'>Perlei</h1>"
        st.markdown(title, unsafe_allow_html=True)
    with col12:
        title = "<h1 style='text-align: center; color: red;'>Love</h1>"
        st.markdown(title, unsafe_allow_html=True)
    with col13:
        title = "<h1 style='text-align: center; color: blue;'>Antonio</h1>"
        st.markdown(title, unsafe_allow_html=True)

    metrics_figs = metrics(max=max, min=min, mean=mean)
    st.plotly_chart(metrics_figs, theme="streamlit", use_container_width=True)

    # if max:
    #     max_fig = metric("max")
    #     st.plotly_chart(max_fig, theme="streamlit", use_container_width=True)
    # if min:
    #     min_fig = metric("min")
    #     st.plotly_chart(min_fig, theme="streamlit", use_container_width=True)
    # if mean:
    #     mean_fig = metric("mean")
    #     st.plotly_chart(mean_fig, theme="streamlit", use_container_width=True)


#%%
