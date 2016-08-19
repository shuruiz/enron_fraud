#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
#
#count poi length or feature size
# print len(enron_data)

# print len(enron_data["SKILLING JEFFREY K"])

# countPOI=0
# for person in enron_data:
# 	if enron_data[person]["poi"]==1:
# 		countPOI+=1
# print countPOI

#explore a person's features in enron_data(/data_question/explore_enron_data.py).

print enron_data["PRENTICE JAMES"]["total_stock_value"]
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]



