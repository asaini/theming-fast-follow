import streamlit as st

def draw_all(key):
    st.write("""
        # Hello

        Hi **there!** This is `code`.

        ```
        This is block code.
        ```
    """)

    radio_markdown = """
    h2.  Select a number

    ---

    You have **3** choices! 
    """

    st.checkbox("Cool?", key=key, help='Press to confirm checkbox')
    st.radio("Pick a number", [1, 2, 3], key=key, help=radio_markdown)
    st.button("Click me!", key=key)
    st.slider("Pick a number", key=key)
    st.select_slider("Pick a number", [1, 2, 3], key=key)
    st.number_input("Pick a number", key=key)
    st.text_input("Pick a number", key=key)
    st.text_area("Pick a number", key=key)
    st.selectbox("Pick a number", [1, 2, 3], key=key)
    st.multiselect("Pick a number", [1, 2, 3], key=key)
    st.file_uploader("Pick a file", key=key)
    st.color_picker("Favorite color", key=key)
    with st.beta_expander("Expand me!"):
        st.write("hi")
    st.progress(0.6)
    st.json({"data": [1,2,3,4]})
    st.dataframe({"data": [1,2,3,4]})
    st.table({"data": [1,2,3,4]})
    st.line_chart({"data": [1,2,3,4]})
    st.help(st.write)

draw_all("main")

with st.sidebar:
    draw_all("sidebar")


st.title('Theming Test')
st.write('Body Text')

'''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum
'''

num = st.sidebar.number_input(label='Enter a number', value=0)

st.write('hi')

with st.echo():
    st.write('Test')


st.info('This is an info')
st.warning('this is a warning')
st.error('this is an error')
st.success('this is success')