import pandas
import streamlit as st
st.set_page_config(layout='wide')

st.button('Hit me')
st.checkbox('Check me out')
st.radio('Radio', [1, 2, 3])
st.selectbox('Select', [1, 2, 3])
st.multiselect('Multiselect', [1, 2, 3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1, '2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
st.color_picker('Pick a color')


st.spinner()
st.balloons()
st.error('Error message')
st.warning('Warning message')
st.info('Info message')
st.success('Success message')


st.empty()
my_placeholder = st.empty()
my_placeholder.text('Replaced!')
st.help(pandas.DataFrame)

st.text('Fixed width text')
st.markdown('_Markdown_')  # see *
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects')  # df, err, func, keras!
st.write(['st', 'is <', 3])  # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')

# Magic commands implicitly `st.write()`
''' _This_ is some __Markdown__ '''
a = 3
''' ## Hello '''
