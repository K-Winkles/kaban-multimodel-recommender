<h2 style="color:#ff9900; background-color:#1c5177; padding: 10px; text-align:left; border: 1px solid #4a62d8;">Abstract</h2>

The purpose of this initiative is to develop multiple recommender systems that can provide personalized product recommendations to e-commerce platform users based on a variety of factors such as purchase history, product ratings, and interests of similar users. It also aims to compare the performance of these recommendation models across different metrics. 

The process involved scraping the data from Amazon.com using Crawlbase API, an all-in-one data crawling and scraping platform, based on defined search terms. After preprocessing, the aggregated data is then fed to recommender system models including Neighborhood-Based Collaborative Filtering, Latent Factor-Based Collaborative Filtering, Content-Based Recommender System, as well as a Hybrid Recommender System using LightFM, to generate product recommendations for users with at least five product reviews.  

After a thorough analysis of the results, the team was able to identify 2 tiers of multimodel recommender systems that would be appropriate for the specific application / requirement of digital market owners and thereby deliver the most business value.  

<p style="text-align: center;"><strong>Table 1: Basic Recommender System</strong></p>

| Model Name | Algorithm | Description | NDCG @ k=10 |
|-----|-----|-----|-----|
| Payak | KNN Basic | Recommends products based on your closest friends | 0.27 |
| Damayan |KNN with Means | Optimized method of recommending products based on your closest friends | 0.27 |
| Aparte | SVD | Recommends products based on common patterns between users and items | 0.26 |

<p style="text-align: center;"><strong>Table 2: Premium Recommender System</strong></p>

| Model Name | Algorithm | Description | NDCG @ k=10 |
|-----|-----|-----|-----|
| Barkada | Latent Factor Based Collaborative Filtering (ALS) | Recommends Products based on your closest friends | 0.99 |
| Suki | Content-Based Recommender System | Recommends Products based on your previous purchase history | 0.96 |
| Sari-sari | Hybrid Recommender System | Recommends a variety of Products that you might like based on your previous purchase history and your closest friends | 0.99 |

The results showed that the recommendations provided by the algorithms are more personalized compared to the baseline global average, which merely offers the top K most popular items.  The algorithms demonstrate a clear connection between users' history and characteristics, resulting in more relevant and engaging recommendations. While offline evaluation metrics indicate the effectiveness of the algorithms, the real test lies in online evaluation metrics, which will provide a more accurate assessment of performance in a live environment. 

The offline evaluation results and metrics suggest that all the recommender systems performed equally well, including the hybrid model using LightFM. Despite having low NDCG scores, the "Basic" recommendation systems still have their merits, recommending relevant items to the sampled users. "Premium" recommendation systems yielded the highest NDCG scores. LightFM's recommendations stand out for their ability to leverage both item and user metadata while addressing the cold start problem, generating relevant and potentially exploratory recommendations that enhance users' experience and satisfaction with the platform. 

To make the recommender systems more robust, the researchers suggest the following: 

1. Consider Contextual Factors  

2. Incorporate Real-time Data Processing  

3. Integrate a Feedback Loop Mechanism 

4. Implement Advanced Algorithms 

5. Employ Predictive Models 

6. Optimize Performance of Developed Models 

Overall, the project has succeeded in developing recommender systems that unlock new market opportunities, boost user engagement, and improve the overall competitiveness of small-scale and emerging online businesses in the digital marketplace.

<h2 style="color:#ff9900; background-color:#1c5177; padding: 10px; text-align:left; border: 1px solid #4a62d8;">Introduction</h2>

For the past three decades, e-commerce has revolutionized the way we shop. Shopping has evolved beyond the traditional notion of visiting a physical store, selecting items, and making purchases. What once took hours can now be accomplished in seconds, at one’s fingertips. 

According to McKinsey, E-commerce has been growing consistently ever since the first online transaction in 1994, when someone sold his friend a Sting CD for $12.48 plus shipping. But when the COVID-19 pandemic hit, triggering lockdowns all over the world, customers went all-in: year-over-year growth of e-commerce as a share of total retail sales grew 1.6 times in China, 3.3 times in the United States, and 4.5 times in the United Kingdom. E-commerce sales penetration in the United States more than doubled to 35 percent in 2020 from the previous year, roughly the equivalent of ten years of growth. Globally, nearly 20 percent of total global sales in 2021 were made from online purchases. By 2025, nearly a quarter of all global sales are expected to be made online [[1]]((https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-e-commerce)).

<h2 style="color:#ff9900; background-color:#1c5177; padding: 10px; text-align:left; border: 1px solid #4a62d8;">Problem Statement</h2>

In the rapidly evolving landscape of e-commerce, small-scale and emerging online businesses face significant challenges in competing with industry giants. This is primarily due to the significant influence and market dominance of these big players but also due to limitations on the end of the small players. One of these limitations is the lack of offering personalized experiences to users. While the likes of Amazon, Alibaba, Rakuten, and Shopify have been leveraging recommendation systems to drive sales and overall success, up-and-coming platforms are in need of similar technology to provide tailored product recommendations to unlock new market opportunities, boost user engagement, and improve overall competitiveness in the digital marketplace. 

To address this critical issue, this project aims to: 

1. Develop multiple recommender systems that can provide personalized product recommendations to e-commerce platform users based on their purchase history, product ratings, and the interests of similar users. 

