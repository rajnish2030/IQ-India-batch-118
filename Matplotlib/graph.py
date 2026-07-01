# import matplotlib.pyplot as plt

# months = ["Jan", "Feb", "Mar", "Apr", "May"]
# sales = [100, 150, 120, 180, 200]

# plt.plot(months, sales)

# plt.title("Monthly Sales")
# plt.xlabel("Months")
# plt.ylabel("Sales")

# plt.show()

# import streamlit as st
# import matplotlib.pyplot as plt

# st.set_page_config(page_title="Graph",page_icon="📈")

# x = [1, 2, 3, 4, 5]
# y = [10, 20, 15, 25, 30]

# fig, ax = plt.subplots()
# ax.plot(x, y)
# ax.set_title("My First Graph")

# st.title("Statistics Graph")
# st.pyplot(fig)

import plotly.express as px

fig = px.line(x=[1,2,3,4], y=[10,20,15,30], title="Sales Graph")
fig.show()