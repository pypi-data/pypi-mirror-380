from ..Http.RequestCore import RequestCore
from .Model import Model

class ShippingCompany(Model):
    def __init__(self, accessToken, endpoint):
        super().__init__(accessToken, endpoint)

    """
     * Create Shipping Company
     * @param dict params {
        "name": "UPS" //配送公司名称 必填
        "code": "code" //编码 必填
        }
     * @return ResponseCore
    """
    def add(self, params):
        request = self.getRequest('/openApi/shippingCompany/add')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result

    """
     * Modify Shipping Company
     * @param dict params {
        "name": "UPS" //配送公司名称 必填
        "code": "code" //编码 必填
        }
     * @return ResponseCore
    """
    def update(self, params):
        request = self.getRequest('/openApi/shippingCompany/update')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result

    """Company
     * Get Shipping Company
     * @param dict params {
        "pagenum": 1 //页码
        "pagesize": 20 //每页数量
        "search": "keywords" //搜索标题
        "code": "code" //搜索编码
        "orderfeild": "id" //排序字段
        "ordersort": "desc" //排序方式
     }
     * @return ResponseCore
    """
    def getList(self, params):
        request = self.getRequest('/openApi/shippingCompany/lists')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
    
    """
     * Delete Shipping Company
     * @param dict params {"id":"25"}
     * @return ResponseCore
    """
    def delete(self, params):
        request = self.getRequest('/openApi/shippingCompany/delete')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
