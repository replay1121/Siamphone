import requests
import urllib, json
from bs4 import BeautifulSoup
import datetime
from ast import literal_eval
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
sucessdata = [];
for i in range(len(data)):
  datephone = datetime.datetime.strptime(data[i]['_source']['release_date_t'], '%Y-%m-%d').strftime("%Y-%m")
  if datanow == datephone :
      if data[i]['_source']['price'] != 0 :
        newdata = {
            "brandname":data[i]['_source']['brand_name'],
            "name":data[i]['_source']['model_fullname'],
            "price":data[i]['_source']['price'],
            "newprice":data[i]['_source']['new_price'],
            "datetime":data[i]['_source']['release_date_t'],
            "image":data[i]['_source']['image_pic1'],
        }
        # print(newdata)
        sucessdata.append(newdata)
# print(sucessdata);
# with open("data_file.json", "w") as write_file:
#     json.dump(sucessdata, write_file)
fileold = literal_eval(open("data_file.json", "r").read())
for item in fileold:
    for checkitem in sucessdata:
           if item['price'] != checkitem['price']:
               print(checkitem)