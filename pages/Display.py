import streamlit as st
from streamlit_extras.switch_page_button import switch_page 
import mysql.connector as mysql

st.set_page_config(initial_sidebar_state="collapsed")

def create_connection():
    mydb = mysql.connect(
        host="sql6.freemysqlhosting.net",
        user="sql6630809", #enter username here
        password="luzGhrQeWj", #enter password here
        database="sql6630809"
    )
    return mydb



def insert_details(name, email, reg_name, class_name, unsuper_name, feed_back):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO projects (name, email, reg_name, cla_name, uns_name, feed_back) VALUES ('{name}','{email}','{reg_name}','{class_name}','{unsuper_name}','{feed_back}');")
    connection.commit()
    connection.close()

st.markdown("""
<style>
    .css-erpbzb.edgvbvh3{
    visibility : hidden;
    }
    .css-aw8l5d.e1akgbir1{
    visibility : hidden;
    }
</style>""",unsafe_allow_html=True)

st.columns(3)[2].header(st.session_state.Name.capitalize())
st.divider()

st.write("Supervised (Regression) Project : ")
st.divider()
st.write(st.session_state.regression)
st.divider()

st.write("Supervised (Classification) Project : ")
st.divider()
st.write(st.session_state.classification)
st.divider()

st.write("Unsupervised (Clustering) Project : ")
st.divider()
st.write(st.session_state.unsuper)
st.divider()

st.divider()
st.write("Fill your feedback below !")
st.divider()
slider_value = st.slider("FeedBack ( How was your experience with the course :)",
                            min_value=1,
                            max_value=5
                            )




col1, col2 = st.columns(2)

with col1 :
    st.write("Please press the button to recieve the mail.")

with col2 :
    if st.button("Recieve Mail"):
        #inserting the values to database.
        insert_details(st.session_state.Name, st.session_state.Email, st.session_state.regression.split(":")[1], st.session_state.classification.split(":")[1], st.session_state.unsuper.split(":")[1], slider_value)
        st.balloons()
        st.success("Mail sent successfully!")


