import streamlit as st
st.set_page_config(
    page_title="Student Management System",
    page_icon="📖",layout="wide"
)

st.markdown("""
<h1 style='text-align:center;
color:#4CAF50;
font-size:45px;'>
🎓 Student Management System
</h1>
""", unsafe_allow_html=True)
with st.form("Student Form"):
    st.markdown("""
<style>

.stTextInput input{
    border:2px solid green;
    border-radius:10px;
    padding:8px;
}

</style>
""", unsafe_allow_html=True)
    Name = st.text_input("Name",placeholder ="Fill the your name..")
    Email = st.text_input("Email", placeholder ="Fill the your Email..")
    PassWord = st.text_input("Password", type="password")
    age = st.number_input("Age", min_value=1, max_value=100, step=1,format="%d")
    gender = st.radio("Gender",["Male","Female","Other"])
    course  = st.selectbox("Course",["Select Cource","Python","SQL","JAVA"])
    Address= st.text_area("Address")
    Agree = st.checkbox("Accept Terms and Conditions")
    submit = st.form_submit_button("Done")

if submit:
    st.success("Form Submitted Successfully!")
    st.write("Name:", Name)
    st.write("Email:", Email)
    st.write("Age:",age)
    st.write("Gender",gender)
    st.write("Course",course)