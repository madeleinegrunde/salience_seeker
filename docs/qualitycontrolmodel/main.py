############################################################
# NETS 213: Salience Seeker - Quality Control Module
############################################################

import pandas as pd
import csv

# use gold standards for quality control
def gold_standard_votes(mturk_res):
  # dataframe containing all relevant data
  df = mturk_res[["og_image", "updated_image", "description_1", "description_2", "description_3", "gold_standard", "img_choice", "ans_1", "ans_2", "ans_3", "ans_gold_standard", "set", "group"]]
  
  # map from image to set of descriptions from good workers
  imageToDesc = {}
  # iterate over the rows
  for index, row in df.iterrows():
    image = row['img_choice']
    og = row['og_image']
    desc_1 = row['description_1']
    desc_2 = row['description_2']
    desc_3 = row['description_3']
    set_num = row['set']
    group_num = row['group']
    # initialize empty set for each image
    if image not in imageToDesc.keys():
      imageToDesc[image] = (set(), [], og)
    if image == row['updated_image'] and row['ans_gold_standard'] == True:
      # good worker, all chosen descriptions get added to set
      if row['ans_1'] == True: imageToDesc[image][0].add(desc_1)
      if row['ans_2'] == True: imageToDesc[image][0].add(desc_2)
      if row['ans_3'] == True: imageToDesc[image][0].add(desc_3)
    imageToDesc[image][1].append(set_num)
    imageToDesc[image][1].append(group_num)
    
  # convert map to list of tuples
  # [ (og_image_url, updated_image_url, ['change mouth to frown', 'change eyebrows to be thicker...'], 1, 2), 
  #   (og_image_url2, updated_image_url2, ['change eye shape to be bigger, ...'], 1, 3), 
  # ...]
  return [(descs[2], img, list(descs[0]), descs[1][0], descs[1][1] ) for img, descs in imageToDesc.items()]
  


# get the good workers as a list
def gold_standard_votes_workers(mturk_res):
  # dataframe containing all relevant data
  df = mturk_res[["worker_id", "updated_image", "img_choice", "ans_gold_standard"]] 

  # set of good workers (correct gold standard answers)
  goodWorkers = set()

  # iterate over the rows and add the good workers
  for index, row in df.iterrows():
    if row['img_choice'] == row['updated_image'] and row['ans_gold_standard'] == True:
      goodWorkers.add(row['worker_id']) # TODO: REPLACE WORKER ID WITH WHATEVER WE USE TO IDENTIFY THEM

  # convert to a list and return
  return list(goodWorkers)

# Your main function

def main():
    # Read in CVS result file with pandas
    mturk_res = pd.read_csv('sample_input_qc.csv').dropna()
    

    # get the majority votes
    votes = gold_standard_votes(mturk_res)

    # get the good workers
    workers = gold_standard_votes_workers(mturk_res)
    print(workers)

    # generate output1 csv containing majority votes
    with open('output1.csv','w') as out:
      csv_out=csv.writer(out)
      csv_out.writerow(['og_image', 'updated_image', 'descriptions', 'set', 'group'])
      for row in votes:
        csv_out.writerow(row)
    
    with open('good_workers.csv', 'w') as out:
      csv_out=csv.writer(out)
      csv_out.writerow(['worker_id']) 
      for row in workers:
        csv_out.writerow([row])


if __name__ == '__main__':
    main()