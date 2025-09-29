"""
 * Container for all response-related methods.
"""
class ResponseCore:
    """
     * Store the HTTP header information.
    """
    header = None

    """
     * Store the SimpleXML response.
    """
    body = None

    """
     * Store the HTTP response code.
    """
    status = None

    def __init__(self, header, body, status = None):
        """
        * Construct a new instance of this class.
        *
        * @param array $header (Required) Associative array of HTTP headers (typically returned by <RequestCore::get_response_header()>).
        * @param string $body (Required) XML-formatted response from Api.
        * @param integer $status (Optional) HTTP response status code from the request.
        * @return Mixed Contains an <php:array> `header` property (HTTP headers as an associative array), a <php:SimpleXMLElement> or <php:string> `body` property, and an <php:integer> `status` code.
        """
        self.header = header
        self.body = body
        self.status = status

    def isOK(codes = (200, 201, 204, 206)):
        """
        * Did we receive the status code we expected?
        *
        * @param integer|array $codes (Optional) The status code(s) to expect. Pass an <php:integer> for a single acceptable value, or an <php:array> of integers for multiple acceptable values.
        * @return boolean Whether we received the expected status code or not.
        """
        if isinstance(codes, dict):
            return self.status in codes
        return self.status == codes