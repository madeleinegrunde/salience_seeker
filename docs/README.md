# Salience Seeker
NETS Final Project

This file describes the major components of our project. Each section contains the overall goal of that component and concludes with a "Milestone" of what tangible output we expect to see at the conclusion of that component. Each major component has a point value between 1-4 points based on difficulty, with a total point value of 19.5 for our project. Each subsection describes the details of the steps necessary to complete these components, as well as how the difficulty points are calculated from each step. 


### [3.5 points] Setup

1. [0.5 points] Decide 5 changes between avatars and make groups of 1, 3, and 5 changes. Determine the number of examples of each group that will be needed to find significant results.
2. [2 points] Make avatar pairs using https://avatarmaker.com/ that differ along 1, 3, or all 5 components. Choose which avatar the worker will need to identify is the one to be identified) out of the two avatars, and add a “gold standard” word that correctly identifies the ‘correct’ avatar out of the two.
3. [0.5 point] Set up an AWS account and host the images on S3 buckets
4. [0.5 points] Create CSV files to import into MTurk. These CSV files include links to the pair of images, as well as an indication of which image will count as a “priority”


**Milestone:** The input to the first MTurk task.


### [4 points] Run MTurk Creation Task

1. [3 points] Create code that presents workers with two pictures with an indication of which one another worker should be able to choose. The task will also provide a textbox in which people write a one word distinguishing feature that they believe would be the most helpful for someone else to choose the indicated image.
2. [0.5 points] Run the experiment such that there are 3 workers per condition.
3. [0.5 points] Create a qualification such that the workers that completed this task cannot participate in the validation task.

**Milestone:** A CSV file of results from the first task, including a descriptive word for each pair of images.

### [4 points] Run quality control module
1. [3 points] Create code for the second task in which people see the 3 descriptive words and with the gold standard along with the two images. These workers must first guess the image, then select all labels that apply. We count a validation HIT as valid if the worker correctly selects the correct image and the gold standard answer.
2. [1 point] Run the experiments. Run the task until all HITs have been completed such that the gold standard answer and the correct image were selected successfully
3. [0.5 points] Only retain data from the validation task in which the validators passed the gold standard task and selected the correct image.
2. [0.5 points] Delete descriptive words that the validators say do not accurately represent the correct image.

**Milestone:** A CSV file of labels on each one-word response that indicate if that word is relevant or not.

### [4 points] Data aggregation
1. [0.5 points] Extract the sentences, words, and frequencies of words used to describe transformations.
2. [1 point] Embed the given words into word2vec
3. [2 points] Do k-means clustering of words to group them into semantic categories. Run clustering on all descriptive words, as well groups given for avatars that differ among 1, 3, or 5 different categories.
4. [0.5 points] Translate the output data into a CSV format that could be used to train a model how to change avatars using natural language

**Milestone:** Output 1: Clusters, frequencies, and lists of words used to change one avatar into another. Output2: A CSV dataset of commands to change avatars.

### [4 points] Data analysis
1. [1 points] Determine the percent of identical words used across the three workers for each pair of images.
2. [1.5 points] Across all responses, determine the semantic categories of each cluster (e.g. color, shape, texture). Identify which semantic categories are most commonly used.
3. [1.5 points] Look at the order in which multiple commands are given to find patterns in which changes people mention first.

**Milestone:** An understanding of the types of descriptions used to make changes between avatars.

# File Structure
### Deliverable 2:


*Raw data*

*Sample input/output for QC*

- docs/qualitycontrolmodel/sample_input_qc.csv: input to the quality control model

- docs/qualitycontrolmodel/output1.csv: csv file containing the descriptions of the filtered workers' responses

- docs/qualitycontrolmodel/good_workers.csv: csv file containing the worker ids of workers who answered the gold standard correctly

*Sample input/output for aggregation*

- docs/aggregation/aggregation_input.csv: input to the aggregation module

- docs/aggregation/datast.csv: the dataset for training machine learning module with the collected descriptions validated thorugh quality control

- docs/aggregation/aggregated_by_group.txt: a dictionary mapping each group, as well as an 'all' category, to its respective data. Each group stores the descriptions by words, sentences, word frequencies, and clusters. 

*Code for QC*

- docs/qualitycontrolmodel/

*Code for aggregation*

- docs/aggregation/aggregation_module.ipynb: the aggregation module code

*A disgustingly clear README telling us where we can find each of the above things*

- docs/README.md: this document


### Deliverable 1:


*Flow diagram of major system components*

- docs/flowchart.jpg: the flowchart of our project's progression. We have since updated our project from gathering single words to gathering sentences.

*Mockups of any user-facing interfaces (crowdworkers and end-users)*

- docs/Mockup1A.png: an example of our creation task

- docs/Mockup1B.png: an example of our creation task

- docs/Mockup1C.png: an example of our creation task

- docs/Mockup2.png: an example of our quality control

*README.md with required content*

- docs/README_deliverable1.md: the original README from deliverable 1, submitted last week


