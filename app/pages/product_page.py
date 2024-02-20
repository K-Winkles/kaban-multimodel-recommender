import streamlit as st
import requests
import json

# Load the JSON data
file_path = 'dataset/extracts/amazon/action figures/items/amazon_B00ASKV7FE.json'
with open(file_path, "r") as file:
    data = json.load(file)
# Using object notation
st.set_page_config(page_title="KabanMarket.com:" + data['body']['name'])
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
