import streamlit as st

st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.header("This is a header with a divider", divider="yellow")
st.header("These headers have rotating dividers", divider=True)
st.header("One", divider=True)
st.header("Two", divider=True)
st.header("Three", divider=True)
st.header("Four", divider=True)
st.button("click me", on_click=lambda: st.text("You clicked the button!"))
st.markdown("*Streamlit* is  **really** ***cool***.")
with st.sidebar:
    st.header("This is a header in the sidebar")
    st.button("click me", on_click=lambda: st.text("You clicked the button in the sidebar!"))

col1,col2 = st.columns(2)

with col1:
    x=st.slider("choose a value between",1,10)
with col2:
    st.write("The value of :orange[***x***] is:",x)