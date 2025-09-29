from ..Http.RequestCore import RequestCore
from .Model import Model

class Settings(Model):
    def __init__(self, accessToken, endpoint):
        super().__init__(accessToken, endpoint)

    """
     * Modify article
     * @param dict params {
        "config_web_title" : title
        "config_web_keywords" : keywords
        "config_web_description" : description
        "config_web_copyright" : Copyright © 2020 SHOP INC. All Rights Reserved.
        "config_robotstxt" : User-agent: *
    Allow: /
    User-agent: baiduspiter_bot
    Disallow: /
        "config_base_language" : 2
        "config_base_currency" : 1
        "config_store_timezone" : GMT+8
        "config_search_analyzer" : icu_analyzer
        "config_emailconfig_adminemail" : test@qq.com
        "config_emailconfig_sendemail" : 
        "config_emailconfig_password" : 
        "config_emailconfig_nickname" : 
        "config_emailconfig_smtp" : 
        "config_emailconfig_port" : 
        "config_emailconfig_replyemail" : test@qq.com
        "config_visit_limit_username" : admin
        "config_visit_limit_password" : 123456
        "config_visit_limit_redirect_type" : 1
        "config_visit_limit_descript" : 
        "config_visit_limit_redirect_url" : http://www.baidu.com
        "config_rewrite_type" : 0
        "config_order_number_prefix" : D
        "config_pixel_google_ads_id" : AW-123456789
        "config_pixel_google_trade_id" : AW-123456789/BtvVCJTBlcsDEIXnx9ID
        "config_pixel_facebook" : 
        "config_pixel_youtube" : 
        "config_pixel_pintrest" : 
        "config_pixel_instgram" : 
        "config_shop_domain_password" : 123456789
        }
     * @return ResponseCore
    """
    def update(self, params):
        request = self.getRequest('/openApi/settings/update')
        result = request.set_body(params).set_method('POST').send_request(True)
        return result

    """
     * Get getSettings
     * @return ResponseCore
    """
    def getSettings(self):
        request = self.getRequest('/openApi/settings/getSettings')
        result = request.set_body(params).set_method('GET').send_request(True)
        return result
