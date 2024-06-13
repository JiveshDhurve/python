from bs4 import BeautifulSoup as bs
import requests as rq
import pandas as pd

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []

for i in range(1, 16):
    url ="https://www.flipkart.com/search?q=gaming+laptops&otracker=AS_Query_HistoryAutoSuggest_2_0&otracker1=AS_Query_HistoryAutoSuggest_2_0&marketplace=FLIPKART&as-show=on&as=off&as-pos=2&as-type=HISTORY&p%5B%5D=facets.rating%255B%255D%3D3%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.rating%255B%255D%3D2%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.rating%255B%255D%3D1%25E2%2598%2585%2B%2526%2Babove"+ str(i)
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

    ratings = bea.find_all("div",class_="XQDdHH")
    for z in ratings:
        list4.append(z.text)

    number_of_ratings = bea.find_all("span",class_="Wphh3N")
    for a in number_of_ratings:
        list5.append(a.text)
    
    original_laptop_price = bea.find_all("div",class_="yRaY8j ZYYwLA")
    for b in original_laptop_price:
        list7.append(b.text)

    discount_on_laptop = bea.find_all("div",class_="UkUFwK")
    for c in discount_on_laptop:
        list6.append(c.text)

    

    data = {
    'laptop_name':list1,
    'laptop_description':list2,
    'laptop_rating':list4,
    'number_of_people_rated_and_reviewed':list5,
    'discounted_laptop_price':list3,
    'original_laptop_price':list7,
    'discount_on_laptop':list6
    
           }
    
    df = pd.DataFrame(data)
print(df)

df.to_csv('data360.csv')