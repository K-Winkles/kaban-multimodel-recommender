import streamlit as st
import os
import json
import pandas as pd
import pickle

custom_css = """
<style>
/* Your custom CSS goes here */
body {
    font-family: "Times New Roman", Times, serif;
}

/* Example to force certain desktop styles */
.container {
    width: 100% !important;
}

.row-widget {
    padding: 10px !important;
}

/* Adjust the maximum width of the main content area */
.stApp {
    max-width: 800px;
    margin: auto;
}

/* Additional custom styles */
</style>
"""


# Load user history and recommendations from the pickle file
file_path = 'dev/user_hist_reco.pkl'
with open(file_path, 'rb') as file:
    user_hist_reco_dict = pickle.load(file)

# Set page title and bannder image
st.set_page_config(page_title="KabanMarket.com")

# Inject custom CSS with st.markdown
st.markdown(custom_css, unsafe_allow_html=True)

st.image('app/pages/image.png')
df_asin_mapping = pd.read_csv('dataset/utility/reviews.csv')

# Display dropdwon of top reviewers
user_names = list(user_hist_reco_dict.keys())
selected_user = st.selectbox("Select User:", user_names)

def display_buttons(asin_value, algo, prodtype):
    """
    Display buttons based on ASIN algo and prod type
    """
    # Container to hold the buttons
    with st.container():
        col1, col2  = st.columns(2)  # Adjust the ratio as needed for your layout
        with col1:
            # "Add to Cart" button
            if st.button("Add to Cart", type = 'secondary', key='add_'+asin_value+algo+prodtype):
                st.write("Add to cart!")  # Placeholder action
        with col2:
            # "Buy Now" button
            if st.button("Buy Now", type = 'primary', key='buy_'+asin_value+algo+prodtype):
                st.write("Proceed to Buy!")  # Placeholder action
                # Get URL to navigate to when image is clicked
def main_page():
    """
    Display the main page of the app containing user history and recommendations
    """
    # Display expandable container for user history
    with st.expander("User history"):
                st.title(selected_user.title() + "'s Reviewed products:")
                df_user_hist = user_hist_reco_dict[selected_user]['SVD'][0].reset_index(drop=True)
                df_user_hist = df_user_hist.drop('ProductName', axis=1)
                df_user_hist = pd.merge(df_user_hist, df_asin_mapping, on='ASIN')
                df_user_hist = df_user_hist.drop_duplicates(subset='ASIN', keep='first')
                # Display items as small tiles in three columns
                cols = st.columns(3)  # Create three columns
                for index, item in df_user_hist.iterrows():
                    col = cols[index % 3]  # Cycle through columns
                    with col:
                        try:
                            st.image(item["image"], use_column_width=True)
                            name = item["ProductName"].replace('_',' ').title()
                            st.markdown(f"<b>{name}</b></div>", unsafe_allow_html=True)
                            st.markdown(f"<span style='color: red;font-size: 20px;'>$ {item['price']}</span>", unsafe_allow_html=True)
                            asin_value = item['ASIN']
                            display_buttons(asin_value,'hist','hist')
                            st.divider()
                        except Exception as e:
                            print(e)
    # Display tabs containing recommendations per algorithm
    tabs = st.tabs(list(user_hist_reco_dict[next(iter(user_hist_reco_dict))].keys()))
    # Iterate over each tab and key in the dictionary simultaneously
    for tab, algo in zip(tabs, user_hist_reco_dict[next(iter(user_hist_reco_dict))].keys()):
        with tab:
            with st.expander("Recommended items", expanded = True):
                st.title(selected_user.split('_')[0].title() + "'s Recommended Products:")
                df_reco = pd.DataFrame(user_hist_reco_dict[selected_user][algo][1], columns=['ASIN'])
                df_reco = pd.merge(df_reco, df_asin_mapping, on = 'ASIN')
                df_reco = df_reco.drop_duplicates(subset='ASIN', keep='first')
                # Display items as small tiles in three columns
                cols = st.columns(3)  # Create three columns
                for index, item in df_reco.iterrows():
                    col = cols[index % 3]  # Cycle through columns
                    with col:
                        try:
                            st.image(item["image"], use_column_width=True)
                            name = item["ProductName"].replace('_',' ').title()
                            st.markdown(f"<b>{name}</b></div>", unsafe_allow_html=True)
                            st.markdown(f"<span style='color: red;font-size: 20px;'>$ {item['price']}</span>", unsafe_allow_html=True)
                            asin_value = item['ASIN']
                            display_buttons(asin_value,algo,'reco')
                            st.divider()
                        except Exception as e:
                            print(e)
if __name__ == "__main__":
     main_page()
