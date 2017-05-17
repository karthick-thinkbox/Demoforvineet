import requests
import json
load={ "request": { "source_type":"web", "source_version":"1.0", "project":"baity" }, "data": { "config_type": "property" } }
res=requests.post('http://staging.fliptango.com:2500/baity/api/getconfig/',json=load)
list_dat=res.json()['data']['category'][0]['property_type']
#print(list_dat)
category=[]
facilities=[]
near=[]
floor=[]
wall=[]
for item in list_dat:
    #print(item['label'])
    category.append(item['label'])
    #print("-------")
    for it in item['amenities']:
       # print(it['label'])
        facilities.append(it['label'])
        
    for it in item['details']:
        #print (it['values'])
        if it['name']=='Floor type':
            for i in it['values']:
                floor.append(i['value'])
        elif it['name']=='Wall type':
            for i in it['values']:
                wall.append(i['value'])
        
                
        
                
        
nearfacil=res.json()['data']['nearest_facilities']
for item in nearfacil:
    near.append(item['label'])
    


'''      
print("Property Type")
print(category)
facil=set(facilities)
print("facilities")
print(facil)

'''
wall=set(wall)
floor=set(floor)
print("wall Type" )

#print(floor)
print(wall)


keys=res.json()['data'].keys()
#print(keys)


    
    
