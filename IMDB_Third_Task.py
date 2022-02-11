from Firsttask import scrap_top_list
import pprint
list_1=scrap_top_list()
import json
def droup_decode(movies):
    list_1=[]
    for i in movies:
        mod=i["year"]%10
        dec=i["year"]-mod
        if dec not in list_1:
            list_1.append(dec)
    list_1.sort()
    movies_dec={}
    # key keieat dec me list chalane k bad year key bna or khali list
    for i in list_1:
        # dic pr loop chalaya or jo v movie ki detel bani hai uske liye
        movies_list=[]
        for   x in movies:
            # task2 pr loop chalaya
            if x["year"]>=i and x["year"]<=i+10:
                # taxk2 ki jab key aai tab sampair kiya ki x bda hai ya =hai fir x chota hai ya =
                movies_list.append(x)
                movies_dec[i]=movies_list
                # print(movies_list)
                with open("3task.json","w")as f:
                    json.dump(movies_dec,f,indent=5)
    return movies_dec
droup_decode(list_1)


