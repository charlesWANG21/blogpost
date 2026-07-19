import streamlit as st

st.logo("https://tse3.mm.bing.net/th/id/OIP.PRn2vZX_fiQ9yOq7y8G8RgHaEG?r=0&rs=1&pid=ImgDetMain&o=7&rm=3", size='large', link="https://cwblogpost.streamlit.app/")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.title("Log in")
    with st.form("Login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Log in")

        if submitted:
            if username =='Ballsackz' and password == 'Garyisgay':
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
            else:
                st.error("Incorrect username OR password")

def logout():
    st.session_state.logged_in = False
    st.rerun()

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

pages = {
    "Daily Life": [
        st.Page("main.py", title="Self Intro"),
        st.Page("food.py", title = "Food", icon=":material/icecream:"),
    ],
"Settings": [logout_page]
}

if st.session_state.logged_in:
    pg = st.navigation(pages)
else: 
    pg = st.navigation([login_page])

pg.run()
