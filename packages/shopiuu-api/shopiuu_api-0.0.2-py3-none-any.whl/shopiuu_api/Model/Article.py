from ..Http.RequestCore import RequestCore
from .Model import Model

class Article(Model):
    def __init__(self, accessToken, endpoint):
        super().__init__(accessToken, endpoint)

    def add(self, params):
        """
        * Create article
        * @param dit params {
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
        request = self.getRequest('/openApi/article/add');
        result = self.set_body(params).set_method('POST').send_request(True)
        return result

    def update(self, params):
        """
        * Modify article
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
        request = self.getRequest('/openApi/article/update');
        result = request.set_body(params).set_method('POST').send_request(True)
        return result

    def getList(self, params):
        """
        * Get articles
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
        request = self.getRequest('/openApi/article/lists')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
    
    def delete(self, params):
        """
        * Delete article
        * @param dict params {"id":"25"}
        * @return ResponseCore
        """
        request = self.getRequest('/openApi/article/delete');
        result = request.set_body(params).set_method('POST').send_request(True)
        return result