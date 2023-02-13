'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file

infile = open("employee_data.csv", "r")
outfile = open

title = "CSR"
dep = "Marketing"

bonus = {}
read = csv.reader(infile)
for row in read:
    if row[4] == title:
        if row[3] == dep:
            # print(f"Employee name: {row[1]}{row[2]}  Current Salary {row[5]}")
            salary = row [5]
            newsal = (float(salary) * 1.1)
            name = (row[1],row[2])
            # print(f"Employee name: {row[1]}{row[2]}  Current Salary {newsal}")
            # bonus = {"manager name":row[1],"last name":row[2],"Salary":row[5]}
            bonus = {"Manager name": {name} ,"Current Salary":{salary}}
            print(bonus)
            bonus["Current Salary"] = round(newsal,3)
            print(bonus)
#create an empty dictionary


#use a loop to iterate through the csv file


    #check if the employee fits the search criteria


    

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout



          
        

        
    
