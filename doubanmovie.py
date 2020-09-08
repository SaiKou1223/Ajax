import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}
# url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20'
url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=100'
# start 起始序号-1
# limit 展示个数
res = requests.get(url,headers=headers).json()
for item in res:
    rate = item['rank']
    title = item['title']
    score = item['score']
    time = item['release_date']
    num = item['vote_count']
    print("排名:",rate,"名字:",title,"评分:",score,"发布时间:",time,"评分人数:",num,)