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
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values (?)", (new_fruit,))
    return "Thanks for adding " + new_fruit

add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a fruit to the list'):
    back_from_function = insert_row_snowflake(add_my_fruit)
    streamlit.text(back_from_function)
