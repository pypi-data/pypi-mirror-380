from ..Http.RequestCore import RequestCore
from .Model import Model

class StoreTheme(Model):
    def __init__(self, accessToken, endpoint):
        super().__init__(accessToken, endpoint)

    """
     * Get store themes
     * @return ResponseCore
    """
    def getList(self):
        request = self.getRequest('/openApi/storeTheme/lists')
        result = request.set_method('GET').send_request(True)
        return result

    """
     * Get store theme files
     * @return ResponseCore
    """
    def getThemeFiles(self, params):
        request = self.getRequest('/openApi/storeTheme/getThemeFiles')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result

    """
     * Get store theme files
     * @return ResponseCore
    """
    def createTheme(self, params):
        request = self.getRequest('/openApi/storeTheme/createTheme')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
    
    """
     * Delete store theme
     * @param dict params {"id":"25"}
     * @return ResponseCore
    """
    def delete(self, params):
        request = self.getRequest('/openApi/storeTheme/delete')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
