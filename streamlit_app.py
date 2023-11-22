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
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

# Display information about a selected fruit from Fruityvice
streamlit.header("Fruityvice Fruit Advice!")

try:
    fruit_choice = streamlit.text_input("What fruit would you like information about?")

    if not fruit_choice:
        streamlit.error("Please select a fruit to get information.")
    else:
        back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)

except URLError as e:
    # Handle URLError as needed
    pass  # Placeholder for handling URLError

import streamlit
import snowflake.connector

# ... (your existing code) ...

streamlit.header("The fruit load list contains:")

# snowflake-function
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
        return my_cur.fetchall()

# Establish Snowflake connection
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

# add button to load data
if streamlit.button("Get fruit load list"):
    fruit_load_list_data = get_fruit_load_list()
    streamlit.dataframe(fruit_load_list_data)

# allow user to add fruit
# allow user to add fruit
import streamlit
import snowflake.connector

# Establish Snowflake connection
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

# allow user to add fruit
def insert_row_snowflake(new_fruit):
    try:
        with my_cnx.cursor() as my_cur:
            query = "INSERT INTO PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST (column_name) VALUES (?)"
            my_cur.execute(query, (new_fruit,))
        return f"Thanks for adding {new_fruit}"
    except Exception as e:
        return f"Error adding {new_fruit}: {e}"

add_my_fruits = ["jackfruit", "papaya", "guava", "kiwi"]

for new_fruit in add_my_fruits:
    back_from_function = insert_row_snowflake(new_fruit)
    print(back_from_function)

# Optional: Uncomment the following lines if you want to display the results in Streamlit
# streamlit.text("Fruits added:")
# streamlit.text("\n".join([insert_row_snowflake(new_fruit) for new_fruit in add_my_fruits]))





