import streamlit as st

# Add a main title at the top of the app
st.title("My Streamlit App")

# Create two columns
col1, col2 = st.columns(2)

# Add headers and text to the columns
with col1:
    st.header("Column 1")
    st.write("Hello")

with col2:
    st.header("Column 2")
    st.write("World")

# Add an expander below the columns
with st.expander("Expand for more information"):
    st.write("Here you could put in some really, really explanatory stuff.")
