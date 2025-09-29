# 创建一个类似response的对象来包装这个异常
class ErrorResponse:
    def __init__(self, error_obj):
        self.error_obj = error_obj
        self.code = error_obj.code
    
    def getcode(self):
        return self.code
    
    def geturl(self):
        return self.error_obj.geturl()
    
    def info(self):
        return self.error_obj.headers
    
    def read(self):
        if hasattr(self.error_obj, 'fp') and self.error_obj.fp:
            return self.error_obj.fp.read()
        return b''
    
    def __getattr__(self, name):
        # 转发其他属性到原始error对象
        return getattr(self.error_obj, name)