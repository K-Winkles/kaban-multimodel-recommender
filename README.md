# amazon-recommender
## Abstract

Abstract here

## Problem Statement
Using Crawlbase, we built a dataset that consists of Amazon products. There are over 38,000 items across different categories such as bathroom, bedroom, television, smart watch, and more. Using content-based filtering we want to create a recommender that outputs suggested items to users. In this case, since we have the individual reviewers for each product, we will use them as “usersˮ. Here is an example entry of a “userˮ under a sample product.

## Methodology

### Summary

* Aggregate the harvested product data into one DataFrame  Create the user matrix
* Go through each product and pick up all the reviewers
* Create the item matrix
    * Create feature vectors 
* Create the user-item matrix
    * Use matrix factorization
* Try different similarity measures (dot similarity, cosine similarity, etc.)  Serve recommendations to select users
* Measure performance (top-k recommendations)
    * DCG
    * NDCG

### Specific Implementation Steps
#### Extract the data
We extracted the data by using the Crawlbase API to crawl the Amazon website and scrape approximately 38,000 items.

#### Clean the data
We collated the userbase and itembase by...

#### Identified Categories (Tentative)
* Electronics
* Children
* Books
* Household appliances
* Furniture
* Car accessories
* Travel
* Fashion
* Health

## Significance of the Study

## List of Tables

## List of Figures

## Preliminaries

## Conclusion

## Recommendations

