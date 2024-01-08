import streamlit as st
st.set_page_config(page_title="Dog Breeds")
st.header("Categories of Dogs")
col1,col2,col3,col4 = st.columns(4)
with col1:
  st.subheader("Husky")
  st.image("./Husky.jpg",caption="Husky Dog", width=300,use_column_width=True)
  st.write("Husky")
with col2:
  st.subheader("GoldenRetriever")
  st.image("./GoldenRetriever.jpg",caption="GoldenRetriever Dog", width=300,use_column_width=True)
  st.write("GoldenRetrieve")
with col3:
  st.subheader("Labrador")
  st.image("./Labrador.jpg",caption="Labrador Dog", width=300,use_column_width=True)
  st.write("Labrador")
with col4:
  st.subheader("German Shepard")
  st.image("./German_Shepard.jpg",caption="German_Shepard", width=300,use_column_width=True)
  st.write("German Shepard")
