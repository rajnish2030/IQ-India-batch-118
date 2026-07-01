import streamlit as st

st.set_page_config(page_title="Student Registration", page_icon="🎓")
st.title("🎓 Student Registration Form")
with st.form("student_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    age = st.number_input("Age", min_value=1, max_value=100)

    gender = st.radio(
        "Gender",
        ["Male", "Female", "Other"]
    )
    course = st.selectbox(
        "Select Course",
        [
            "Python",
            "Java",
            "MySQL",
            "Data Science",
            "Web Development"
        ]
    )

    skills = st.multiselect(
        "Skills",
        [
            "Python",
            "HTML",
            "CSS",
            "JavaScript",
            "SQL"
        ]
    )

    address = st.text_area("Address")
    agree = st.checkbox("I accept the terms and conditions")
    submit = st.form_submit_button("Register")
if submit:
    if not agree:
        st.error("Please accept the terms and conditions.")
    else:
        st.success("Registration Successful ✅")

        st.write("## Student Details")

        st.write("👤 Name:", name)
        st.write("📧 Email:", email)
        st.write("📱 Phone:", phone)
        st.write("🎂 Age:", age)
        st.write("🚻 Gender:", gender)
        st.write("📚 Course:", course)
        st.write("💻 Skills:", ", ".join(skills))
        st.write("🏠 Address:", address)