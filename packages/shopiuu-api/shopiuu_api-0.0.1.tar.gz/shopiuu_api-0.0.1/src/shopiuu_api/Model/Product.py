from ..Http.RequestCore import RequestCore
from .Model import Model

class Product(Model):
    def __init__(self, accessToken, endpoint):
        super().__init__(accessToken, endpoint)

    """
     * Create product
     * @param dict params 
       {
            "category" : "Fashion Secret Dress,kawai Dress",
            "name" : "Halloween Clothes 9996",
            "tags" : "New Product,Hot Product",
            "brand" : "",
            "supplier" : "",
            "sort" : "",
            "images" :
               [
                    "http://image.example.com/1/goods/2020-11-01/7677ebe1faa16638.jpg",
                    "http://image.example.com/1/goods/2020-11-01/93e9bef6b2b1c927.jpg"
               ],
            "price" : "100",
            "mprice" : "",
            "cprice" : "",
            "itemno" : "LC9996137-1",
            "stock" : "100",
            "instock" : "1",
            "minnum" : "",
            "option_name" :
               [
                    "Color",
                    "Size"
               ],

            "option_value" :
               [
                    "Red,Yellow",
                    "S,M,L"
               ],
            "variants" :
                [
                       {
                            "spec" : "Red,S",
                            "price" : "99",
                            "weight" : "0.5",
                            "stock" : "99",
                            "sku_code" : "LC403138-1",
                            "barcode" : ""
                       },
                       {
                            "spec" : "Red,M",
                            "price" : "99",
                            "weight" : "0.5",
                            "stock" : "99",
                            "sku_code" : "LC403138-2",
                            "barcode" : ""
                       },
                       {
                            "spec" : "Red,L",
                            "price" : "99",
                            "weight" : "0.5",
                            "stock" : "99",
                            "sku_code" : "LC403138-3",
                            "barcode" : ""
                       },
                       {
                            "spec" : "Yellow,S",
                            "price" : "99",
                            "weight" : "0.5",
                            "stock" : "99",
                            "sku_code" : "LC403138-4",
                            "barcode" : ""
                       },
                       {
                            "spec" : "Yellow,M",
                            "price" : "99",
                            "weight" : "0.5",
                            "stock" : "99",
                            "sku_code" : "LC403138-5",
                            "barcode" : ""
                       },
                       {
                            "spec" : "Yellow,L",
                            "price" : "99",
                            "weight" : "0.5",
                            "stock" : "99",
                            "sku_code" : "LC403138-6",
                            "barcode" : ""
                       }

                ],
            "weight" : "0.5",
            "title" : "",
            "keywords" : "",
            "descript" : "",
            "diy_url" : "",
            "details" : "<p>Halloween Clothes 001</p>"
       }

     * @return ResponseCore
    """
    def add(self, params):
        request = self.getRequest('/openApi/products/add')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result

    """
     * Update product
     * @param dict params 
       {
            "id" : "1",
            "category" : "Fashion Secret Dress,kawai Dress",
            "name" : "Halloween Clothes 9996",
            "tags" : "New Product,Hot Product",
            "brand" : "",
            "supplier" : "",
            "sort" : "",
            "images" :
               [
                    "http://image.example.com/1/goods/2020-11-01/7677ebe1faa16638.jpg",
                    "http://image.example.com/1/goods/2020-11-01/93e9bef6b2b1c927.jpg"
               ],
            "price" : "100",
            "mprice" : "",
            "cprice" : "",
            "itemno" : "LC9996137-1",
            "stock" : "100",
            "instock" : "1",
            "minnum" : "",
            "option_name" :
               [
                    "Color",
                    "Size"
               ],

            "option_value" :
               [
                    "Red,Yellow",
                    "S,M,L"
               ],
            "variants" :
                [
                       {
                            "spec" : "Red,S",
                            "price" : "99",
                            "weight" : "0.5",
                            "stock" : "99",
                            "sku_code" : "LC403138-1",
                            "barcode" : ""
                       },
                       {
                            "spec" : "Red,M",
                            "price" : "99",
                            "weight" : "0.5",
                            "stock" : "99",
                            "sku_code" : "LC403138-2",
                            "barcode" : ""
                       },
                       {
                            "spec" : "Red,L",
                            "price" : "99",
                            "weight" : "0.5",
                            "stock" : "99",
                            "sku_code" : "LC403138-3",
                            "barcode" : ""
                       },
                       {
                            "spec" : "Yellow,S",
                            "price" : "99",
                            "weight" : "0.5",
                            "stock" : "99",
                            "sku_code" : "LC403138-4",
                            "barcode" : ""
                       },
                       {
                            "spec" : "Yellow,M",
                            "price" : "99",
                            "weight" : "0.5",
                            "stock" : "99",
                            "sku_code" : "LC403138-5",
                            "barcode" : ""
                       },
                       {
                            "spec" : "Yellow,L",
                            "price" : "99",
                            "weight" : "0.5",
                            "stock" : "99",
                            "sku_code" : "LC403138-6",
                            "barcode" : ""
                       }

                ],
            "weight" : "0.5",
            "title" : "",
            "keywords" : "",
            "descript" : "",
            "diy_url" : "",
            "details" : "<p>Halloween Clothes 001</p>"
       }
     * The id is required, others is optional.
     * @return ResponseCore"
    """
    def update(self, params):
        request = self.getRequest('/openApi/products/update')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result

    """
     * Get products
     * @param dict params dict(
        "pagenum": 1 //页码
        "pagesize": 20 //每页数量
        "search": "keywords" //搜索标题
        "itemno": "ITEM001" //搜索商品编号
        "orderfeild": "id" //排序字段
        "ordersort": "desc" //排序方式
        "start_date": "2025-01-01" //开始日期
        "end_date": "2025-01-01" //结束日志
    }
     * @return ResponseCore
    """
    def getList(self, params):
        request = self.getRequest('/openApi/products/lists')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
    
    """·1
     * Delete article
     * @param dict params dict("id":"25")
     * @return ResponseCore
    """
    def delete(self, params):
        request = self.getRequest('/openApi/products/delete')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
