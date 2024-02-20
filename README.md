# amazon-recommender
## Abstract

Abstract here

## Problem Statement
Using Crawlbase, we built a dataset that consists of Amazon products. There are over 38,000 items across different categories such as bathroom, bedroom, television, smart watch, and more. Using content-based filtering we want to create a recommender that outputs suggested items to users. In this case, since we have the individual reviewers for each product, we will use them as “usersˮ. Here is an example entry of a “userˮ under a sample product.

## Methodology

### Summary

* Aggregate the harvested product data into one DataFrame Create the user matrix
* Go through each product and pick up all the reviewers
* Create the item matrix
    * Create feature vectors 
* Create the user-item matrix
    * Use matrix factorization
* Try different similarity measures (dot similarity, cosine similarity, etc.) Serve recommendations to select users
* Measure performance (top-k recommendations)
    * DCG
    * NDCG

### Specific Implementation Steps
#### Extract the data
We extracted the data by using the Crawlbase API to crawl the Amazon website and scrape approximately 38,000 items.

![DataExtraction](images/DataExtraction.png)

#### Clean the data
We collated the userbase and itembase by...

![DataCleaning](images/DataCleaning.png)

#### Identified Categories (Tentative)
| Fashion         | Electronic devices   | Peripheral Devices | Computer Components | Mobile Accessories      | Personal Care | Car Stuff     | Office Supplies | Travel Essentials |
|-----------------|----------------------|--------------------|---------------------|-------------------------|---------------|---------------|-----------------|-------------------|
| belt            | camera               | keyboard           | cpu cooler          | cables (phone chargers, extension, etc.) | conditioner   | car accessories| folder          | first aid (kits) |
| cap             | cellphone            | mouse              | gpu                 | chargers (mostly phone) | deodorant    | dash cam      | home_office     | luggage           |
| coat            | headphones           | webcam             | hard drive          | phone case              | face wash    | gps (also includes watch type GPS) | notebook        | packing cubes     |
| dress           | laptop               | microphone         | intel amd processor | screen protector        | facial toner | ram vehicles  | school supplies | stanley cup (tumbler & accessories) |
| face mask       | monitor              | printer            | motherboard         | tripod                  | feminine wash| tires         | stationary      | travel essentials |
| jewelry         | smart watch          | projector          | pc chassis          |                         | lotion       | office chair  | water flask     |                   |
| men bag         | speakers             | usb                | pc fan              |                         | makeup       |               |                 |                   |
| men jeans       | surveillance camera | computer accessories| pc power supply     |                         | moisturizer  |               |                 |                   |
| men shirt       | tablet               | pc ram             |                     |                         | mouthwash    |               |                 |                   |
| men shoes       | television           |                    | solid state drive   |                         |               |               |                 |                   |
| men sweater     | videogame console    |                    |                     |                         | shaving cream|               |                 |                   |
| socks           | wifi router          |                    |                     |                         | shampoo      |               |                 |                   |
| underwear       |                      |                    |                     |                         | soap         |               |                 |                   |
| women bag       |                      |                    |                     |                         | tampon       |               |                 |                   |
| women jeans     |                      |                    |                     |                         | tissue       |               |                 |                   |
| women shirt     |                      |                    |                     |                         | toothbrush   |               |                 |                   |
| women shoes     |                      |                    |                     |                         | vitamins     |               |                 |                   |
| women sweater   |                      |                    |                     |                         |              |               |                 |                   |
| workout clothes |                      |                    |                     |                         |              |               |                 |                   |

## Significance of the Study

## List of Tables

## List of Figures

## Preliminaries

## Conclusion

## Recommendations

