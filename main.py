import streamlit as st
import pandas

col1 ,col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Bio")   
    content = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Tristique risus nec feugiat in. 
    Mattis aliquam faucibus purus in massa. Etiam non quam lacus suspendisse faucibus interdum. Suspendisse sed nisi lacus sed viverra tellus.
    """
    st.write(content)

content2 = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Tristique risus nec feugiat in. 
        Mattis aliquam faucibus purus in massa. Etiam non quam lacus suspendisse faucibus interdum. Suspendisse sed nisi lacus sed viverra tellus.
        """
st.write(content2)

df = pandas.read_csv("data.csv", sep =";")

col3 ,empty_col,col4 = st.columns([1.5,0.5,1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+ row["image"])
        st.write(f"[source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+ row["image"])
        st.write(f"[source code]({row['url']})")
    

