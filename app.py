import os

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    layout="wide",
    page_title="LA Connect — Rail + Bus Prototype",
    page_icon="🚆",
)

st.title("LA Connect")
st.caption(
    "A concept rider app for the 405 Rail + Bus Feeder Network — "
    "rail for speed, buses for the last mile, local perks for every ride."
)

HTML_PATH = os.path.join(os.path.dirname(__file__), "la_connect_prototype.html")

with open(HTML_PATH, "r", encoding="utf-8") as f:
    prototype_html = f.read()

components.html(prototype_html, height=900, scrolling=True)

with st.sidebar:
    st.markdown("**Concept prototype** — all data shown is demo data.")
    st.markdown("**Screens in this prototype:**")
    st.markdown(
        "- Onboarding\n"
        "- Home\n"
        "- Trip Planner\n"
        "- Live Trip\n"
        "- Rewards\n"
        "- Reward Detail\n"
        "- Wallet\n"
        "- Community\n"
        "- Profile"
    )
