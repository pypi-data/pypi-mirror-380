from ..Http.RequestCore import RequestCore
from abc import ABC, abstractmethod

class Model(ABC):
    accessToken = ''
    endpoint = ''
    
    def __init__(self, accessToken, endpoint):
        self.accessToken = accessToken
        self.endpoint = endpoint

    def getRequest(self, api_path):
        """
        * Get RequestCore object
        * @return RequestCore
        """
        url = self.endpoint+''+api_path
        request = RequestCore(url)
        request.add_header('Content-Type','application/json').add_header('X-Shopiuu-Shop-Api-Access-token',self.accessToken)
        return request