from ..Http.RequestCore import RequestCore
from .Model import Model

class Nav(Model):
    def __init__(self, accessToken, endpoint):
        super().__init__(accessToken, endpoint)

    """
     * getNavMenu
     * @return ResponseCore
    """
    def getNavMenu(self):
        request = self.getRequest('/openApi/nav/getNavMenu')
        result = request.set_method('GET').send_request(True)
        return result
    
    """
     * getAllNavLists
     * @return ResponseCore
    """
    def getAllNavLists(self):
        request = self.getRequest('/openApi/nav/getAllNavLists')
        result = request.set_method('GET').send_request(True)
        return result
    
    """
     * Create nav
     * @param dict params {
            [name] => bottom menu
            [code] => bottom_menu
        }
     * @return ResponseCore
    """
    def add(self, params):
        request = self.getRequest('/openApi/nav/add')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
    
    """
     * Modify nav
     * @param dict params {
            [id] => 1
            [name] => bottom menu
            [code] => bottom_menu
        }
     * @return ResponseCore
    """
    def update(self, params):
        request = self.getRequest('/openApi/nav/update')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
    
    """
     * Create menu
     * @param dict params {
            [name] => bottom menu
            [code] => bottom_menu
        }
     * @return ResponseCore
    """
    def addMenu(self, params):
        request = self.getRequest('/openApi/nav/addMenu')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
    
    """
     * Modify menu
     * @param dict paramss {
            [id] => 1
            [name] => bottom menu
            [code] => bottom_menu
        }
     * @return ResponseCore
    """
    def updateMenu(self, params):
        request = self.getRequest('/openApi/nav/updateMenu')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
        """
     * menuLists
     * @param dict paramss {
            [id] => 1  //nav id
            [code] => bottom_menu //nav code，optional
        }
     * @return ResponseCore
    """
    def menuLists(self, params):
        request = self.getRequest('/openApi/nav/menuLists')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
        
    """
     * Delete nav
     * @param dict params {"id"=>"25"}
     * @return ResponseCore
    """
    def deleteNav(self, params):
        request = self.getRequest('/openApi/nav/deleteNav')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
    
    """
     * Delete nav menu
     * @param dict params {"id"=>"25"}
     * @return ResponseCore
    """
    def deleteMenu(self, params):
        request = self.getRequest('/openApi/nav/deleteMenu')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result
