import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

# For more emojis code https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Portfolio", page_icon=":computer:", layout= "wide")

def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#-- Load assets
lottie_coding = load_lottieur("https://assets5.lottiefiles.com/packages/lf20_iv4dsx3q.json")
img_password_manager = Image.open("images/passwordmanager.png")


# -- header section
with st.container():
    st.subheader("Hi, I am name :wave:")
    st.title("A Software Engineer")
    st.write("Turning ideas into well developed products is my calling")
    st.write("[See some of my codes >](https://github.com)")

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

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# -- Projects
with st.container():
    st.write("---")
    st.header("My recent projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))

    with image_column:
        st.image(img_password_manager)
    with text_column:
        st.subheader("Project 1")
        st.write(
            """
            Description example: Save your accounts emails and passwords under a single txt file.
            This was done using learned concepts on Python and the package tkinter
            """
            )
        st.markdown("[Watch video >](https://www.youtube.com/watch?v=sUwD3GRPJos)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_password_manager)
    with text_column:
        st.subheader("Project 2")
        st.write(
            """
            Description example: Save your accounts emails and passwords under a single txt file.
            This was done using learned concepts on Python and the package tkinter
            """
            )
        st.markdown("[Watch video >](https://www.youtube.com/watch?v=sUwD3GRPJos)")

# -- contact
with st.container():
    st.write("---")
    st.header("Get in touch with me")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/your@email.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder= "Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
    """
    left_column,right_column =st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
