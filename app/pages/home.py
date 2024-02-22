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

def product_page():
    if st.button("Back to Main Page"):
        st.session_state.current_page = 'main_page'
    asin_value = st.session_state.asin_value
    file_path = 'dataset/extracts/amazon/action figures/items/amazon_' + asin_value + '.json'
    # Load the JSON data
    with open(file_path, "r") as file:
        data = json.load(file)
    # Using object notation
    
    st.title("KabanMarket.com")

    # Display the e-commerce data
    st.header(data['body']['name'])
    st.title(f"Price: {data['body']['price']}",)
    st.write(f"Brand: {data['body']['brand']}")
    st.button("Add to Cart", type='secondary')
    st.button("Buy Now", type='primary')
    st.image(data['body']['mainImage'],
            caption='Main Image', use_column_width='always')

    # Display image carousel
    st.write("Image Carousel")
    selected_image_index = st.slider(
        "Select Image", 0, len(data["body"]["images"]) - 1, 0)

    # Display selected image
    st.image(data["body"]["images"][selected_image_index],
            width=400, caption="Image")

    # Display other relevant information
    st.header("Description:")
    st.write(data['body']['description'])
    # Create a single container for all images with horizontal layout
    container = st.container()


    st.divider()
    st.header("Features:")
    for feature in data['body']['features']:
        st.write(feature)
    st.divider()
    st.header("Customer Reviews:")
    st.subheader(f"Rating: {data['body']['customerReview']}")
    # Display reviews
    st.write(f"Number of Reviews: {data['body']['customerReviewCount']}")
    for review in data["body"]["reviews"]:
        st.header(f"Title: {review['reviewTitle']}")
        st.subheader(f"Rating: {review['reviewRating']}")
        st.write(f"Reviewer: {review['reviewerName']}")
        st.write(f"Date: {review['reviewDate']}")
        st.write(f"Text: {review['reviewText']}")
        st.write("---")  # Add a horizontal line between reviews





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
                    st.write(f"Price: {item['body']['price']}",)
                    asin_value = get_asin(item)
                    if st.button("Go to Product Page", key='prod_'+asin_value):
                        st.session_state.current_page = 'product_page'
                        print("Current page:" ,st.session_state.current_page)
                        st.session_state.asin_value = asin_value
                        print(asin_value)
                    st.text(asin_value)
                    st.divider()
            except Exception as e:
                print(e)

    # if st.session_state.current_page == 'main_page':
    #     main_page()

    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'main_page'
    if st.session_state.current_page == 'product_page':
        product_page()

if __name__ == "__main__":
     main_page()
