from .Http.RequestCore import RequestCore
from .Http.RequestException import RequestException
from .Core.Result import Result
from .Core.ShopiuuException import ShopiuuException

from .Model.Article import Article
from .Model.ArticleCategory import ArticleCategory
from .Model.Currency import Currency
from .Model.Nav import Nav
from .Model.Payment import Payment
from .Model.Product import Product
from .Model.Seo import Seo
from .Model.Settings import Settings
from .Model.Shipping import Shipping
from .Model.ShippingArea import ShippingArea
from .Model.ShippingCompany import ShippingCompany
from .Model.StoreTheme import StoreTheme
from .Model.EmbedCode import EmbedCode

class ShopiuuClient:
    def __init__(self, accessToken, endpoint):

        if accessToken is None:
            raise ShopiuuException("access token id is empty")
        if endpoint is None:
            raise ShopiuuException("endpoint is empty")

        accessToken = accessToken.strip()
        endpoint = endpoint.strip().strip('/')

        self.accessToken = accessToken
        self.endpoint = endpoint

    def addArticle(self, data):
        articleModel = Article(self.accessToken, self.endpoint)
        try:
            response = articleModel.add(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")

    def updateArticle(self, data):
        articleModel = Article(self.accessToken, self.endpoint)
        try:
            response = articleModel.update(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")

    def getArticles(self, data):
        articleModel = Article(self.accessToken, self.endpoint)
        try:
            response = articleModel.getList(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")

    def getArticleCategories(self):
        articleCategoryModel = ArticleCategory(self.accessToken, self.endpoint)
        try:
            response = articleCategoryModel.getCategories()
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")

    def getArticleCategoryTree(self):
        articleCategoryModel = ArticleCategory(self.accessToken, self.endpoint)
        try:
            response = articleCategoryModel.getCategoryTree()
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")

    def addArticleCategory(self, data):
        articleCategoryModel = ArticleCategory(self.accessToken, self.endpoint)
        try:
            response = articleCategoryModel.add(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")

    def getStoreThemes(self):
        storeThemeModel = StoreTheme(self.accessToken, self.endpoint)
        try:
            response = storeThemeModel.getList()
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def getThemeFiles(self, data):
        storeThemeModel = StoreTheme(self.accessToken, self.endpoint)
        try:
            response = storeThemeModel.getThemeFiles(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")

    def createTheme(self, data):
        storeThemeModel = StoreTheme(self.accessToken, self.endpoint)
        try:
            response = storeThemeModel.createTheme(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def addCurrency(self, data):
        currencyModel = Currency(self.accessToken, self.endpoint)
        try:
            response = currencyModel.add(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def updateCurrency(self, data):
        currencyModel = Currency(self.accessToken, self.endpoint)
        try:
            response = currencyModel.update(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def deleteCurrency(self, data):
        currencyModel = Currency(self.accessToken, self.endpoint)
        try:
            response = currencyModel.delete(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def getCurrencies(self, data):
        currencyModel = Currency(self.accessToken, self.endpoint)
        try:
            response = currencyModel.getList(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def addEmbedCode(self, data):
        embedCodeModel = EmbedCode(self.accessToken, self.endpoint)
        try:
            response = embedCodeModel.add(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def updateEmbedCode(self, data):
        embedCodeModel = EmbedCode(self.accessToken, self.endpoint)
        try:
            response = embedCodeModel.update(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def deleteEmbedCode(self, data):
        embedCodeModel = EmbedCode(self.accessToken, self.endpoint)
        try:
            response = embedCodeModel.delete(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def getEmbedCodes(self, data):
        embedCodeModel = EmbedCode(self.accessToken, self.endpoint)
        try:
            response = embedCodeModel.getList(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def getNavMenu(self):
        navModel = Nav(self.accessToken, self.endpoint)
        try:
            response = navModel.getNavMenu()
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def getAllNavLists(self):
        navModel = Nav(self.accessToken, self.endpoint)
        try:
            response = navModel.getAllNavLists()
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def addNav(self, data):
        navModel = Nav(self.accessToken, self.endpoint)
        try:
            response = navModel.add(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def updateNav(self, data):
        navModel = Nav(self.accessToken, self.endpoint)
        try:
            response = navModel.update(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def addNavMenu(self, data):
        navModel = Nav(self.accessToken, self.endpoint)
        try:
            response = navModel.addMenu(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def updateNavMenu(self, data):
        navModel = Nav(self.accessToken, self.endpoint)
        try:
            response = navModel.updateMenu(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def deleteNav(self, data):
        navModel = Nav(self.accessToken, self.endpoint)
        try:
            response = navModel.deleteNav(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def deleteNavMenu(self, data):
        navModel = Nav(self.accessToken, self.endpoint)
        try:
            response = navModel.deleteMenu(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def getNavMenuLists(self, data):
        navModel = Nav(self.accessToken, self.endpoint)
        try:
            response = navModel.menuLists(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def addPayment(self, data):
        paymentModel = Payment(self.accessToken, self.endpoint)
        try:
            response = paymentModel.add(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def updatePayment(self, data):
        paymentModel = Payment(self.accessToken, self.endpoint)
        try:
            response = paymentModel.update(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def deletePayment(self, data):
        paymentModel = Payment(self.accessToken, self.endpoint)
        try:
            response = paymentModel.delete(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def getPayments(self, data):
        paymentModel = Payment(self.accessToken, self.endpoint)
        try:
            response = paymentModel.getList(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def getAllPayments(self, data):
        paymentModel = Payment(self.accessToken, self.endpoint)
        try:
            response = paymentModel.getAllPayments(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def addProduct(self, data):
        productModel = Product(self.accessToken, self.endpoint)
        try:
            response = productModel.add(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def updateProduct(self, data):
        productModel = Product(self.accessToken, self.endpoint)
        try:
            response = productModel.update(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def deleteProduct(self, data):
        productModel = Product(self.accessToken, self.endpoint)
        try:
            response = productModel.delete(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def getProducts(self, data):
        productModel = Product(self.accessToken, self.endpoint)
        try:
            response = productModel.getList(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def updateSeo(self, data):
        seoModel = Seo(self.accessToken, self.endpoint)
        try:
            response = seoModel.update(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def getSeos(self, data):
        seoModel = Seo(self.accessToken, self.endpoint)
        try:
            response = seoModel.getList(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def updateSettings(self, data):
        settingsModel = Settings(self.accessToken, self.endpoint)
        try:
            response = settingsModel.update(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def getSettings(self):
        settingsModel = Settings(self.accessToken, self.endpoint)
        try:
            response = settingsModel.getSettings()
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def addShipping(self, data):
        shippingModel = Shipping(self.accessToken, self.endpoint)
        try:
            response = shippingModel.add(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def updateShipping(self, data):
        shippingModel = Shipping(self.accessToken, self.endpoint)
        try:
            response = shippingModel.update(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def deleteShipping(self, data):
        shippingModel = Shipping(self.accessToken, self.endpoint)
        try:
            response = shippingModel.delete(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def getShippings(self, data):
        shippingModel = Shipping(self.accessToken, self.endpoint)
        try:
            response = shippingModel.getList(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def getAllShippings(self, data):
        shippingModel = Shipping(self.accessToken, self.endpoint)
        try:
            response = shippingModel.getAllShippings(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def addShippingArea(self, data):
        shippingAreaModel = ShippingArea(self.accessToken, self.endpoint)
        try:
            response = shippingAreaModel.add(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def updateShippingArea(self, data):
        shippingAreaModel = ShippingArea(self.accessToken, self.endpoint)
        try:
            response = shippingAreaModel.update(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def deleteShippingArea(self, data):
        shippingAreaModel = ShippingArea(self.accessToken, self.endpoint)
        try:
            response = shippingAreaModel.delete(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def getShippingAreas(self, data):
        shippingAreaModel = ShippingArea(self.accessToken, self.endpoint)
        try:
            response = shippingAreaModel.getList(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def addShippingCompany(self, data):
        shippingCompanyModel = ShippingCompany(self.accessToken, self.endpoint)
        try:
            response = shippingCompanyModel.add(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def updateShippingCompany(self, data):
        shippingCompanyModel = ShippingCompany(self.accessToken, self.endpoint)
        try:
            response = shippingCompanyModel.update(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def deleteShippingCompany(self, data):
        shippingCompanyModel = ShippingCompany(self.accessToken, self.endpoint)
        try:
            response = shippingCompanyModel.delete(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
    
    def getShippingCompanies(self, data):
        shippingCompanyModel = ShippingCompany(self.accessToken, self.endpoint)
        try:
            response = shippingCompanyModel.getList(data)
            result = Result(response)
            return result
        except RequestException as e:
            raise ShopiuuException(f"Request error: {e}")
        except Exception as e:
            raise ShopiuuException(f"Request error: {e}")
