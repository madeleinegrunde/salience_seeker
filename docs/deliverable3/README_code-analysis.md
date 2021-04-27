# Code Documentation

## Creation task [implemented]

Collects the worker responses through a < crowd-form > object. Within this object there are:
- instructions for the task
- two images
- a crowd input textbox

This structure allows us to input two images and recieve in return a description of how to turn one image into another. 

## Quality control task [implemented]

Collects the worker responses through a < crowd-form > object. Within this object there are: 
- instructions for the task
- two images
- a < crowd-classifier > object that allows the person to choose which image shows the updated avatar
- four < crowd-checkbox> items associated with descriptons. Three of these descriptions come from the creation task, and one comes from our gold standard output.


This structure allows us to input two images and three descriptions and recieve in return which descriptions are valid. We double check attention by asking which of the images is the final, updated avatar.


## Quality control analysis [implemented]

### gold_standard_votes

Checks if the worker correctly selects the updated image and the gold standard answer. If this is the case, the worker is considered a "good worker", and the descriptions they chose are added to our list of descriptions.

### gold_standard_votes_workers

Takes the mturk data and returns a list of good workers. 

### main

Reads in the input from the mturk responses. Then, it calls functions to get the descriptions that were validated as correct from good workers and a list of good workers. Finally, it saves this information. 


## Aggregation module [implemented]

### Imports
Imports all the necessary packages

### Extract descriptions from quality control output

Contains a series of function that takes an output file of the quality control module and extracts the descriptions. From these functions we can extract a dataframe of data, the sentences, the words, and a dictionary mapping words to the number of times they occur. 

### Embedding and clustering

These functions first get the GloVe embeddings of the words in the descriptions (besides a hand-coded list of uninteresting words such as "the"). 

Then, there are functions to run a k-means clustering algorithm on all the words to find clusters, and to stort these clusters into a useable data format. 

### Put data into correct format

These functions take the extracted data and collect the sentences, words, frequencies, and clusters for each group. A group is defined as the images that have 1, 2, or 3 changes.

### Overall functions to retrieve data

This section calls the functions established in the previous sections, then saves the aggregated data.

## Analysis


### Description length and variety

First, we will do general analysis on the descriptions. We will determine the number of words used per description, as well as the variety of words used for each description. We will do this analysis over the entire dataset as well as for each individual group. By separating by group we can see description length as a function of the number of differences between the two images.


### Semantic categories

Run the clustering algorithm with various numbers of clusters and determine the number that leads to the least total within-cluster variation. Examine these clusters by hand to determine the semnatic categories used (e.g. color, shape, texture) and the frequency of each.


### Hand coding 

We will hand code the results along multiple dimensions. 

First, we will find the percentage of descriptions that describe just physical attributes as well as those that describe non-physical attributes such as emotion. 

Second, we will check to see if each description captured all existing differences, and if they included differences that did not exist. We will analyze the prevalence of each of these phenomena. We will also investigate the data to see if there are certain categories of changes that are left out or mistaken most often.


### Scaling up to an entire dataset

Our format would be able to train a machine learning model to change avatars based on natural language descriptions. However, we are collecting information for 35 avatar pairs, which is not enough data to appropriately train a model. We will investigate how much money and time it would take to create a full dataset of labeled data. For example, this paper (https://www.aclweb.org/anthology/L18-1683.pdf) uses the Visual Genome dataset to train image editing from natural language descriptions. The Visual Genome dataset has 108k images. Therefore, we will see how expensive it would be in terms of money and time to label 100k sets of images. 



### Required information

All of this analysis just requires the natural language descriptions, which we are successfully collecting. 