2. Compare the performance of these recommender systems across different metrics and identify which models work best for specific applications and purposes. 

<h2 style="color:#ff9900; background-color:#1c5177; padding: 10px; text-align:left; border: 1px solid #4a62d8;">Motivation</h2>

Amazon is the largest e-commerce brand in the world in terms of revenue and market share [[2]]((https://www.statista.com/statistics/1103390/amazon-retail-ecommerce-sales-global/)). It currently uses a hybrid recommender system – a combination of collaborative and content-based filtering in its platforms which had largely influenced the company’s success. In 2023, Amazon's net revenue from e-commerce net sales was US$575 billion [[3]]((https://s2.q4cdn.com/299287126/files/doc_financials/2023/q4/AMZN-Q4-2023-Earnings-Release.pdf)), and as of 2021, about 35 percent of all sales on Amazon happen via recommendations [[4]]((https://www.datafeedwatch.com/blog/amazon-statistics#6.-amazon%E2%80%99s-recommendations)). 


Recommendations personalized based on a user's past interactions and interests make it very likely for that user to find the recommended product interesting as well. In fact, according to a study of Epsilon Marketing, 80% percent of consumers are more likely to purchase from a brand that delivers personalized content [[5]]((https://www.slideshare.net/EpsilonMktg/the-power-of-me-the-impact-of-personalization-on-marketing-performance#1)). In another study conducted by PracticalEcommerce, it was found that brands who provide recommendations experiences higher conversions rates than those who don’t and that customers who click on product recommendations are 4 times more likely to add that product to cart and complete the purchase [[6]]((https://www.practicalecommerce.com/study-personalized-recommendations-produce-4-times-conversions)).

This clearly demonstrates the impact of recommendations. In this study, our team looks to develop recommender systems using Amazon products and users as a testbed. Based on the results, the team will infer which algorithms perform the best for different situations. The resulting models can serve as a tool for up-and-coming e-commerce players to increase engagement and conversions. Overall, the study would benefit these entities by elevating user experience, improving item discoverability, increase average cart size, and target users more accurately.

<h2 style="color:#ff9900; background-color:#1c5177; padding: 10px; text-align:left; border: 1px solid #4a62d8;">Preliminaries</h2>

#### Recommender Systems 

The basic idea of recommender systems is to utilize various sources of data to infer customer interests. The entity to which the recommendation is provided is referred to as the user, and the product being recommended is also referred to as an item. Therefore, recommendation analysis is often based on the interaction between users and items, because past interests and proclivities are often good indicators of future choices [[8]]((https://pzs.dstu.dp.ua/DataMining/recom/bibl/1aggarwal_c_c_recommender_systems_the_textbook.pdf)).

#### Collaborative Filtering 

Collaborative Filtering models make recommendations by leveraging the collaborative power of ratings provided by multiple users. In this method, the descriptive attributes of an item are not explicitly used in providing recommendations. 
The two main classes of collaborative filtering methods are: 
* Neighborhood-based method also known as memory-based method 
* Model-based method also known as latent factor model 

#### Content-Based Recommender System 

Content-based recommender models make recommendations by using the descriptive attributes of items. The system does not consider how other users rated the items but instead relies on its features and provide item recommendations similar to items highly rated by the user. 
This user-specific model is used to predict whether the corresponding individual will like an item for which her rating or buying behavior is unknown [[9]]((https://pzs.dstu.dp.ua/DataMining/recom/bibl/1aggarwal_c_c_recommender_systems_the_textbook.pdf)).

#### Hybrid Recommender System Using LightFM 

As per LightFM documentation, LightFM is a hybrid recommender system that handles both explicit and implicit feedback. Its main feature is its ability to incorporate user and item metadata into the matrix factorization models. This enhances the capability to recommend new items to users and to adapt to new users' preferences based on their features [[10]](http://ceur-ws.org/Vol-1448/paper4.pdf).  

The core of LightFM lies in its hybrid model, which combines traditional collaborative filtering methods with content-based approaches through latent representations [[10]](http://ceur-ws.org/Vol-1448/paper4.pdf). It represents users and items in a shared high-dimensional space, where the embeddings of users and items can be combined to predict a user's preference for an item [[11]](https://making.lyst.com/lightfm/docs/home.html). The strength of this model is in its ability to generalize across users and items, making it highly effective for scenarios where cold-start or sparsity issues are prevalent. 

LightFM provides several loss functions to optimize the recommendation model, catering to different scenarios of feedback and objectives. These include Logistic Loss, Bayesian Personalised Ranking (BPR) Loss, Weighted Approximate-Rank Pairwise (WARP) Loss, and k-Order Statistic Loss (k-OS WARP) [[11]](https://making.lyst.com/lightfm/docs/home.html). Each of these loss functions is designed to handle different types of data and recommendation scenarios, from explicit positive and negative interactions to implicit feedback where only positive interactions are present [[10]](http://ceur-ws.org/Vol-1448/paper4.pdf).

### Methodology Details

1. We scraped data using Crawlbase API. CrawlAPI refers to a set of APIs that allow users to interact directly with crawlers for web crawling purposes. This API enables users to manage and configure crawlers to extract data from websites efficiently. It provides a simple framework for parallel crawling of web pages, allowing users to crawl web pages in parallel.

2. We define search terms (ex. “bedroom”, “fashion”) and scrape all products that appear on the Amazon page. For each product, we get a JSON file with the product information as well as the reviewers and their corresponding reviews.

3. After going through all search terms, the raw JSON files are then collated. For all strings, we clean them by removing most special characters. Then, for each product feature, we break them apart into individual tokens. This is because, many of the raw features look like this: “cardigan_womens_cotton” and each token is actually 1 feature. So we break them apart and assign a value of 1 because the product has that feature. We also ignore features that pertain to dimensions or climate change readiness. Note that we only pick up products that have reviews.

4. We construct the user-item matrix by getting all user ratings for the products . We also construct the reviews matrix, which contains all the reviews of each user for each product. We process the user-item matrix by aggregating all repeated ASINs (this happens in the case wherein a product appears in more than 1 category). We get the sum between all repeated rows, in order to get the aggregated item features.

5. We also construct the reviews matrix, which contains all the reviews of each user for each product

6. We process the user-item matrix by aggregating all repeated ASINs (this happens in the case wherein a product appears in more than 1 category). We get the sum between all repeated rows, in order to get the aggregated item features.

7. We process the userbase by grouping by reviewerID and taking only those that have given 5 or more reviews.

8. We then feed the datasets to each of the algorithms.

9. We compare results for a sample user by looking at the recommendations given by the global baseline average and the top 10 recommendations given by the 6 algorithms.


**Snippet of a sample raw json given below**

```json
{
	"reviewerName": "Hector C.",
                "reviewerLink": "https://www.amazon.com/gp/profile/amzn1.account.AHIIWZBU7QUN2XE5ZPUYQRF5AWEQ",
                "reviewLink": "https://www.amazon.com/gp/customer-reviews/R1JYBKPFVVARL7?ASIN=B0CB36QMXR",
                "reviewRating": "4.0 out of 5 stars",
                "reviewDate": "Reviewed in the United States on July 18, 2021",
                "reviewTitle": "4.0 out of 5 stars Great gaming laptop for the price",
                "reviewText": "The design is beautiful, the keyboard feels nice to type in, gaming experience is great (although I recommend disabling Hybrid mode on the Lenovo Vantage app to get higher fps), fans get loud with high demanding games but is not noticeable with headphones, battery life is okay and what you would expect from a gaming laptop, I like the option lenovo gives for having the battery charged until 60% for preserving battery life (for me it's perfect since I always have it plugged in). The only thing that disappointed be a little was the screen, which when I compared it with my previous laptop had some of a yellow tone in it (it was not night mode since I checked it was turned off). I had to configure a color profile for getting it to a normal tone, although this decreased the max brightness it can give and also some green pixels appear in the screen here and there which I have not figured out yet what they are, but they are not dead pixels. Apart from that the laptop is great and the shipping was very fast, I think it is a great value for the money you pay. Would definitely recommend.",
                "reviewVotes": "",
                "reviewVerifiedPurchase": true,
                "reviewCommentCount": 0,
                "media": {
                    "images": [],
                    "video": ""
                }
}
```

**Legality of scraping**
1. Am I scraping personal data?
2. Am I scraping copyrighted data?
3. Am I scraping data from behind a login?

If your answers to all three of these questions is “No”, then your web scraping is legal.

### Data Description

The data is scrapped fromm Crawlbase API selected by each search term product whuich turns to described with its title, ASIN (Amazon Standard Identification Number), price, dimensions (if available), image URL, rating, and the number of reviews.

### Data Collection

We scrape data using Crawlbase API. CrawlAPI refers to a set of APIs that allow users to interact directly with crawlers for web crawling purposes. This API enables users to manage and configure crawlers to extract data from websites efficiently. It provides a simple framework for parallel crawling of web pages, allowing users to crawl web pages in parallel[[11]](https://www.algolia.com/doc/rest-api/crawler/).

 
We define search terms and scrape all products that appear on the Amazon page. For each product, we get a JSON file with the product information as well as the reviewers and their corresponding reviews. 

<p style="text-align: center;"><strong>Table 3: List of Search Terms</strong></p>

| <center><b></b></center> | <center><b></b></center> |<center><b></b></center> |<center><b></b></center> |
|:---|:---|:---|:---|
|`adventure novel`|`dress`|`moisturizer`|`speakers`|
|`air freshener`|`dresser`|`monitor`|`stanley cup (tumbler & accessories)`|
|`air fryer`|`fabric conditioner`|`mop`|`stationary`|
|`air purifier`|`face mask`|`motherboard`|`steamer`|
|`baby bottle`|`face wash`|`mouse`|`stove`|
|`baby formula`|`facial toner`|`mouthwash`|`stroller`|
|`baby wipes`|`fantasy novel`|`mystery novel`|`surveillance camera`|
|`bathroom (accessories)`|`feminine wash`|`napkin`|`table`|
|`battery (includes household, automotive)`|`first aid (kits)`|`night stand`|`tablet`|
|`bedding`|`folder`|`nonfiction novel`|`tampon`|
|`bedframe`|`frying pan`|`notebook`|`television`|
|`bedroom(accessories)`|`furniture`|`nursery`|`thriller novel`|
|`belt`|`garage`|`office chair`|`tires`|
|`bookshelf`|`gps (also includes watch type GPS)`|`oven`|`tissue`|
|`broom`|`gpu`|`over the counter (includes appliances, countertop stuff, and meds)`|`toddler toy`|
|`building toys`|`hard drive`|`pacifier`|`toilet`|
|`cabinet`|`headphones`|`packing cubes`|`toothbrush`|
|`cables (phone chargers, extension, etc.)`|`historical novel`|`patio (mostly furniture, also includes lamps, rugs, etc.)`|`toy airplanes`|
|`camera`|`home décor`|`pc chassis`|`toy cars`|
|`cap`|`home_office`|`pc fan`|`toy dolls`|
|`car accessories`|`intel amd processor`|`pc power supply`|`travel essentials`|
|`car seat*`|`iron(supplement & for clothes)`|`pc ram`|`tripod`|
|`carpet`|`jewelry`|`phone case`|`underwear`|
|`cellphone`|`keyboard`|`pillow`|`usb`|
|`chair`|`kitchen`|`playroom (also includes playroom furnitures)`|`utensils`|
|`chargers(mostly phone)`|`kitchen knife`|`portable fan`|`vacuum`|
|`coat`|`lamp (includes home and industrial)`|`printer`|`videogame console`|
|`coffee maker`|`laptop`|`projector`|`vitamins`|
|`coffee table`|`linen`|`ram vehicles`|`wall mount`|
|`computer accessories`|`linen`|`razor`|`washing machine`|
|`conditioner`|`living room`|`ring doorbell`|`water flask`|
|`couch`|`lotion`|`romance novels`|`webcam`|
|`cpu cooler`|`luggage`|`school supplies`|`wifi router`|
|`crib*`|`makeup`|`science fiction novel`|`women bag`|
|`curtain`|`mattress/items`|`screen protector`|`women jeans`|
|`dash cam`|`men bag`|`seat cushion (pangoffice din)`|`women shirt`|
|`deodorant`|`men jeans`|`shampoo`|`women shoes`|
|`desk`|`men shirt`|`shaving cream`|`women sweater`|
|`desk lamp`|`men shoes`|`shoe rack`|`workout clothes`|
|`detergent`|`men sweater`|`smart watch`|`young adult novel`|
|`diaper`|`microphone`|`soap`|
|`dining room (mostly chiars and tables)`|`microwave`|`socks`|
|`dishwasher (mostly items for dishwasher maintenance)`|`mirror`|`solid state drive`|

<h2 style="color:#ff9900; background-color:#1c5177; padding: 10px; text-align:left; border: 1px solid #4a62d8;">Dataset Generation and Pre-processing</h2> 

### **Skip this step if you do not have access to the raw data!**

Following the compilation of all search terms, the raw JSON files are consolidated. Next, all strings undergo a cleaning process where most special characters are removed. Subsequently, each product feature is disassembled into individual tokens. This step is crucial since many raw features are formatted as compound strings like "cardigan_womens_cotton," where each token represents a distinct feature. These tokens are then assigned a value of 1 to indicate the presence of the corresponding feature in the product. Features related to dimensions or climate change readiness are disregarded during this process. It's important to note that only products with reviews are considered for further analysis.

<h2 style="color:#ff9900; background-color:#1c5177; padding: 10px; text-align:left; border: 1px solid #4a62d8;">Data Exploration</h2> 

### Preprocess Itemset and Userbase

We begin by constructing the user-item matrix, gathering all user ratings for the products. Additionally, we create the reviews matrix, which encompasses all reviews provided by each user for each product. To refine the user-item matrix, we aggregate all instances of repeated ASINs, particularly when a product is listed in multiple categories. This aggregation involves summing the values across duplicate rows to obtain the aggregated item features, ensuring a consolidated representation of each product's attributes across categories.

<p style="text-align: center;"><strong>Table 4: Search Items per Category</strong></p>

| <center><b>Categories</b></center> | <center><b>Search items</b></center> |
|:---|:---|
| ` Bedroom` | 'bedding', 'bedroom(accessories)', 'toilet', 'playroom (also includes playroom furnitures)', 'desk lamp', 'iron(supplement & for clothes)', 'lamp (includes home and industrial)', 'bedframe', 'bookshelf', 'cabinet', 'desk', 'dresser', 'night stand' 'table' |
| `Bathroom` | 'bathroom (accessories)', 'mattress/items', 'pillow', 'seat cushion (pangoffice din)', 'air purifier', 'washing machine', 'air freshener', 'mirror', 'linen' |
| `Books` | 'adventure novel', 'fantasy novel', 'historical novel', 'mystery novel', 'nonfiction novel', 'romance novels', 'science fiction novel', 'thriller novel', 'young adult novel' |
| `Car Stuff` | 'car accessories', 'dash cam', 'gps (also includes watch type GPS)', 'ram vehicles', 'tires' |
| `Children` | 'action figures', 'building toys', 'toddler toy', 'toy airplanes', 'toy cars', 'toy dolls', 'baby bottle', 'baby formula', 'baby wipes', 'car seat*', 'crib*', 'diaper', 'nurserypacifier', 'stroller' |
| `Cleaning Material` | 'vacuum', 'detergent', 'mop', 'broom', 'dishwasher (mostly items for dishwasher maintenance)', 'fabric conditioner' |
| `Computer Components` | 'cpu cooler', 'gpu', 'hard drive', 'intel amd processor', 'motherboard', 'pc chassis', 'pc fan', 'pc power supply', 'pc ram', 'solid state drive' |
| `Electronic devices` | 'camera', 'cellphone', 'headphones', 'laptop', 'monitor', 'smart watch', 'speakers', 'surveillance camera', 'tablet', 'television', 'videogame console', 'wifi router' |
| `Fashion` | 'belt', 'cap', 'coat', 'dress', 'face mask', 'jewelry', 'men bag', 'men jeans', 'men shirt', 'men shoes', 'men sweater', 'socks', 'underwear', 'women bag', 'women jeans', 'women shirt', 'women shoes', 'women sweater' |
| `Garage` | 'garage', 'battery (includes household, automotive)' |
| `Kitchen` | 'utensils', 'air fryer', 'coffee maker', 'frying pan', 'kitchen knife', 'microwave', 'oven', 'over the counter (includes appliances, countertop stuff, and meds)', 'steamer', 'stove', 'kitchen', 'dining room (mostly chiars and tables)' |
| `Living Room ` | 'carpet', 'home décor', 'living room', 'ring doorbell', 'wall mount', 'portable fan', 'curtain', 'coffee table', 'couch', 'chair', 'furniture', 'patio (mostly furniture, also includes lamps, rugs, etc.)', 'shoe rack' |
| `Mobile Accessories` | 'cables (phone chargers, extension, etc.)', 'chargers(mostly phone)', 'phone case', 'screen protector', 'tripod' |
| `Office Supplies` | 'folder', 'home_office', 'notebook', 'school supplies', 'stationary', 'office chair' |
| `Peripheral Devices` | 'keyboard', 'mouse', 'webcam', 'microphone', 'printer', 'projector', 'usb', 'computer accessories' |
| `Personal Care` | 'conditioner', 'deodorant', 'face wash', 'facial toner', 'feminine wash', 'lotion', 'makeup', 'moisturizer', 'mouthwash', 'napkin', 'razor', 'shampoo', 'shaving cream', 'soap', 'tampon', 'tissue', 'toothbrush', 'vitamins' |
| `Travel  Essentials` | 'first aid (kits)', 'luggage', 'packing cubes', 'stanley cup (tumbler & accessories)', 'travel essentials', 'water flask' |

To construct the reviews matrix and process the user-item matrix by aggregating all repeated ASINs, as well as processing the userbase by grouping by reviewerID and taking only those that have given 10 or more reviews, you can follow these steps:

### Load Dataset

1. Load your dataset containing reviews, user-item interactions, and product categories.
2. Aggregate the reviews matrix by summing up all reviews for each user and product.
3. Remove any duplicate ASINs to avoid double-counting.
4. Filter the userbase to include only those users who have given 10 or more reviews.
5. Construct the reviews matrix using the aggregated user-item interactions.
6. Use the processed userbase for further analysis or recommendation purposes.

The dataframe `df_utility` has a shape of (451, 33510), indicating 451 users and 33,510 items.

The dataframe `items_df` has a shape of (33510, 2438), indicating 33,510 items and 2,438 features.

The dataframe `asins_df` has a shape of (33510, 2), indicating 33,510 items and 2 columns, likely containing ASINs and their corresponding categories.

<h2 style="color:#ff9900; background-color:#1c5177; padding: 10px; text-align:left; border: 1px solid #4a62d8;">Streamlit Demo Application</h2>

Streamlit is an open-source Python library that simplifies the process of creating and sharing beautiful, custom web apps for machine learning and data science. It enables developers, data scientists, and analysts to turn data scripts into shareable web apps in a matter of minutes without the need for extensive front-end development experience. 

To facilitate an efficient evaluation process for researchers to assess the relevance and accuracy of recommended items, a Streamlit web application was developed. This application leverages Streamlit's interactive capabilities to provide a user-friendly interface where researchers can seamlessly navigate through recommendations, visualize pertinent data, and directly verify the appropriateness of each suggested item.

<img src="streamlit_flow.png" alt="Image Description">

<center><p><strong>Figure 19. Streamlit Flow</strong></p></center>

### Generate Recommendations per Algorithm

We focused on identifying the top 20 users based on the number of reviews submitted to achieve better recommendation results. For each of these users, the top 10 recommended items for each of the implemented algorithms—KNNBasic, KNNWithMeans, SVD, ALS, Content-Based, and LightFM—were extracted. The items reviewed by each user were also extracted and stored as a tuple together with the recommended items. These tuples were then stored in a dictionary and saved as a Pickle file. 

### Loading Pickle File to KabanMarket Web Application 

First, the app loads the user's review history and their recommended items from the Pickle file. To display item details such as the image and name, it loads these details from the reviews.csv file, using the item ID as a reference. 

A dropdown menu where you can choose from the list of top reviewers. Once a reviewer is selected, the items they have reviewed are displayed in the User History section, which can be collapsed or expanded.  

![app_userhistory.png](app_userhistory.png)
<center><p><strong>Figure 20. User History</strong></p></center>

Below this section, there are tabs you can click to view the items recommended to the user by different methods. This way, we can easily explore the items each user has reviewed and what the recommender system suggests the user might like.

![app_recommendations.png](app_recommendations.png)

<center><p><strong>Figure 21. Product Recommendations</strong></p></center>

<h2 style="color:#ff9900; background-color:#1c5177; padding: 10px; text-align:left; border: 1px solid #4a62d8;">Results and Discussion</h2>

In addition to the interpretation of results in the preceding section, the following are additional insights on the recommendation systems.
The resulting recommendations from each model can be evaluated in terms of the following:

***Relevance***

- **KNN Basic** and **ALS** both demonstrated a high level of relevance, with KNN Basic aligning well with technology-related interests and ALS covering a broad spectrum of the user's needs including tech and personal care.
- The **Content-Based** system had the lowest relevance due to its narrow focus on kitchen and home organization, diverging significantly from the user's recent tech-focused transactions.
    - **KNN with Means**, **SVD**, and **LightFM** showed moderate relevance, with each missing certain aspects of the user's interests, particularly in tech and toys.

***Novelty***

- **KNN Basic**, **KNN with Means**, **SVD**, and **ALS** introduced novel items, suggesting these systems are capable of enhancing user discovery by recommending new and unfamiliar products.
- The **Content-Based** system and **LightFM** also introduced novelty, but primarily within a narrow focus, which may limit discovery potential outside of specific interest areas.

***Serenditpity***

- **KNN Basic** and **ALS** provided serendipitous recommendations by suggesting items that might unexpectedly appeal to the user's unexpressed interests.
- **SVD** and **LightFM** also offered serendipitous finds but were more limited in scope, focusing on specific lifestyle or personal care items.
- The **Content-Based** system's potential for serendipity was constrained by its narrow focus, reducing the likelihood of surprising or delighting the user with unexpected discoveries.

***Diversity***

- **KNN Basic** and **ALS** showed the highest diversity, covering a wide range of categories that reflect the varied interests displayed in the user's transactions.
- **SVD** and **LightFM** demonstrated moderate diversity within their focused categories but failed to fully capture the breadth of the user's interests.
- The **Content-Based** system had the lowest diversity, with a singular focus on kitchen and home organization products, missing the broader range of interests evident in the user's transactions.

***Overall Model Assessment*** 

- **ALS** provides the best balance of relevance, novelty, serendipity, and diversity, where it is more aligned with the user's demonstrated interests while introducing new and potentially interesting items.
- **KNN Basic** also performs well, particularly in terms of relevance and diversity, but may benefit from further refinement to enhance novelty and serendipity.
- **KNN with Means**, **SVD**, and **LightFM** each have their strengths but might need adjustments to better capture and reflect the full spectrum of the user's interests.
- The **Content-Based** systems, atleast in this user, is the least aligned with the user's preferences, suggesting a need for a broader data set.
- Model performance also depends on consumer/purchase behavior. Transaction history with more variability may not be captured by the recommender system.
    - Less variability = more predictable
    - More variability = less predictable


The following are the exact NDCG values for each algorithm:
* KNNBasic	0.266200
* KNNWithMeans	0.263800
* SVD	0.266397
* ALS	0.997882
* Content-based with Euclidean distance	0.965205

These values became the basis of the different reccomendation system tiers to be discused in the conlusion section.

<h2 style="color:#ff9900; background-color:#1c5177; padding: 10px; text-align:left; border: 1px solid #4a62d8;">Conclusion</h2>

To address the challenge faced by up-and-coming e-commerce platforms in providing personalized experiences to users, this project successfully developed and implemented 6 recommender systems which could be leveraged by small-scale and emerging online businesses to provide tailored product recommendations and thereby unlock new market opportunities, boost user engagement, and improve overall competitiveness in the digital marketplace. By comparing the models’ performance using NDCG on the scraped Amazon dataset, the team was able to identify to 2 tiers of recommender systems that would be appropriate for the specific application / requirement of digital market owners and thereby deliver the most business value.

<p style="text-align: center;"><strong>Table 1: Basic Recommender System</strong></p>

| Model Name | Algorithm | Description | NDCG @ k=10 |
|-----|-----|-----|-----|
| Payak | KNN Basic | Recommends products based on your closest friends | 0.27 |
| Damayan |KNN with Means | Optimized method of recommending products based on your closest friends | 0.27 |
| Aparte | SVD | Recommends products based on common patterns between users and items | 0.26 |

<p style="text-align: center;"><strong>Table 2: Premium Recommender System</strong></p>

| Model Name | Algorithm | Description | NDCG @ k=10 |
|-----|-----|-----|-----|
| Barkada | Latent Factor Based Collaborative Filtering (ALS) | Recommends Products based on your closest friends | 0.99 |
| Suki | Content-Based Recommender System | Recommends Products based on your previous purchase history | 0.96 |
| Sari-sari | Hybrid Recommender System | Recommends a variety of Products that you might like based on your previous purchase history and your closest friends | 0.99 |

The results showed that the recommendations provided by the algorithms are more personalized compared to the baseline global average, which merely offers the top K most popular items.  The algorithms demonstrate a clear connection between users' history and characteristics, resulting in more relevant and engaging recommendations. While offline evaluation metrics indicate the effectiveness of the algorithms, the real test lies in online evaluation metrics, which will provide a more accurate assessment of performance in a live environment. 

The offline evaluation results and metrics suggest that all the recommender systems performed equally well, including the hybrid model using LightFM. Despite having low NDCG scores, the "Basic" recommendation systems still have their merits, recommending relevant items to the sampled users. "Premium" recommendation systems yielded the highest NDCG scores. LightFM's recommendations stand out for their ability to leverage both item and user metadata while addressing the cold start problem, generating relevant and potentially exploratory recommendations that enhance users' experience and satisfaction with the platform.  

Overall, the project has succeeded in developing recommender systems that unlock new market opportunities, boost user engagement, and improve the overall competitiveness of small-scale and emerging online businesses in the digital marketplace.

<h2 style="color:#ff9900; background-color:#1c5177; padding: 10px; text-align:left; border: 1px solid #4a62d8;">Recommendations</h2>

<h2 style="color:#1c5177; background-color:#ff9900; padding: 3px; text-align:left; border: 1px solid #ff9900;">Limitations of the Study</h2>

The team recognizes and acknowledges the assumptions and limitations that may have had an impact on the recommender systems’ performance: 

***Resource Constraints***

The task of covering all Amazon items and users posed significant challenges due to constraints in time and resources. With millions of products and users on the platform, it was impractical to gather data on every item and individual within the allotted timeframe and with available resources. As a result, the research team had to prioritize data collection efforts, focusing on a subset of items and users that were deemed representative or of particular interest for the study. This selective approach allowed for more efficient use of resources while still providing valuable insights into the recommendation system's performance and effectiveness. 

***Technical Constraints***

To minimize the effect of the cold-start problem for the non-hybrid recommender systems, the study implemented two key criteria: 

1. Include only products with at least one review 

2. Select users with a minimum of five reviews 

These measures ensured that the recommendation algorithms had sufficient data to generate meaningful suggestions, improving overall system accuracy and effectiveness. 

***Legal Constraints***

In compliance with Amazon.com's terms and conditions, the research team refrained from conducting comparisons within the platform's recommendation system. The enforceability of the website’s terms and conditions underscores the importance of adhering to legal constraints, as the data accessed is subject to Amazon’s policies. Creating an account for data collection purposes is discouraged, as it necessitates agreement to the terms and conditions. In gathering publicly available data for the recommendation system, the focus remained on factual and publicly accessible information, such as product names, prices, and features, which are typically not copyrighted. However, strict adherence to laws, regulations, and terms of service is paramount, including any restrictions on data scraping and usage imposed by the platform. Throughout the research process, the user's identity remained anonymized to ensure confidentiality and privacy [[11]](https://www.scraperapi.com/blog/is-web-scraping-legal/).

***Model Constraints***

For this project, the researchers focused exclusively on the development and implementation of recommender systems, opting not to employ predictive models. While predictive models could offer valuable insights into future trends or outcomes, the study's scope remained within the analysis and enhancement of recommendation algorithms. Despite the absence of predictive modeling, the study provided actionable recommendations for improving their performance and effectiveness. 

<h2 style="color:#1c5177; background-color:#ff9900; padding: 3px; text-align:left; border: 1px solid #ff9900;">For Further Studies and Model Improvements</h2>

To make the recommender systems more robust, the researchers suggest the following: 

***Consider Contextual Factors***  

To improve the relevance of recommendations factors, contextual factors must be taken into account, including user’s location, time of day, device type, and browsing history. By considering these, the recommender system would be able to provide recommendations tailored to each user’s specific circumstances and preferences. For example: (1) Recommending season-appropriate items based on the user’s current location, weather condition, interests, etc. (Suggesting popular jerseys during the PBA or UAAP playoffs for avid basketball or volleyball fans). (2) Recommending local event-related items based on the user’s location and time of day.  (Suggesting Panagbenga or Sinulog merchandise to locals or even prospective tourists weeks prior the festival). 

***Incorporate Real-time Data Processing***

To generate recommendations in near real time, real-time data processing must be integrated in the system for it to adapt to evolving user preferences and behavior changes. For example, if a user’s browsing behavior suddenly indicates a new interest, such as exploring gardening tools, the system can adjust its recommendations to reflect this change and suggest gardening books or equipment. Consequently, the improved system can generate recommendations in near real-time, ensuring that users receive up-to-date suggestions. For example, let’s say a user adds an item to their cart. The system can immediately generate recommendations for complementary products, such as accessories or related items other customers frequently buy together[[12]](https://www.baeldung.com/cs/amazon-recommendation-system). A statistical model may also be considered to help predict the buying behavior of a user in real-time during a session. 

***Integrate a feedback loop mechanism***

For the recommender system to be more effective, user feedback, such as ratings, reviews, and purchase history, must be continuously collected and analyzed. This feedback will help refine the recommendation models and improve the accuracy of future recommendations. By adapting to user preferences based on feedback, the models will better ensure a personalized and dynamic recommendation experience. For instance: Collecting ratings and reviews from users to refine the recommendation algorithm and improve future suggestions. Tracking user click-through rates and conversions to evaluate the effectiveness of recommendations and make adjustments accordingly[[12]](https://www.baeldung.com/cs/amazon-recommendation-system).

***Implement Advanced Algorithms***

More complex algorithms such as Deep Neural Networs can be employed  for Click-Through Rate (CTR) prediction. More advanced e-commerce platforms uses deep neural networks, such as Multi-Layer Perceptrons (MLPs) and Deep Autoencoders, for click-through rate prediction. The system can estimate the likelihood of a user clicking on a particular it by training these models on historical click data. For instance, if a user frequently purchases outdoor gear during the summer, the system can predict their interest in similar products during future summer seasons and recommend relevant items accordingly[[12]](https://www.baeldung.com/cs/amazon-recommendation-system).

***Optimize Hybrid Recommender Performance through Hyperparameter Tuning***

To enhance the performance of the hybrid recommender system, it is recommended to fully understand the hybrid model and implement hyperparameter tuning. In the case of this project, algorithms like LightFM and ALS were utilized without hyperparameter tuning. Implementing hyperparameter tuning offers the potential to significantly improve the performance of these algorithms. By fine-tuning the parameters, the model's accuracy and effectiveness in generating personalized recommendations tailored to individual user preferences can be optimized. This optimization process ensures that the hybrid recommender system operates at its full potential, providing users with more accurate and relevant suggestions, thereby enhancing their overall experience on the platform.

***Use Natural Language Processing Techniques***

To improve the specificity of product features, it is recommended to leverage Natural Language Processing (NLP) techniques to extract keywords from the long-form feature tags associated with products. NLP algorithms can analyze the textual descriptions and attributes of products to identify key terms and phrases that capture the most relevant and specific features. By incorporating NLP into the feature identification process, a more nuanced understanding of product characteristics can be obtained, enabling more accurate and detailed recommendations tailored to user preferences.

***Employ Predictive Models***

The integration of predictive models can be explored to unlock new avenues for understanding user preferences and predicting future trends in e-commerce behavior. This expansion of analytical approaches has the potential to further enhance the effectiveness of recommender systems, ultimately providing users with even more personalized and relevant recommendations. 

***Optimize Performance of Developed Models***

For the models developed in this project, several strategies can be used to optimize their performance and effectiveness: 

1. Include less popular items: Expand the recommendation pool to include items that are less popular than those currently in the itemset. This approach introduces diversity into the recommendations and ensures that users are exposed to a wider range of products. 

2. Include reviewers with fewer reviews: Broaden the userbase by including reviewers with fewer reviews than those currently in the userbase. This inclusion allows for the exploration of preferences among users who may be less active or have different tastes, thereby enriching the recommendation process. 

3. Tune hyperparameters: Optimize the performance of recommendation algorithms, not just LightFM, by tuning their hyperparameters. Fine-tuning the parameters of various algorithms can significantly improve their accuracy and effectiveness in generating personalized recommendations tailored to individual user preferences. 

<h2 style="color:#1c5177; background-color:#ff9900; padding: 3px; text-align:left; border: 1px solid #ff9900;">For Future Stakeholders and Users</h2>

E-commerce businesses who intend to utilize these recommender systems in their platforms can use an individual model or combine the strengths of the models to provide more accurate and diverse recommendations. Depending on the strategic thrust of the organization, they can implement the most fitting model in their system. For example, if the goal is to maximize repeat purchases by recurring customers, the Suki Recommender System may be the most effective, mainly due to how the algorithm works. By leveraging multiple techniques, or even combining them, digital marketplaces can enhance the overall recommendation quality and overcome limitations inherent in individual methods.

<h2 style="color:#ff9900; background-color:#1c5177; padding: 10px; text-align:left; border: 1px solid #4a62d8;">References</h2>

[[1] McKinsey & Company. (2023) What is e-commerce? ](https://www.forbes.com/sites/suzannerowankelleher/2023/06/14/most-visited-theme-parks-disney-universal/?sh=41e2ff22400a)

[[2] Amazon. (2024) Full Year 2023 Financial Results.](https://s2.q4cdn.com/299287126/files/doc_financials/2023/q4/AMZN-Q4-2023-Earnings-Release.pdf)

[[3] Statista. (2021) Worldwide retail e-commerce sales of Amazon from 2017 to 2021.](https://www.statista.com/statistics/1103390/amazon-retail-ecommerce-sales-global/)

[[4] Nick Shaw – Brightpearl. (2021) 8 Stats Amazon Sellers Need to Know in 2021.](https://www.datafeedwatch.com/blog/amazon-statistics#6.-amazon%E2%80%99s-recommendations)

[[5] Epsilon Marketing. (2018) The power of me: The impact of personalization on marketing performance.](https://www.slideshare.net/EpsilonMktg/the-power-of-me-the-impact-of-personalization-on-marketing-performance#1)

[[6] Pamela Hazelton. (2018) Study: Personalized Recommendations Produce 4 Times More Conversions.](https://www.practicalecommerce.com/study-personalized-recommendations-produce-4-times-conversions)


[[7] Is Web Scraping Legal? The Complete Guide](https://www.scraperapi.com/blog/is-web-scraping-legal/)

[[8] Aggarwal C. C. (2016) Recommender Systems: The Textbook. Springer. p.1](https://pzs.dstu.dp.ua/DataMining/recom/bibl/1aggarwal_c_c_recommender_systems_the_textbook.pdf)

[[9] Aggarwal C. C. (2016) Recommender Systems: The Textbook. Springer. p.14](https://pzs.dstu.dp.ua/DataMining/recom/bibl/1aggarwal_c_c_recommender_systems_the_textbook.pdf)

[[10] Kula, M. (2015). Metadata embeddings for user and item cold-start recommendations. In Proceedings of the 2nd Workshop on New Trends on Content-Based Recommender Systems co-located with 9th ACM Conference on Recommender Systems (RecSys 2015), Vienna, Austria, September 16-20, 2015.](http://ceur-ws.org/Vol-1448/paper4.pdf)

[[11] Lyst. (n.d.). LightFM documentation.](https://making.lyst.com/lightfm/docs/home.html)

[[12] Crawler API](https://www.algolia.com/doc/rest-api/crawler/ )