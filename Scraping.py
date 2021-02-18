import requests
import urllib, json
from bs4 import BeautifulSoup
import datetime
from ast import literal_eval
from Email import sentMail
import time
import timeit
import re 


regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))       
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return userInput 
            break
def inputemail(email):
    while True:
        email = input(email)
        if(re.search(regex,email)):  
            print("Valid Email")
            return email        
            break  
        else:
            print("Please Enter the Email Agian:")
            continue
            
            
  
    # pass the regular expression 
    # and the string in search() method 
    
         
print("****************************************************************************************")
email = inputemail("Enter the email you want to send notifications for : ")
t=inputNumber("Please Set Time Cooldown Data(Min):")

t = t*60
print("****************************************************************************************")

def contains(list, filter):
    for x in list:
        if filter(x):
            return True
    return False

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
        #  if data[i]['_source']['price'] != 0 :
            newdata = {
                "brandname":data[i]['_source']['brand_name'],
                "name":data[i]['_source']['model_fullname'],
                "price":str(data[i]['_source']['price']),
                "newprice":str(data[i]['_source']['new_price']),
                "datetime":data[i]['_source']['release_date_t'],
                # "image":data[i]['_source']['image_pic1'],
                "link":data[i]['_source']['link_spec']
            }
            
            sucessdata.append(newdata)
    
    fileold = literal_eval(open("data_file.json", "r").read())
    
    datanewprice = []
    datanewitem = []
    
    for checkitem in sucessdata:
        for item in fileold:
            if  checkitem['name']  == item['name']:
                if  checkitem['price'] != item['price'] :
                    datanewprice.append(checkitem)
            
            else:
                pass
        if contains(fileold, lambda x: x['name'] == checkitem['name']):
            pass
        else:
           if (checkitem in fileold) == False:
                 datanewitem.append(checkitem)
        
    
   
    if len(datanewitem) > 0:
        sentMail(datanewitem,datanewprice,email)
        with open("data_file.json", "w") as write_file:
          json.dump(sucessdata, write_file)
        print("Send Message Success")
    elif len(datanewprice) > 0:
        sentMail(datanewitem,datanewprice,email)
        with open("data_file.json", "w") as write_file:
          json.dump(sucessdata, write_file)
        print("Send Message Success")
    else:
        print("Not Sent Email")
    success()
    

               
def countdown(t): 
    while t: 
            mins, secs = divmod(t, 60) 
            timer = '{:02d}:{:02d}'.format(mins, secs) 
            print(timer, end="\r") 
            time.sleep(1)
            t -= 1
   
    scarping()

    
def success():
    countdown(int(t))
   


scarping()
