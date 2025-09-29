from ..Http.RequestCore import RequestCore
from .Model import Model

class EmbedCode(Model):
    def __init__(self, accessToken, endpoint):
        super().__init__(accessToken, endpoint)

    """
     * Create embed code
     * @param dict params {
            [name] : Hide price
            [details] : <style>.price{display:none}</style>
            [position] : BODY_BOTTOM
            [page_code] : 
            [status] : 1
            [only_show_once] : N
        }
     * @return ResponseCore
    """
    def add(self, params):
        request = self.getRequest('/openApi/embedCode/add')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
    
    """
     * Modify embed code
     * @param dict paramss {
            [id] : 1
            [name] : Hide price
            [details] : <style>.price{display:none}</style>
            [position] : BODY_BOTTOM
            [page_code] : 
            [status] : 1
            [only_show_once] : N
        }
     * @return ResponseCore
    """
    def update(self, params):
        request = self.getRequest('/openApi/embedCode/update')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
    
    """
     * Get embed code
     * @param dict params {
        "pagenum": 1 //页码
        "pagesize": 20 //每页数量
        "search": "keywords" //搜索标题
        "position": "BODY_BOTTOM" //搜索位置编码
        "page_code": "checkout_success" //搜索页面编码
        "orderfeild": "id" //排序字段
        "ordersort": "desc" //排序方式
     }
     * @return ResponseCore
    """
    def getList(self, params):
        request = self.getRequest('/openApi/embedCode/lists')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
        
    """
     * Delete embed code
     * @param dict params {"id":"25"}
     * @return ResponseCore
    """
    def delete(self, params):
        request = self.getRequest('/openApi/embedCode/delete')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
