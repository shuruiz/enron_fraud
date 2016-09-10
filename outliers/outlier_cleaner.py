#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    # print net_worths
    # print "prediction",predictions
    # print "ages_train:",ages


    cleaned_data = []
    import math

    ### your code goes here
    for i in range(0,len(ages)):
        error=math.fabs(net_worths[i][0]-predictions[i][0])
        #print "errors:\n",error
        
        tup=(ages[i][0],net_worths[i][0],error)
        cleaned_data.append(tup)  
    

    
    for i in range(len(cleaned_data)-1,0,-1):
    	for j in range(0,i):
    		if cleaned_data[j][2]>cleaned_data[j+1][2]:
    			cleaned_data[j],cleaned_data[j+1]=cleaned_data[j+1],cleaned_data[j]

    cleaned_data=cleaned_data[0:81]
    #print cleaned_data


    
    return cleaned_data

