import streamlit as st
from streamlit_extras.let_it_rain import rain

st.title("This is my blogpost😊")

st.header(" My name is Charles Wang")
st.subheader("This is about my adorable gecko")

st.markdown("""
  My name is Charles, I am a student, and I am a very happy person! My hobbies: Hockey, Piano, Reading, Coding, and Gaming.
        
            I have a gecko named Gecky🦎🦎🦎🦎🦎🦎🦎🦎🦎🦎, who is really cute and always exporing his tank full of plentiful surprises.
            """)
# button is click
if st.button("send balloons"):
    st.balloons()

if st.button('snowflake'):
    st.snow()

if st.button('click me'):
    rain(
        emoji='🎊',
        font_size=50,
        falling_speed=8,
        animation_length="10"

    )

if st.button('Raining Gecko's'):
    rain(
        emoji='🦎',
        font_size=60,
        falling_speed=12,
        animation_length="5"

    )

st.image('https://i.pinimg.com/originals/aa/82/0f/aa820f504b0e23cbd861e2fb4add413c.jpg')
st.image('https://i.redd.it/200zveum3oj91.gif')

