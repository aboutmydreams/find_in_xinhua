import requests,json


def find_it(word,page_num):
    url = f"http://so.news.cn/getNews?keyword={word}&curPage={page_num}&sortField=0&searchFields=0&lang=cn"

    res = requests.get(url).text
    data = json.loads(res)
    my_list = data["content"]["results"]
    all_data = [one_data["url"] for one_data in my_list]
    print(all_data)



find_it("强镇改革",1)
