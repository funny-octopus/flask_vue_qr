from selenium.webdriver.common.by import By


class AuthLocators(object):
    """Локаторы страницы авторизации"""

    LOGIN = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    SUBMIT = (By.NAME, "submit")


class BaseLocators(object):
    """Локаторы базовой страницы"""

    LOGOUT = (By.CSS_SELECTOR, ".bi-door-open")
    SIDEBAR = (By.ID, "sidebarMenu")
    MENU_ITEMS = (By.CSS_SELECTOR, "#sidebarMenu a")


class MainLocators(BaseLocators):
    """Локаторы главной страницы"""

    CATEGORY_TILE = (By.CSS_SELECTOR, "[data-qa='Плитка']")
    SEARCH_FIELD = (By.CSS_SELECTOR, "input[type='text']")
    BACK_ARROW = (By.CSS_SELECTOR, "[data-qa='back-arrow']")
    SPAN_FACTORY = (By.CSS_SELECTOR, "[data-qa='span_factory']")
    SPAN_COLLECTION = (By.CSS_SELECTOR, "[data-qa='span_collection']")
    SPAN_PROVIDER = (By.CSS_SELECTOR, "[data-qa='span_provider']")
    SELECT_FACTORY = (By.CSS_SELECTOR, "[data-qa='select_factory']")
    SELECT_COLLECTION = (By.CSS_SELECTOR, "[data-qa='select_collection']")
    SELECT_PROVIDER = (By.CSS_SELECTOR, "[data-qa='select_provider']")
    CATEGORY_ITEM = (By.CSS_SELECTOR, "[data-qa='category_item']")


class ItemLocators(BaseLocators):
    """Локаторы на странице товара"""

    IMAGE = (By.CSS_SELECTOR, "img[alt='Изображение товара']")
    QR = (By.XPATH, "//a[contains(text()), 'QR-код']")
    DELETE = (By.XPATH, "//button[contains(text(), 'Удалить')]")
    SAVE = (By.XPATH, "//button[contains(text()), 'Сохранить']")
    LIST_ROW = (By.TAG_NAME, "li")
    LIST_PROPS = (By.CSS_SELECTOR, "[data-qa='props']")
    CATEGORY_PROP = (By.CSS_SELECTOR, "[data-qa='category']")
    ARTICLE_PROP = (By.CSS_SELECTOR, "[data-qa='article']")
    FACTORY_PROP = (By.CSS_SELECTOR, "[data-qa='factory']")
    PROVIDER_PROP = (By.CSS_SELECTOR, "[data-qa='provider']")
    COUNTRY_PROP = (By.CSS_SELECTOR, "[data-qa='country']")
    COLLECTION_PROP = (By.CSS_SELECTOR, "[data-qa='collection']")
    SIZE_PROP = (By.CSS_SELECTOR, "[data-qa='size']")
    NAME_PROP = (By.CSS_SELECTOR, "[data-qa='name']")
    PRICE_PROP = (By.CSS_SELECTOR, "[data-qa='price']")
    CURRENCY_PROP = (By.CSS_SELECTOR, "[data-qa='currency']")
    COURSE_PROP = (By.CSS_SELECTOR, "[data-qa='course']")
    PRICEV_PROP = (By.CSS_SELECTOR, "[data-qa='price_v']")
    PERCENT_PROP = (By.CSS_SELECTOR, "[data-qa='percent']")
    COUNT_PROP = (By.CSS_SELECTOR, "[data-qa='count']")
    NOTES_PROP = (By.CSS_SELECTOR, "[data-qa='notes']")


class AddItemLocators(BaseLocators):
    """Локаторы на странице добавления товара"""

    NAME = (By.ID, "name")
    CATEGORY = (By.ID, "category")
    IMAGE = (By.ID, "image_url")
    FACTORY = (By.ID, "factory")
    PROVIDER = (By.ID, "provider")
    COUNTRY = (By.ID, "country")
    COLLECTION = (By.ID, "collection")
    SIZE = (By.ID, "size")
    PRICE = (By.ID, "price")
    CURRENCY = (By.ID, "currency")
    COURSE = (By.ID, "course")
    PRICEV = (By.ID, "price_v")
    PERCENT = (By.ID, "percent")
    COUNT = (By.ID, "count")
    NOTES = (By.ID, "notes")
    SAVE = (By.ID, "submit")
