from Firsttask import scrap_top_list
import json
list=scrap_top_list()
def group_by_year(movies):
    years=[]
    for i in movies:
        # print(i)
        year=i["year"]
        if year not in years:
            years.append(year)
    movies_dict={i:[]for i in years}
    years.append(movies)
    for i in movies:
        # print(i)
        years=i["year"]
        # print(years)
        for x in movies_dict:
            # print(x)
            if str(x)==str(years):
                movies_dict[x].append(i)
                # print(movies_dict)
    with open("2task.json","w") as file:
        json.dump(movies_dict,file,indent=4)
    return movies_dict
    # print(movies_dict)
group_by_year(list)

