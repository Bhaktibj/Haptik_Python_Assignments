import json
array = []
fo = open('chiller.json','r')
dict_data = json.load(fo)
for k in dict_data:
    print(k)
    val = k['id']
    array.append(val)
print("id:",array)

