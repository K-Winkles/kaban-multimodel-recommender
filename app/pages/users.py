import streamlit as st
import os
import json
import pandas as pd
import pickle

folder_path = 'dataset/extracts'


file_path = 'dev/user_hist_reco.pkl'
with open(file_path, 'rb') as file:
    user_hist_reco_dict = pickle.load(file)

def get_csv_files(directory):
    """
    Get all csv files in a directory
    """
    csv_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if (file.startswith('log_amazon') or file.startswith('amazon')) and file.endswith('.csv'):
                csv_files.append(os.path.join(root, file))
    return csv_files

def get_asin_name_mapping():
    files = get_csv_files(folder_path)
    df_itemset = pd.DataFrame()
    for file in files:
        try:
            df = pd.read_csv(file, low_memory=False)[['name','asin','image', 'price','customerReview']]
            df_itemset = pd.concat([df_itemset, df], ignore_index=True)   
        except Exception as e:
            print(e)
    df_itemset['asin'] = df_itemset['asin'].str.lower()
    df_itemset = df_itemset.drop_duplicates(subset='asin', keep='first')
    return df_itemset

st.set_page_config(page_title="KabanMarket.com")
df_asin_mapping = get_asin_name_mapping()
    
# Display Top Reviewers
user_names = user_hist_reco_dict[next(iter(user_hist_reco_dict.keys()))].keys()
selected_user = st.selectbox("Select a Reviewer", [name.replace('_', '') for name in user_names])
# Function to display buttons
def display_buttons(asin_value, algo, prodtype):
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
# Main function
def main_page():
    # Create tabs dynamically based on the keys of the dictionary
    with st.expander("User history"):
                st.title(selected_user.title() + "'s Reviewed products:")
                df_user_hist = user_hist_reco_dict['SVD'][selected_user+'_'][0].reset_index(drop=True)
                df_user_hist = pd.merge(df_user_hist, df_asin_mapping, left_on='ASIN', right_on='asin', how='left')
                # Display items as small tiles in three columns
                cols = st.columns(3)  # Create three columns
                for index, item in df_user_hist.iterrows():
                    col = cols[index % 3]  # Cycle through columns
                    with col:
                        try:
                            st.image(item["image"], use_column_width=True)
                            name = item["name"]
                            st.markdown(f"<b>{name}</b></div>", unsafe_allow_html=True)
                            st.markdown(f"<span style='color: red;font-size: 20px;'>{item['price']}</span>", unsafe_allow_html=True)
                            st.caption(item['customerReview'])
                            asin_value = item['asin']
                            display_buttons(asin_value,'hist','hist')
                            st.divider()
                        except Exception as e:
                            print(e)
    tabs = st.tabs(list(user_hist_reco_dict.keys()))
    # Iterate over each tab and key in the dictionary simultaneously
    for tab, algo in zip(tabs, user_hist_reco_dict.keys()):
        with tab:
            with st.expander("Recommended items", expanded = True):
                st.title(selected_user.title() + "'s Recommended Products:")
                df_reco = user_hist_reco_dict[algo][selected_user+'_'][1]
                df_reco = pd.merge(df_reco, df_asin_mapping, left_on='ASIN', right_on='asin', how='left')
                # Display items as small tiles in three columns
                cols = st.columns(3)  # Create three columns
                for index, item in df_reco.iterrows():
                    col = cols[index % 3]  # Cycle through columns
                    with col:
                        try:
                            st.image(item["image"], use_column_width=True)
                            name = item["name_x"]
                            st.markdown(f"<b>{name}</b></div>", unsafe_allow_html=True)
                            st.markdown(f"<span style='color: red;font-size: 20px;'>{item['price']}</span>", unsafe_allow_html=True)
                            st.caption(item['customerReview'])
                            asin_value = item['asin']
                            display_buttons(asin_value,algo,'reco')
                            st.divider()
                        except Exception as e:
                            print(e)
if __name__ == "__main__":
     main_page()
