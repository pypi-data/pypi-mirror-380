from shopiuu_api.ShopiuuClient import ShopiuuClient
from shopiuu_api.Core.ShopiuuException import ShopiuuException

accessToken = 'shpat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
endpoint = 'http://xxxxx.example.com/'
apiClient = ShopiuuClient(accessToken, endpoint)

try:
    products_res = apiClient.getProducts({})
    #print(products_res)
    #print(products_res.getData())
    #print(products_res.parseDataFromResponse())
    #print(products_res.getStatus())
    products = products_res.parseDataFromResponse()

    accessToken_2 = 'shpat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx2'
    endpoint_2 = 'http://xxxx2.example.com/'
    apiClient2 = ShopiuuClient(accessToken_2, endpoint_2)
    for index, product in enumerate(products['data']):
        try:
            result = apiClient2.addProduct(product)
            #print(result.getRawResponse())
            print(result.getData())
            print(result.getStatus())
        except ShopiuuException as e:
            print("添加商品失败")
            print(e)
except ShopiuuException as e:
    print("ShopiuuException异常")
    print(e)
except Exception as e:
    print("异常")
    print(e)
