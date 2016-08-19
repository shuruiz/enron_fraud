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
print " \n"
print "E+F data set size:	"+str(len(enron_data))

print " \n"
print "data set format {[LASTNAME FIRSTNAME MIDINIT],features},this is SKILLING JEFFREY K: \n"+str(enron_data["SKILLING JEFFREY K"])

countPOI=0
for person in enron_data:
	if enron_data[person]["poi"]==1:
		countPOI+=1
print " \n"
print "POI size:	"+str(countPOI)

#explore a person's features in enron_data(/data_question/explore_enron_data.py).

# print enron_data["PRENTICE JAMES"]["total_stock_value"]
# print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

#compare money paid of CEO CFO and BOARD DIRECTOR

# print enron_data["SKILLING JEFFREY K"]["total_payments"]
# print enron_data["FASTOW ANDREW S"]["total_payments"]
# print enron_data["LAY KENNETH L"]["total_payments"]

has_salary_count=0
has_email_count=0
dont_has_totle_payment=0
poi_size=0
poi_not_has_totle_payment_size=0
for folk in enron_data:
	if enron_data[folk]["salary"] !='NaN':
		has_salary_count+=1
	if enron_data[folk]["email_address"] !='NaN':
		has_email_count+=1
	if enron_data[folk]["total_payments"]=='NaN':
		dont_has_totle_payment+=1
	if enron_data[folk]["poi"] and enron_data[folk]["total_payments"]=='NaN':
		poi_not_has_totle_payment_size+=1
print " \n"
#How many POIs in the E+F dataset have NaN for their total payments
print "has_qualified_salary_count:	  "+str(has_salary_count)
print "has_email_count: 	 "+str(has_email_count)
print " \n"
print "dont_has_totle_payment_count:	"+str(dont_has_totle_payment)
print "dont_has_totle_payment fraction:	"+str(dont_has_totle_payment*1.0/(len(enron_data)))
print " \n"
print "poi_not_has_totle_payment_percentage:	"+str(poi_not_has_totle_payment_size*1.0/countPOI)


