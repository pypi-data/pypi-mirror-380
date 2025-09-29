#
# Class ShopiuuException
#
# This is the class that ShopiuuClient is expected to thrown, which the caller needs to handle properly.
# It has the Api specific errors which is useful for troubleshooting.
#
# @package shopiuu-api\Core
#
class ShopiuuException(Exception):
    __details = {}

    def __init__(self, details="Something went wrong"):
        # 调用基类的构造函数
        if isinstance(details, dict):
            message = details['code'] + ': ' + details['message'] + ' RequestId: ' + details['request-id']
            super().__init__(message)
            self.__details = details
        else:
            super().__init__(details)

    def getHTTPStatus(self):
        return __details['status'] if 'status' in __details else ''

    def getRequestId(self):
        return __details['request-id'] if 'request-id' in __details else ''
        
    def getErrorCode(self):
        return __details['code'] if 'code' in __details else ''

    def getErrorMessage(self):
        return __details['message'] if 'message' in __details else ''

    def getDetails(self):
        return __details['body'] if 'body' in __details else ''
        