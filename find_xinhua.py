import requests,json


def find_it(word,page_num):
    url = "http://so.news.cn/getNews?keyword={}&curPage={}&sortField=0&searchFields=0&lang=cn".format(word,page_num)
    res = requests.get(url).text
    data = json.loads(res)
    my_list = data["content"]["results"]
    all_data = []
    for one_data in my_list:
        all_data.append(one_data["url"])
    print(all_data)



find_it("强镇改革",1)
