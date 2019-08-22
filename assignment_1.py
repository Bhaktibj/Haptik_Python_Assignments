from Assignments.assignment_2 import array
import time
import json
import datetime
import random
id = 1
current_time = datetime.datetime.now()
f = open('data_file.json','w')
arr = []
for i in range(1, 11):
    data = {
            'id' : id,
            'timeseriesid': random.choice(array),
            'val': random.randint(0,100),
            'metric': "raw",
            'timeOffset': "-5.00",
            'timestamp': str(current_time)
            }
    id += 1
    time.sleep(3)
    print("data: ", data)
    arr.append(data)
json_data = json.dumps(arr, indent=4)
f.write(json_data)







