import datetime
from typing import List
import numpy as np
import streamlit as st

from viz import image_show, daily_scatter, weekday_bar
from os import listdir
from os.path import isfile, join
import random
import time


def write():

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
