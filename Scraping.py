import requests
import urllib, json
from bs4 import BeautifulSoup
import datetime
from ast import literal_eval
from Email import sentMail
import time
import timeit



def scarping():
    url = "https://store.siamphone.com/services/spec/test?&order_by=release_date%20desc"

    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'Accept-Encoding': 'identity',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content,'html.parser')
    datanow = datetime.datetime.now().strftime("%Y-%m")


    response =  json.loads(str(soup))
    data = response['hits']['hits']
    sucessdata = []
    for i in range(len(data)):
        datephone = datetime.datetime.strptime(data[i]['_source']['release_date_t'], '%Y-%m-%d').strftime("%Y-%m")
        if datanow == datephone :
         if data[i]['_source']['price'] != 0 :
            newdata = {
                "brandname":data[i]['_source']['brand_name'],
                "name":data[i]['_source']['model_fullname'],
                "price":str(data[i]['_source']['price']),
                "newprice":str(data[i]['_source']['new_price']),
                "datetime":data[i]['_source']['release_date_t'],
                # "image":data[i]['_source']['image_pic1'],
                "link":data[i]['_source']['link_spec']
            }
            # print(newdata)
            sucessdata.append(newdata)
    # print(sucessdata);
    # with open("data_file.json", "w") as write_file:
    #      json.dump(sucessdata, write_file)
    fileold = literal_eval(open("data_file.json", "r").read())
    
    datanewprice = []
    for checkitem in sucessdata:
        for item in fileold:
            if  checkitem['name']  == item['name']:
                if  checkitem['price'] != item['price'] :
                    # print(checkitem)
                    datanewprice.append(checkitem)
                elif item['name'] != checkitem['name']:
                    #   print("newitem",checkitem)
                    datanewprice.append(checkitem)
                else:
                    print("newitem",checkitem)

    #print(checkitems)
    #sentMail(checkitems)
    #success()
    
               
def countdown(t): 
    while t: 
            mins, secs = divmod(t, 60) 
            timer = '{:02d}:{:02d}'.format(mins, secs) 
            print(timer, end="\r") 
            time.sleep(1)
            t -= 1
    success()

    
def success():
    countdown(int(10))
    scarping()

scarping()
#countdown()
#countdown(int(5)) 
#success()