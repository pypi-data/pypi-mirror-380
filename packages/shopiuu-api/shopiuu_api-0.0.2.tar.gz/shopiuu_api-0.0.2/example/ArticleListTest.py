from shopiuu_api.ShopiuuClient import ShopiuuClient
from shopiuu_api.Core.ShopiuuException import ShopiuuException

accessToken = 'shpat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
endpoint = 'http://xxxxx.example.com/'
apiClient = ShopiuuClient(accessToken, endpoint)

try:
    articles = apiClient.getArticles({})
    print(articles)
    print(articles.getData())
    print(articles.parseDataFromResponse())
    print(articles.getStatus())
except ShopiuuException as e:
    print("ShopiuuException异常")
    print(e)
except Exception as e:
    print("异常")
    print(e)
