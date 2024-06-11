from bs4 import BeautifulSoup as bs
import requests as rq
import pandas as pd

list1 = []
list2 = []
list3 = []

for i in range(1, 57):
    url = "https://www.flipkart.com/search?q=multitasking+laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_19_sc_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_19_sc_na_ps&as-pos=1&as-type=RECENT&suggestionId=multitasking+laptop%7CLaptops&requestId=4b641ee5-f9fb-47b5-8ca3-0063e6a3edb9&as-searchtext=multitaskinglaptops" + str(i)
    header = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)'}
    req = rq.get(url,headers=header)
    bea = bs(req.text, "html.parser")
    
    #box = bea.find("div", class_="DOjaWF gdgoEp")
    
    laptops_names = bea.findAll("div", class_="KzDlHZ")
    for w in laptops_names:
        list1.append(w.text)

    description = bea.findAll("ul", class_="G4BRas")
    for x in description:
        list2.append(x.text)
    
    price= bea.findAll("div", class_="Nx9bqj _4b5DiR")
    for y in price:
        list3.append(y.text)

    data = {
    'laptop_name':list1,
    'laptop_description':list2,
    'laptop_price':list3
           }
    
    df = pd.DataFrame(data)
print(df)

#df.to_csv('all_laptos_info.csv')