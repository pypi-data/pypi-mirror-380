from ..Http.RequestCore import RequestCore
from .Model import Model

class Currency(Model):
    def __init__(self, accessToken, endpoint):
        super().__init__(accessToken, endpoint)

    """
     * Create currency
     * @param dict params {
            [name] : 美元
            [symbol_left] : US 
            [symbol_code] : USD
            [symbol_right] : 
            [rate] : 1
            [decimal_points] : 2
            [country_code] : US
            [sort] : 10
            [status] : 1
        }
     * @return ResponseCore
    """
    def add(self, params):
        request = self.getRequest('/openApi/currency/add')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result

    """
     * Modify currency
     * @param dict params {
            [id] : 1
            [name] : 美元
            [symbol_left] : US 
            [symbol_code] : USD
            [symbol_right] : 
            [rate] : 1
            [decimal_points] : 2
            [country_code] : US
            [sort] : 10
            [status] : 1
        }
     * @return ResponseCore
    """
    def update(self, params):
        request = self.getRequest('/openApi/currency/update')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result

    """
     * Get currency
     * @param dict params {
        "pagenum": 1 //页码
        "pagesize": 20 //每页数量
        "search": "keywords" //搜索标题
        "symbol_code": "USD" //搜索货币符号
        "orderfeild": "id" //排序字段
        "ordersort": "desc" //排序方式
     }
     * @return ResponseCore
    """
    def getList(self, params):
        request = self.getRequest('/openApi/currency/lists')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
    
    """
     * Delete currency
     * @param dict params {"id":"25"}
     * @return ResponseCore
    """
    def delete(self, params):
        request = self.getRequest('/openApi/currency/delete')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
