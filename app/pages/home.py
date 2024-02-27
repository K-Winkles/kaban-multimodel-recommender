import streamlit as st
import os
import json

# Function to get categories from folder names
def get_categories(directory):
    categories = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
    return sorted(categories)

st.set_page_config(page_title="KabanMarket.com")
# Path to the directory containing category folders
data_directory = "dataset/extracts/amazon/"
    
# Get categories from folder names
categories = get_categories(data_directory)
    
# Display categories
st.sidebar.title("KabanMarket Product Categories")
selected_category = st.sidebar.selectbox("Select a category", categories)
st.title("KabanMarket: " + selected_category.title())
st.divider()
# Function to display product page

# Function to read JSON files in a category folder
def read_items(category_directory):
    items = []
    for file_name in os.listdir(category_directory):
        file_path = os.path.join(category_directory, file_name)
        if os.path.isfile(file_path) and file_name.endswith('.json') and not file_name == 'amazon_sspa.json':
            with open(file_path, 'r') as f:
                data = json.load(f)
                items.append(data)
    return items

# Function to get ASIN
def get_asin(item):
    asin_value = ''
    for key in item["body"]["productInformation"]:
        if key["name"] == "ASIN":
            asin_value = key["value"]
            break
    return asin_value

# Function to display buttons
def display_buttons(asin_value):
    # Container to hold the buttons
    with st.container():
        col1, col2  = st.columns(2)  # Adjust the ratio as needed for your layout
        with col1:
            # "Add to Cart" button
            if st.button("Add to Cart", type = 'secondary', key='add_'+asin_value):
                st.write("Add to cart!")  # Placeholder action
        with col2:
            # "Buy Now" button
            if st.button("Buy Now", type = 'primary', key='buy_'+asin_value):
                st.write("Proceed to Buy!")  # Placeholder action
                # Get URL to navigate to when image is clicked

# Main function
def main_page():   
    # Path to the selected category directory
    category_directory = os.path.join(data_directory, selected_category, 'items')
    
    # Read JSON files in the selected category directory
    items = read_items(category_directory)
    
    # Display items as small tiles in three columns
    cols = st.columns(3)  # Create three columns
    for index, item in enumerate(items):
        col = cols[index % 3]  # Cycle through columns
        with col:
            try:
                if 'body' in item and 'mainImage' in item['body']:
                    st.image(item["body"]["mainImage"], use_column_width=True)
                    name = item["body"]["name"]
                    st.markdown(f"<b>{name}</b></div>", unsafe_allow_html=True)
                    st.markdown(f"<span style='color: red;font-size: 20px;'>{item['body']['price']}</span>", unsafe_allow_html=True)
                    st.caption(item['body']['customerReview'])
                    asin_value = get_asin(item)
                    display_buttons(asin_value)
                    st.divider()
            except Exception as e:
                print(e)

if __name__ == "__main__":
     main_page()
