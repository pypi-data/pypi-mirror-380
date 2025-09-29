from .ShopiuuException import ShopiuuException
from ..Http.ResponseCore import ResponseCore
import json

#
# Class Result, The result class of The operation of the base class, different requests in dealing with the return of data have different logic,
# The specific parsing logic postponed to subclass implementation
#
# @package Shopiuu\Core
#
class Result:

    # Indicate whether the request is successful
    _isOk = False

    # Data parsed by subclasses
    _parsedData = None

    # Store the original Response returned by the auth function
    # @var ResponseCore
    _rawResponse = None

    #
    # Result constructor.
    # @param $response ResponseCore
    # @throws ShopiuuException
    #
    def __init__(self, response):
        if response is None:
            raise ShopiuuException("raw response is empty")
        self._rawResponse = response
        self.parseResponse()

    #
    # Get requestId
    #
    # @return string
    #
    def getRequestId(self):
        requestId = ''
        try:
            requestId = rawResponse.header['x-shopiuu-request-id']
        except NameError:
            requestId = ''
        return requestId

    #
    # Get the returned data, different request returns the data format is different
    #
    # $return mixed
    #
    def getData(self):
        return self._parsedData

    #
    # Subclass implementation, different requests return data has different analytical logic, implemented by subclasses
    #
    # @return mixed
    #
    def parseDataFromResponse(self):
        content = self._rawResponse.body
        json_obj = json.loads(content)
        return json_obj

    #
    # Whether the operation is successful
    #
    # @return mixed
    #
    def isOK(self):
        return self._isOk

    #
    # @throws ShopiuuException
    #
    def parseResponse(self):
        self._isOk = self._isResponseOk()
        if self._isOk:
            self._parsedData = self.parseDataFromResponse()
        else:
            try:
                self._parsedData = self.parseDataFromResponse()
            except Exception as e:
                httpStatus = str(self._rawResponse.status)
                requestId = str(self.getRequestId())
                code = self.__retrieveErrorCode(self._rawResponse.body)
                message = self.__retrieveErrorMessage(self._rawResponse.body)
                body = self._rawResponse.body

                details = {
                    'status' : httpStatus,
                    'request-id' : requestId,
                    'code' : code,
                    'message' : message,
                    'body' : body
                }
                #print(details)
                raise ShopiuuException(details)

    def __retrieveErrorMessage(self, body):
        """
        #
        # Try to get the error message from body
        #
        # @param $body
        # @return string
        #
        """
        if body is None:
            return ''
            
        json_obj = json.loads(body)
        if json_obj['errors'] is None:
            return ''
        else:
            return str(json_obj['errors']['details'])

    def __retrieveErrorCode(self, body):
        """
        * Try to get the error Code from body
        *
        * @param $body
        * @return string
        """
        if body is None:
            return ''
            
        json_obj = json.loads(body)
        if json_obj['errors'] is None:
            return ''
        return json_obj['errors'].get('error_code','')

    def _isResponseOk(self):
        """
        * Judging from the return http status code, [200-299] that is OK
        *
        * @return bool
        """
        status = self._rawResponse.status
        if int(int(status) / 100) == 2:
            return True
            
        return False

    def getStatus(self):
        """
        * Return http status code
        *
        * @return int
        """
        status = self._rawResponse.status
        return status

    def getRawResponse(self):
        """
        * Return the original return data
        *
        * @return ResponseCore
        """
        return self._rawResponse