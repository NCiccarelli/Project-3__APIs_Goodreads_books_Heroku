#import package
import streamlit as st
from PIL import Image
import pandas as pd
#from IPython.display import Image,display

#Section 1: title and importing data:
st.title("Welcome to the APIs_Goodreads_books App")

#import the data from the Streamlit folder
small_books_df = pd.read_csv("small_books_df.csv")


st.write('The textual data for this app comes from Kaggle\'s Goodreads dataset and the "Open Library Books API". The book covers are retrieved from the "Open Library Covers API".')

st.write('You can see the data/dataframe by clicking on "See the data/dataframe" checkbox:')
#checking the data
check_data = st.checkbox("See the dataframe")
if check_data:
    st.write(small_books_df)



# Section 2: show the book covers:
st.write('Please choose a book title from the list reported below and click on "Run me!". We will show you the book cover for that title as soon as you have chosen the title!')
chosen_option = st.selectbox('', list(small_books_df.title))
index = small_books_df.index[small_books_df['title'] == chosen_option]
chosen_isbn13 = small_books_df.isbn13.loc[index[0]]
#trasnform the isbn13 into a string:
chosen_isbn13=str(chosen_isbn13)
#Identify the book cover via the isbn13:
chosen_image_location = f"images_streamlit/image{chosen_isbn13}.jpg"
#Image:
img = Image.open(chosen_image_location)        #"images_streamlit/chosen_image_location.jpg"
#Show the image:
if st.button("Run me!"):
    st.image(img, width=None)
    st.write('Below we show the book cover again:')
    st.image(img, width=None)

#Let's show the image again:
#st.write('Below we show the book cover again:')
#st.image(img, width=None)
