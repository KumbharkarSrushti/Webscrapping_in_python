from bs4 import BeautifulSoup
import requests,json
from pprint import pprint

pickle_url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="
page_1=requests.get(pickle_url)
soup=BeautifulSoup(page_1.text,"html.parser")
# print(soup)
div=soup.find("div",class_="_1EI9").span.get_text()
# print(div)
def pickle_list():
    URL="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="
    page1=requests.get(URL)
    soup=BeautifulSoup(page1.text,"html.parser")
    # print(soup)
    main_data=soup.find("div",class_="_3RA-")
    # pprint(div1)
    pickle_name=main_data.find_all("div",class_="UGUy")
    # pprint(pickle_name)
    pickle_price=main_data.find_all("div",class_="_1kMS")
    # pprint(pickle_price)
    pickle_link=main_data.find_all("div",class_="_3nWP")
    # pprint(pickle_link)
    link=main_data.find_all("div",class_="_3WhJ")
    # pprint(link)
    i=0
    list1=[]
    position=0
    while i<len(pickle_link):
        position+=1
        pickle_name1=link[i].get_text()
        # pprint(pickle_name1)
        pickle_price1=pickle_price[i].span.get_text()
        # pprint(pickle_price1)
        pickle_link1=(link[i].a["href"])
        pickle_link2="https://paytmmall.com/"+pickle_link1
        # pprint(pickle_link2)
        dict={"position":position,"pickle_name":pickle_name1,"pickle_price":pickle_price1,"pickle_link":pickle_link2}
        list1.append(dict)
        # pprint(list1)
        with open("pickle_data32.json","w") as file:
            json.dump(list1,file,indent=4)

        i+=1
    # return list1
pickle_list()

