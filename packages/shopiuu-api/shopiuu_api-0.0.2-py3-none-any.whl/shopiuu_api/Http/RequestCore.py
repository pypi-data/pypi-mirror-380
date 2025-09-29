from .RequestException import RequestException
from .ResponseCore import ResponseCore
from .ErrorResponse import ErrorResponse
from urllib import request, error
from urllib.parse import urlencode
import json

class RequestCore:
    request_headers = None
    request_proxy = ''
    request_user_agent = 'Shopiuu Api-sdk-python 1.0'
    request_referer = ''
    request_cookies = ''
    request_body = ''
    request_method = 'POST'
    request_url = ''
    """
     * The request timeout time, which is 600 seconds,that is, 10 minutes by default
     *
     * @var int
    """
    timeout = 600

    """
     * The connection timeout time, which is 30 seconds by default
     *
     * @var int
    """
    connect_timeout = 30
    """
     * The raw response callback headers
    """
    response_raw_headers = None

    """
     * Response body when error occurs
    """
    response_error_body = None

    """
     * The response returned by the request.
    """
    response = None

    """
     * The headers returned by the request.
    """
    response_headers = None

    """
     * The body returned by the request.
    """
    response_body = None

    """
     * The HTTP status code returned by the request.
    """
    response_code = None

    """
     * Additional response data.
    """
    response_info = None

    def __init__(self, url = None, proxy = None):
        # Set some default values.
        self.request_url = url
        #self.request_method = self::HTTP_GET
        self.request_headers = {}
        self.request_body = ''

        if proxy is not None:
            self.set_proxy(proxy)

    def set_url(self, url):
        self.request_url = url
        return self

    def set_proxy(self, proxy):
        self.request_proxy = proxy
        return self

    def set_user_agent(self, user_agent):
        self.request_user_agent = user_agent
        return self

    def set_referer(self, referer):
        self.request_referer = referer
        return self

    def set_cookies(self, cookies):
        self.request_cookies = cookies
        return self

    def set_body(self, body):
        self.request_body = body
        return self

    def set_method(self, method):
        self.request_method = method
        return self

    def add_header(self, key, value):
        self.request_headers[key] = value
        return self
    
    def pre_request(self):
        if self.request_body:
            data = self.request_body
            if isinstance(data, dict):
                data = json.dumps(data).encode('utf-8')
            req = request.Request(self.request_url, data=data, method=self.request_method.upper())
        else:
            req = request.Request(self.request_url, method=self.request_method.upper())
        if self.request_proxy:
            req.set_proxy(self.request_proxy, 'http')

        if self.request_user_agent:
            req.add_header('User-Agent', self.request_user_agent)

        if self.request_referer:
            req.add_header('Referer', self.request_referer)

        if self.request_cookies:
            req.add_header('Cookie', self.request_cookies)
            
        if self.request_headers:
            for key in self.request_headers:
                req.add_header(key, self.request_headers[key])

        return req

    def process_response(self, req = None, response = None):
        """
        * Take the post-processed cURL data and break it down into useful header/body/info chunks. Uses the
        * data stored in the `req` and `response` properties unless replacement data is passed in via
        * parameters.
        *
        * @param Request object req (Optional) The reference to the already executed cURL request.
        * @param string response (Optional) The actual response content itself that needs to be parsed.
        * @return ResponseCore A <ResponseCore> object containing a parsed HTTP response.
        """
        # Accept a custom one if it's passed.
        if req and response:
            self.response = response

        # As long as this came back as a valid resource or CurlHandle instance...
        if req:
            # Determine what's what.
            self.response_headers = dict(response.headers)
            self.response_body = response.read()
            self.response_code = response.getcode()
            
            if req and response:
                return ResponseCore(self.response_headers, self.response_body, self.response_code)

        # Return False
        return False
    
    def send_request(self, parse = False):
        req = self.pre_request()
        try:
            self.response = request.urlopen(req, timeout=self.timeout)
        except error.HTTPError as e:
            self.response = ErrorResponse(e)
        if parse:
            parsed_response = self.process_response(req, self.response)
            return parsed_response

        return self.response
    
    # RESPONSE METHODS
    def get_response_header(self, header = None):
        """
        * Get the HTTP response headers from the request.
        *
        * @param string header (Optional) A specific header value to return. Defaults to all headers.
        * @return string|array All or selected header values.
        """
        if header is not None:
            return self.response_headers[header.lower()]
        return self.response_headers

    def get_response_body(self):
        """
        * Get the HTTP response body from the request.
        *
        * @return string The response body.
        """
        return self.response_body

    def get_response_code(self):
        """
        * Get the HTTP response code from the request.
        *
        * @return string The HTTP response code.
        """
        return self.response_code