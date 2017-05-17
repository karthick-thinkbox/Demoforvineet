from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import requests

def post_sell_view(request):
    load={ "request": { "source_type":"web", "source_version":"1.0", "project":"baity" }, "data": { "config_type": "property" } }
    result=requests.post('http://staging.fliptango.com:2500/baity/api/getconfig/',json=load)
    list_dat=result.json()['data']['category'][0]['property_type']
    category=[]
    amenities=[]
    near_facilities=[]
    floor=[]
    wall=[]
    for item in list_dat:
        category.append(item['label'])
        for it in item['amenities']:
           amenities.append(it['label'])
        for it in item['details']:
            if it['name']=='Floor type':
                for i in it['values']:
                    floor.append(i['value'])
            elif it['name']=='Wall type':
                for i in it['values']:
                    wall.append(i['value'])   
                    
    nearfacil=result.json()['data']['nearest_facilities']
    for item in nearfacil:
        near_facilities.append(item['label'])
        
    
    amenities=set(amenities)  # to remove duplicates as API yield each property type with seperate amenities
    wall=set(wall)
    floor=set(floor)
    return render(request,'2_Property-add-post-sell.html',{'category':category,'amenities':amenities,'near_facilities':near_facilities,'floor':floor ,'wall':wall})
           
    

    


    
    


