from ..Http.RequestCore import RequestCore
from .Model import Model

class Shipping(Model):
    def __init__(self, accessToken, endpoint):
        super().__init__(accessToken, endpoint)

    """
     * Create Shipping
     * @param dict params {
        "name": "UPS" //配送方式名称 必填
        "interface": "firstaddedweight" //运费公式
        "status": "1" //状态， 1 开启 0 关闭
        "shipping_param": {
            "first_weight": "0.5"
            "added_weight": "0.5"
            "first_price": "30"
            "added_price": "6"
            "freeshipping_price": "0"
            "freeshipping_num": "1"
            "limit_weight": "0"
        }
        "display_param": {
            "amount_max": ""
            "amount_min": ""
            "country_whitelist": ""
            "country_blacklist": ""
        }
        "image": "//image.example.com/Upload/1/shipping/2021-05-31/55d8d850af608994.jpg" // 配送方式图片
        "time_descript": "" //时效说明
        "details": "" //配送方式说明
        "sort": "0" //排序
        "collect_image": "1" //是否采集图片
        "area_id": "0" //配送区域id
        "shipping_company_id": "0" //配送公司id
       }
     * @return ResponseCore
    """
    def add(self, params):
        request = self.getRequest('/openApi/shipping/add')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result

    """
     * Modify Shipping
     * @param dict params {
        "name": "UPS" //配送方式名称 必填
        "interface": "firstaddedweight" //运费公式
        "status": "1" //状态， 1 开启 0 关闭
        "shipping_param": {
            "first_weight": "0.5"
            "added_weight": "0.5"
            "first_price": "30"
            "added_price": "6"
            "freeshipping_price": "0"
            "freeshipping_num": "1"
            "limit_weight": "0"
        }
        "display_param": {
            "amount_max": ""
            "amount_min": ""
            "country_whitelist": ""
            "country_blacklist": ""
        }
        "image": "//image.example.com/Upload/1/shipping/2021-05-31/55d8d850af608994.jpg" // 配送方式图片
        "time_descript": "" //时效说明
        "details": "" //配送方式说明
        "sort": "0" //排序
        "collect_image": "1" //是否采集图片
        "area_id": "0" //配送区域id
        "shipping_company_id": "0" //配送公司id
       }
     * @return ResponseCore
    """
    def update(self, params):
        request = self.getRequest('/openApi/shipping/update')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result

    """
     * Get Shipping
     * @param dict params {
        "pagenum": 1 //页码
        "pagesize": 20 //每页数量
        "search": "keywords" //搜索标题
        "shipping_company_id": "1" //搜索配送公司id
        "orderfeild": "id" //排序字段
        "ordersort": "desc" //排序方式
     }
     * @return ResponseCore
    """
    def getList(self, params):
        request = self.getRequest('/openApi/shipping/lists')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result

    """
     * Get All Shippings
     * @param dict params {
        "search": "keywords" //搜索标题
        "shipping_company_id": "1" //搜索配送公司id
        "orderfeild": "id" //排序字段
        "ordersort": "asc" //排序方式
     }
     * @return ResponseCore
    """
    def getAllShippings(self, params):
        request = self.getRequest('/openApi/shipping/getAllShippings')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
    
    """
     * Delete Shipping
     * @param dict params {"id":"25"}
     * @return ResponseCore
    """
    def delete(self, params):
        request = self.getRequest('/openApi/shipping/delete')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
