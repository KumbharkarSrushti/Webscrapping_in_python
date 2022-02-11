from bs4 import BeautifulSoup
import requests
import json
from pprint import pprint

# def ecommerce():
web_url="https://webscraper.io/test-sites"
page_1=requests.get(web_url)
# print(page_1)
soup=BeautifulSoup(page_1.text,"html.parser")
# print(soup)
main_data=soup.find("div",class_="container test-sites")
main_data1=main_data.find_all("div",class_="col-md-7 pull-right")
# pprint(main_data1)
position=0
List=[]
i=0
for i in main_data1:
    position+=1
    name1=i.find("h2",class_="site-heading").get_text().strip()
    # print(name1)
    link1=i.find("h2",class_="site-heading").a["href"]
    link2="https://webscraper.io/test-sites"+link1
    # print(link2)
    dict1={"position":position,"name":name1,"link":link2}
    List.append(dict1)
    # print(List)
    with open("ecommerce_data.json","w")as file:
        json.dump(List,file,indent=4)


# ecommerce()

