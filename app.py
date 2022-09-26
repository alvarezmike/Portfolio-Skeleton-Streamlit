import streamlit as st
import requests
from streamlit_lottie import st_lottie

# For more emojis code https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Portfolio", page_icon=":computer:", layout= "wide")

def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#-- Load assets
lottie_coding = load_lottieur("https://assets5.lottiefiles.com/packages/lf20_iv4dsx3q.json")


# -- header section
with st.container():
    st.subheader("Hi, I am Michael :wave:")
    st.title("A Software Engineer")
    st.write("Turning ideas into well developed products is my calling")
    st.write("[See some of my codes >](https://github.com/alvarezmike)")

# -- What I Do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            dgdggdgdgdgdgdgdgdg
            - sddgdgdggdgd
            - ddgdgdggdddhdhdhdh
            - dhdhhdhdhdhdhd
            - ahhaagagagag
            
            If this sounds interesting to you, coonsider subscribing shsushbbddbb
            """
        )
        st.write("[Youtube channel] > link here")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# -- Projects
with st.container():
    st.write("---")
    st.header("My recent projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))

    with image_column:
        # insert image
        with text_column:
            st.subheader("Password Manager")
            st.write(
                """
                Save your accounts emails and passwords under a single txt file
                This was done using learned concepts on Python and the package tkinter
                """
            )
            st.markdown("[Watch video..](https://www.youtube.com/watch?v=sUwD3GRPJos)")