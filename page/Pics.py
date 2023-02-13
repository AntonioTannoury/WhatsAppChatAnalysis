import streamlit as st
from viz import image_show


def write():

    st.markdown(
        """
        # When Random Love Hits
        """
    )
    image = image_show(height=800)
    st.plotly_chart(image, theme="streamlit", use_container_width=True)
    _, _, col3, _, _ = st.columns(5)
    with col3:
        st.button("Don't push")
