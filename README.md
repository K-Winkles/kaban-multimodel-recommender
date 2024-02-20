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

#### Identified Categories
| Children         | Books               | Cleaning Material | Garage              | Kitchen          | Bedroom             | Living Room       | Bathroom           | Fashion         | Electronic devices   | Peripheral Devices | Computer Components | Mobile Accessories      | Personal Care | Car Stuff     | Office Supplies | Travel  Essentials |
|-----------------|---------------------|--------------------|---------------------|------------------|---------------------|-------------------|---------------------|-----------------|----------------------|--------------------|---------------------|-------------------------|---------------|---------------|-----------------|-------------------|
| action figures  | adventure novel     | vacuum             | garage              | utensils         | bedding             | carpet            | bathroom (accessories) | belt            | camera               | keyboard           | cpu cooler          | cables (phone chargers, extension, etc.) | conditioner   | car accessories| folder          | first aid (kits) |
| building toys   | fantasy novel       | detergent          | battery (includes household, automotive) | air fryer  | bedroom(accessories) | home décor       | mattress/items      | cap             | cellphone            | mouse              | gpu                 | chargers(mostly phone) | deodorant    | dash cam      | home_office     | luggage           |
| toddler toy     | historical novel    | mop                |                     | coffee maker     | toilet              | living room      | pillow              | coat            | headphones           | webcam             | hard drive          | phone case              | face wash    | gps (also includes watch type GPS) | notebook        | packing cubes     |
| toy airplanes   | mystery novel       | broom              |                     | frying pan       | playroom (also includes playroom furnitures) | ring doorbell    | air purifier        | dress           | laptop               | microphone         | intel amd processor | screen protector        | facial toner | ram vehicles  | school supplies | stanley cup (tumbler & accessories) |
| toy cars        | nonfiction novel    | dishwasher (mostly items for dishwasher maintenance) |                  | kitchen knife    | desk lamp           | wall mount       | washing machine     | face mask       | monitor              | printer            | motherboard         | tripod                  | feminine wash| tires         | stationary      | travel essentials |
| toy dolls       | romance novels      | fabric conditioner|                     | microwave        | iron(supplement & for clothes) |                    | air freshener       | jewelry         | smart watch          | projector          | pc chassis          |                         | lotion       | office chair  | water flask     |                   |
| baby bottle     | science fiction novel|                    | oven                | lamp (includes home and industrial) | curtain        | mirror            | men bag             | speakers        | usb                  | pc fan             |                    |                         | makeup       | seat cushion  | portable fan    |                   |
| baby formula    | thriller novel      |                    | over the counter (includes appliances, countertop stuff, and meds) | bedframe | coffee table        | linen             | men jeans           | surveillance camera | computer accessories| pc power supply     |                         | moisturizer  |               |                 |                   |
| baby wipes      | young adult novel   |                    | steamer             | bookshelf        | couch               |                   | men shirt           | tablet          | pc ram               |                    |                    |                         | mouthwash    |               |                 |                   |
| car seat*       |                     |                    | stove               | cabinet          | chair               |                   | men shoes           | television      |                      | solid state drive   |                    |                         |               |               |                 |                   |
| crib*           |                     |                    | kitchen             | desk             | furniture           |                   | men sweater         | videogame console    |                      |                    |                    |                         | shaving cream|               |                 |                   |
| diaper          |                     |                    | dining room (mostly chiars and tables) | dresser | patio (mostly furniture, also includes lamps, rugs, etc.) |                   | socks              | wifi router     |                      |                    |                         | shampoo      |               |                 |                   |
| nursery         |                     |                    | night stand         | patio (mostly furniture, also includes lamps, rugs, etc.) |                    |                     | underwear           |                    |                      |                    |                    |                         | soap         |               |                 |                   |
| pacifier        |                     |                    | table               |                  |                     |                    | women bag           |                    |                      |                    |                    |                         | tampon       |               |                 |                   |
| stroller        |                     |                    |                     |                  |                     |                    | women jeans         |                    |                      |                    |                    |                         | tissue       |               |                 |                   |
|                 |                     |                    |                     |                  |                     |                    | women shirt         |                    |                      |                    |                    |                         | toothbrush   |               |                 |                   |
|                 |                     |                    |                     |                  |                     |                    | women shoes         |                    |                      |                    |                    |                         | vitamins     |               |                 |                   |
|                 |                     |                    |                     |                  |                     |                    | women sweater       |                    |                      |                    |                    |                         |              |               |                 |                   |
|                 |                     |                    |                     |                  |                     |                    | workout clothes    |                    |                      |                    |                    |                         |              |               |                 |                   |


## Significance of the Study

## List of Tables

## List of Figures

## Preliminaries

## Conclusion

## Recommendations

