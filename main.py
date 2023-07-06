import streamlit as st
from streamlit_extras import switch_page_button
st.set_page_config(initial_sidebar_state="collapsed")

with open(r"style.css") as f:
    st.markdown(f"<script>{f.read()}</script>",unsafe_allow_html=True)


st.markdown("<style>.css-aw8l5d.e1akgbir1 { visibility : hidden}</style>",unsafe_allow_html=True)

st.header("Ola! 👋")
st.divider()

st.markdown("_Please select the projects from Supervised (Regression, Classification), Unsupervised (Clustering)_")


st.session_state["Name"] = st.text_input("Enter your name : ")
st.session_state["Email"] = st.text_input("Enter your Email : ")


if st.columns(5)[2].button("Continue ..."):
    if st.session_state.Name and st.session_state.Email and "@" in st.session_state.Email : 
        switch_page_button.switch_page("Regression")
    else:    
        st.error("NOTE : please enter valid details to get Continue button!")


