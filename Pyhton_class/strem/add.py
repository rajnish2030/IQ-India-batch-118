import streamlit as st

st.set_page_config(page_title="Add Two Number", page_icon="➕")

st.title("Addition Two Number")
st.caption("Enter Two Numbers and it will return their sum.")

form = st.form("Add_form")

num1 = form.number_input("Enter Your First Number")
num2 = form.number_input("Enter Your Second Number")

submitted = form.form_submit_button("Calculate Sum")

if submitted:
    result = num1 + num2
    st.divider()
    st.metric(label="Result", value=result)