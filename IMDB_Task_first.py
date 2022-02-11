from bs4 import BeautifulSoup
import requests
import json
from pprint import pprint

def scrap_top_list():
    movio_url="https://www.imdb.com/india/top-rated-indian-movies/"
    page=requests.get(movio_url)
    soup=BeautifulSoup(page.text,"html.parser")
    # print(page)
    main=soup.find("div", class_="lister")
    tbody=main.find("tbody", class_="lister-list")
    trs=tbody.find_all("tr")
    list_1=[]
    a=1
    num=0
    for tr in trs:
        num=num+1
        movie_name=tr.find("td",class_="titleColumn").a.get_text()
        position_1=movie_name
        movio_release_year=tr.find("td",class_="titleColumn").span.get_text()[1:5]
        year=int(movio_release_year)
        movio_imdbRating=tr.find("td",class_="ratingColumn imdbRating").strong.get_text()
        imdbRating=float(movio_imdbRating)
        movio_poster=tr.find("td",class_="posterColumn").a["href"]
        link="https://www.imdb.com/"+movio_poster
        i={"position":num,"movio_name":position_1,"year":year,"movio_imdbRating":imdbRating,"movio_poster":link}
        list_1.append(i)

        with open ("1task.json","w")as file:
            json.dump(list_1,file,indent=4)
    return list_1
(scrap_top_list())
# pprint(ttask_1ask_1)

