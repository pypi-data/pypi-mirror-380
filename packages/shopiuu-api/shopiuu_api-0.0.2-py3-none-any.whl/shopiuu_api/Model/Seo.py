from ..Http.RequestCore import RequestCore
from .Model import Model

class Seo(Model):
    def __init__(self, accessToken, endpoint):
        super().__init__(accessToken, endpoint)

    """
     * Modify seo
     * @param dict params {
        "id":"1" //seo id 可选
        "system_id":"1" //系统seo id 可选，当id为空时，则system_id 必填
        "title": "title" //seo 标题，必填
        "keywords": "keywords" //seo 关键词，选填
        "description": "description" //seo 描述，选填
        }
     * @return ResponseCore
    """
    def update(self, params):
        request = self.getRequest('/openApi/seo/update')
        result = request.set_body(params).set_method('POST').send_request(true)
        return result

    """
     * Get seo
     * @param dict params {
        "pagenum": 1 //页码
        "pagesize": 20 //每页数量
        "search": "keywords" //搜索标题
        "orderfeild": "id" //排序字段
        "ordersort": "desc" //排序方式
     }
     * @return ResponseCore
    """
    def getList(self, params):
        request = self.getRequest('/openApi/seo/lists')
        result = request.set_body(params).set_method('POST').send_request(true)
        return result
