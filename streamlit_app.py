import streamlit
import pandas as pd
import requests as r

streamlit.title('hela hola kinder cola')

streamlit.header('🥣Breakfast Menu')   

streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑🍞Hard-Boiled Free-Range Egg')

streamlit.header('🍌Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.

streamlit.dataframe(fruits_to_show)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)


streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = r.get("https://fruityvice.com/api/fruit/" +"kiwi")

# Normalize
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

# output Normalized data
streamlit.dataframe(fruityvice_normalized)
