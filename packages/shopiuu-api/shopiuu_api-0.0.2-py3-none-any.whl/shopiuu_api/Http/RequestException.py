"""
 * Class RequestException
 *
 * This is the class that ShopiuuClient is expected to thrown, which the caller needs to handle properly.
 * It has the Api specific errors which is useful for troubleshooting.
 *
 * @package Shopiuu\Http
"""
class RequestException(Exception):
    def __init__(self, message="Something went wrong"):
        # 调用基类的构造函数
        super().__init__(message)