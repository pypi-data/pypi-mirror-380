from ..Http.RequestCore import RequestCore
from .Model import Model

class ShippingArea(Model):
    def __init__(self, accessToken, endpoint):
        super().__init__(accessToken, endpoint)

    """
     * Create Shipping Area
     * @param dict params {
        "name": "USA" //配送区域名称
        "description": "description" //描述
        "areas": [
                {
                    "country_id": 1 //必填
                    "state_id": 1 //选填
                }
                ...
            ]
        } //选填
     * @return ResponseCore
    """
    def add(self, params):
        request = self.getRequest('/openApi/shippingArea/add')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result

    """
     * Modify Shipping Area
     * @param dict params {
        "name": "USA" //配送区域名称
        "description": "description" //描述
        "areas": [
                {
                    "country_id": 1 //必填
                    "state_id": 1 //选填
                }
                ...
            ]
        } //选填
     * @return ResponseCore
    """
    def update(self, params):
        request = self.getRequest('/openApi/shippingArea/update')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result

    """
     * Get Shipping Area
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
        request = self.getRequest('/openApi/shippingArea/lists')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
    
    """
     * Delete Shipping Area
     * @param dict params {"id":"25"}
     * @return ResponseCore
    """
    def delete(self, params):
        request = self.getRequest('/openApi/shippingArea/delete')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
