import requests
import pandas as pd
import json
import datetime


'''
Question 1:
Write a program to download data from: 
https://api.publicapis.org/entries into an csv file. 
The code has to log the success and failure of the load with detailed logging.
'''

time = "Current timestamp: " + str(datetime.datetime.now())

try: 
    f = open("logfile.txt", "a")
    f.write("About to call API call \n")
    response = requests.get("https://api.publicapis.org/entries")
    f.write("Got a response from API call \n")
    if response.status_code == 200:
        f.write("API call is successful \n")
        f.write(time)
        f.write("\n-----------------------\n")
        response_info = json.loads(response.text)
        api_list = []
        for api_info in response_info['entries']:
                api_list.append([api_info['API'], api_info['Description'], 
                                 api_info['Auth'], api_info['HTTPS'],
                                 api_info['Cors'], api_info['Link'], 
                                 api_info['Category']])
        api_df = pd.DataFrame(data = api_list, columns = 
                              ['API', 'Description', 'Auth', 'HTTPS', 
                               'Cors', 'Link', 'Category'])
        api_df.to_csv('Output_Alex_1.csv', index = True) #Import to csv
        print(api_df.head(10))
        f.close()
    else:
        f.write("API call failed \n")
        f.write(time)
        f.write("\n-----------------------\n")
        f.close()
        response.raise_for_status
except Exception as e:
    f.write(str(e))
    f.write("\n")
    f.write(time)
    f.write("\n-----------------------\n")
    f.close()
    
'''
Question 2:
Write a program to create an index/ id column on csv from 1 to 698.
'''    
api_df.index += 1 #Move index +1
print(api_df.head(10))
api_df.to_csv('Output_Alex_2.csv', index = True) #Import to csv


'''
Question 2:
Write a program to create an index/ id column on csv from 1 to 698.
'''
category_groupby = api_df.groupby("Category").size().to_frame('Count').reset_index() #Group by Category
category_groupby = category_groupby.sort_values(['Count'], ascending = False) #Sort count descending
category_groupby.to_csv('Output_Alex_3.csv', index = False) #Import to csv
print(category_groupby.head(10)) #Display result    


