import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(page_title='Tana Web GIS', layout = 'wide', page_icon=":shark:")

# loading the png image
img = Image.open("./img/tana.png")


#removing menu and footer note
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden; }
    footer {visibility: hidden; }
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html = True)

st.image(img, width=700)

st.write("""
####         A map displaying Water Service Providers under TWWDA coverage area

*Select an option in the select box below to view your desired WSP*
""")


options = ['Nyewasco', 'Omwasco', 'Chuka', 'Mawasco']
choice_selected = st.selectbox("Select a WSP to view", options)

if choice_selected == 'Omwasco':
    HtmlFile = open("./maps/omwasco.html", 'r')
    omwasco = HtmlFile.read()
    st.subheader("Omwasco Service Area Utilities")
    components.html(omwasco, height=500)

elif choice_selected == 'Nyewasco':
    HtmlFile_2 = open("./maps/nyewasco.html", 'r')
    nyewasco = HtmlFile_2.read()
    st.subheader("Nyewasco Service Area Utilities")
    components.html(nyewasco, height=500)

elif choice_selected == 'Chuka':
    HtmlFile_3 = open("./maps/chuka.html", 'r')
    chuka = HtmlFile_3.read()
    st.subheader('Chuka Service Area Utilities')
    components.html(chuka, height=500)

elif choice_selected == 'Mawasco':
    HtmlFile_4 = open("./maps/mawasco.html", 'r')
    mawasco = HtmlFile_4.read()
    st.subheader('Mawasco Service Area Utilities')
    components.html(mawasco, height=500)