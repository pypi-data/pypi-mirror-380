from ..Http.RequestCore import RequestCore
from .Model import Model

class Payment(Model):
    def __init__(self, accessToken, endpoint):
        super().__init__(accessToken, endpoint)

    """
     * Create payment
     * @param dict params {
        "name": "PayPal" //支付方式名称
        "interface": "paypalcheckout" //支付方式接口
        "fee_interface": "paymentfee_percent_fixed" //支付方式接口
        "status": "1" //状态， 1 开启 0 关闭
        "payment_param": {
            "account":"test@paypal.com"
            "client_id":""
            "secret":""
            "is_sandbox":"1"
            "tracking_send":"1"
            "brand":"shop"
            "payment_mode":"CAPTURE"
            "express":"1"
            "smart_button":"1"
        }
        "fee_param": {
            "percent": 0
        }
        "display_param": {
            "amount_max": ""
            "amount_min": ""
            "country_whitelist": ""
            "country_blacklist": ""
        }
        "image": "//image.example.com/Upload/1/payment/2021-05-31/55d8d850af608994.jpg" // 支付图片
        "discount_descript": "" //折扣说明
        "account_descript": "" //收款账号说明
        "details": "" //支付说明
        "sort": "0" //排序
        "collect_image": "1" //是否采集图片
        }
     * @return ResponseCore
    """
    def add(self, params):
        request = self.getRequest('/openApi/payment/add')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
    
    """
     * Modify payment
     * @param dict params {
        "id":"25" //支付方式id
        "name": "PayPal" //支付方式名称
        "interface": "paypalcheckout" //支付方式接口
        "fee_interface": "paymentfee_percent_fixed" //支付方式接口
        "status": "1" //状态， 1 开启 0 关闭
        "payment_param": {
            "account":"test@paypal.com"
            "client_id":""
            "secret":""
            "is_sandbox":"1"
            "tracking_send":"1"
            "brand":"shop"
            "payment_mode":"CAPTURE"
            "express":"1"
            "smart_button":"1"
        }
        "fee_param": {
            "percent": 0
        }
        "display_param": {
            "amount_max": ""
            "amount_min": ""
            "country_whitelist": ""
            "country_blacklist": ""
        }
        "image": "//image.example.com/Upload/1/payment/2021-05-31/55d8d850af608994.jpg" // 支付图片
        "discount_descript": "" //折扣说明
        "account_descript": "" //收款账号说明
        "details": "" //支付说明
        "sort": "0" //排序
        "collect_image": "1" //是否采集图片
        }
     * @return ResponseCore
    """
    def update(self, params):
        request = self.getRequest('/openApi/payment/update')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
    
    """
     * Get payments
     * @param dict params {
        "pagenum": 1 //页码
        "pagesize": 20 //每页数量
        "search": "keywords" //搜索标题
        "interface": "paypalcheckout" //接口类型搜索
        "orderfeild": "id" //排序字段
        "ordersort": "desc" //排序方式
        "status": 1 //状态搜索
     }
     * @return ResponseCore
    """
    def getList(self, params):
        request = self.getRequest('/openApi/payment/lists')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
    
    """
     * Get all payments
     * @param dict params {
        "search": "keywords" //搜索标题
        "interface": "paypalcheckout" //接口类型搜索
        "orderfeild": "id" //排序字段
        "ordersort": "asc" //排序方式
        "status": 1 //状态搜索
     }
     * @return ResponseCore
    """
    def getAllPayments(self, params):
        request = self.getRequest('/openApi/payment/getAllPayments')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
        
    """
     * Delete payment
     * @param dict params {"id":"25"}
     * @return ResponseCore
    """
    def delete(self, params):
        request = self.getRequest('/openApi/payment/delete')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
