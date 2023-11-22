import streamlit
import pandas as pd
import requests
from urllib.error import URLError

# Display breakfast menu
streamlit.header('🥣 Breakfast Menu')
streamlit.text('🥗Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔 🥑Kale, Spinach & Rocket Smoothie')
streamlit.text('🍞Hard-Boiled Free-Range Egg')

# Display options for building a fruit smoothie
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Load fruit data from a CSV file
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Display the entire fruit list
streamlit.dataframe(my_fruit_list)

# Let users pick some fruits
selected_fruits = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the selected fruits
fruits_to_show = my_fruit_list.loc[selected_fruits]
streamlit.dataframe(fruits_to_show)

# Fruityvice API integration
import streamlit
import requests
import pandas as pd
from urllib.error import URLError

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    
    if fruityvice_response.status_code == 200:
        fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
        return fruityvice_normalized

# Display information about a selected fruit from Fruityvice
# Display information about a selected fruit from Fruityvice
# Display information about a selected fruit from Fruityvice
streamlit.header("Fruityvice Fruit Advice!")
try:
    fruit_choice = streamlit.text_input("What fruit would you like information about?")
if not fruit_choice:
        streamlit.error("Please select a fruit to get information.")
else:
    back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)


