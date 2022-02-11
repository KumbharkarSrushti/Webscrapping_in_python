from  bs4 import BeautifulSoup
import requests
# from requests.models import Response
import json
def task_pickles():
    url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
    page=requests.get(url)
    soup=BeautifulSoup(page.text,"html.parser")
    # mon=soup.find("div",class_="_1gX7").span.get_text()
    div=soup.find("div",class_="_1gX7")
    div1=div.span.get_text()
    list=[]
    pickle=div1.split(" ")
    # print(pickle)
    # print(pickle)for products*split string ko htata hai
    split=int(pickle[1])
    # print(split)
    split1=split//32+1
    list=[]
    position=0
    k=1
    while k<=split1:
        url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
        # url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="
        api=requests.get(url)
        soup=BeautifulSoup(api.text,"html.parser")
        main_div=soup.find("div",class_="_3RA-")
        div=main_div.find_all("div",class_="UGUY")
        pickle_price=main_div.find_all("div",class_="_1kMS")
        link=main_div.find_all("div",class_="_3WhJ")
        i=0
        while i <len(link):
            position+=1
            pickle_name=link[i].get_text()
            price=pickle_price[i].get_text()
            link_1=(link[i].a["href"])
            link_2="https://paytmmall.com"+link_1
            dict={"position1":position,"pickle_names":pickle_name,"price":price,"link_name":link_2}
            list.append(dict)
            i=i+1
        k=k+1
    with open("pickle_data352.json","w") as file:
        json.dump(list,file,indent=5)
    return list
task_pickles()

