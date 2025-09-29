from ..Http.RequestCore import RequestCore
from .Model import Model

class ArticleCategory(Model):
    def __init__(self, accessToken, endpoint):
        super().__init__(accessToken, endpoint)

    """
     * Create articleCategory
     * @param dict params {
        "name": "Sexy Lingerie 005" //文章标题
        "image": "//image.example.com/Upload/1/article/2021-05-31/55d8d850af608994.jpg" // 文章图片
        "status": "1" //状态， 1 开启 0 关闭
        "sort": "0" //排序
        "diy_url": "Sexy-Lingerie-003.html" //定义url
        "title": "title" //seo 标题
        "keywords": "keywords" //seo 关键词
        "descript": "descript" //seo 描述
        "details": "<p>Sexy Lingerie 005</p>" //文章内容
        "category": "News" //文章类目
        "collect_image": "1" //是否采集图片
        }
     * @return ResponseCore
    """
    def add(params):
        request = self.getRequest('/openApi/articleCategory/add')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
    
    """
     * Modify articleCategory
     * @param dict params {
        "id":"25" //文章id
        "name": "Sexy Lingerie 005" //文章标题
        "image": "//image.example.com/Upload/1/article/2021-05-31/55d8d850af608994.jpg" // 文章图片
        "status": "1" //状态， 1 开启 0 关闭
        "sort": "0" //排序
        "diy_url": "Sexy-Lingerie-003.html" //定义url
        "title": "title" //seo 标题
        "keywords": "keywords" //seo 关键词
        "descript": "descript" //seo 描述
        "details": "<p>Sexy Lingerie 005</p>" //文章内容
        "category": "News" //文章类目
        "collect_image": "1" //是否采集图片
        }
     * @return ResponseCore
    """
    def update(self, params):
        request = self.getRequest('/openApi/articleCategory/update')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
    
    """
     * Get articleCategories
     * @param dict params {
        "pagenum": 1 //页码
        "pagesize": 20 //每页数量
        "search": "keywords" //搜索标题
        "orderfeild": "id" //排序字段
        "ordersort": "desc" //排序方式
        "start_date": "2025-01-01" //开始日期
        "end_date": "2025-01-01" //结束日志
     }
     * @return ResponseCore
    """
    def getList(self, params):
        request = self.getRequest('/openApi/articleCategory/lists')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
    
    """
     * Get getCategories
     * @param dict params {
        "pagenum": 1 //页码
        "pagesize": 20 //每页数量
        "search": "keywords" //搜索标题
        "orderfeild": "id" //排序字段
        "ordersort": "desc" //排序方式
        "start_date": "2025-01-01" //开始日期
        "end_date": "2025-01-01" //结束日志
     }
     * @return ResponseCore
    """
    def getCategories(self):
        request = self.getRequest('/openApi/articleCategory/getCategories')
        result = request.set_method('GET').send_request(True)
        return result
    
    """
     * Get getCategoryTree
     * @return ResponseCore
    """
    def getCategoryTree(self):
        request = self.getRequest('/openApi/articleCategory/getCategoryTree')
        result = request.set_method('GET').send_request(True)
        return result
        
    """
     * Delete articleCategory
     * @param dict params {"id":"25"}
     * @return ResponseCore
    """
    def delete(self, params):
        request = self.getRequest('/openApi/articleCategory/delete')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
