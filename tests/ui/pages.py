from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from locators import AuthLocators
from elements import (TextInputEl, ButtonEl, DivEl, LinkEl, SpanEl, ImageEl,
        SelectEl, TextAreaEl, ElList, InputFileEl)
from locators import AuthLocators, MainLocators, ItemLocators, BaseLocators, AddItemLocators


class AuthPage:
    """Страница авторизации"""

    def __init__(self, driver):
        self.login = TextInputEl(driver, AuthLocators.LOGIN)
        self.password = TextInputEl(driver, AuthLocators.PASSWORD)
        self.submit = ButtonEl(driver, AuthLocators.SUBMIT)

    def is_load(self):
        """Проверка загрузки страницы"""

        return (self.login.is_displayed() and self.password.is_displayed() and self.submit.is_displayed())


    def auth(self, login, password):
        """
        Аутентифицироваться
        :param login: Логин
        :param password: Пароль
        """

        self.login.type_in(login)
        self.password.type_in(password)
        self.submit.push()


class BasePage:
    """Базовая страница"""

    def __init__(self, driver):
        self.driver = driver
        self.logout_btn = ButtonEl(driver, BaseLocators.LOGOUT)
        self.sidebar = DivEl(driver, BaseLocators.SIDEBAR)
        self.menu = ElList(self.driver, BaseLocators.MENU_ITEMS)
        self.alert = Alert(driver)

    def logout(self):
        self.logout_btn.push()

    def is_base_load(self):
        return (self.logout_btn.is_displayed() and self.sidebar.is_displayed())
    
    def go_to_page(self, menu_item: str):
        """Переход на страницу через меню"""
        item = self.menu.item(contains_text=menu_item)
        item.click()


class MainPage(BasePage):
    """Главная страница"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.category_tile = LinkEl(self.driver, MainLocators.CATEGORY_TILE)

        self.search_field = TextInputEl(self.driver, MainLocators.SEARCH_FIELD)
        self.back_arrow = LinkEl(self.driver, MainLocators.BACK_ARROW)
        self.span_factory = SpanEl(self.driver, MainLocators.SPAN_FACTORY)
        self.span_collection = SpanEl(self.driver, MainLocators.SPAN_COLLECTION)
        self.span_provider = SpanEl(self.driver, MainLocators.SPAN_PROVIDER)
        self.select_factory = SelectEl(self.driver, MainLocators.SELECT_FACTORY)
        self.select_collection = SelectEl(self.driver, MainLocators.SELECT_COLLECTION)
        self.select_provider = SelectEl(self.driver, MainLocators.SELECT_PROVIDER)
        self.category_item = LinkEl(self.driver, MainLocators.CATEGORY_ITEM)
        self.category_items = ElList(self.driver, MainLocators.CATEGORY_ITEM)

    def is_load(self):
        """Проверка загрузки страницы"""

        return self.is_base_load() and self.category_tile.is_displayed()

    def is_load_category(self):
        """Проверка загрузки категории"""

        return self.is_base_load()\
                and self.search_field.is_displayed()\
                and self.back_arrow.is_displayed()\
                and self.span_factory.is_displayed()\
                and self.span_collection.is_displayed()\
                and self.span_provider.is_displayed()\
                and self.select_factory.is_displayed()\
                and self.select_collection.is_displayed()\
                and self.select_provider.is_displayed()\
                and self.category_item.is_displayed()

    def go_to_category(self, category: str):
        """
        Переход в категорию по названию
        :param category: название категории
        """

        el = self.driver.find_element(By.XPATH, f"//div[contains(text(), '{category}')]")
        el.click()

    def go_to_item(self, item: str = None):
        """
        Переход в категорию по названию
        :param item: название товара
        """

        el = self.driver.find_element(By.XPATH, f"//div[contains(text(), '{item}')]") if item else self.category_item
        el.click()



class ItemPage(BasePage):
    """Страница товара"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image = ImageEl(self.driver, ItemLocators.IMAGE)
        self.category = SelectEl(self.driver, ItemLocators.CATEGORY_PROP)
        self.article = TextInputEl(self.driver, ItemLocators.ARTICLE_PROP)
        self.factory = TextInputEl(self.driver, ItemLocators.FACTORY_PROP)
        self.provider = TextInputEl(self.driver, ItemLocators.PROVIDER_PROP)
        self.country = SelectEl(self.driver, ItemLocators.COUNTRY_PROP)
        self.collection = TextInputEl(self.driver, ItemLocators.COLLECTION_PROP)
        self.size = TextInputEl(self.driver, ItemLocators.SIZE_PROP)
        self.name = TextInputEl(self.driver, ItemLocators.NAME_PROP)
        self.price = TextInputEl(self.driver, ItemLocators.PRICE_PROP)
        self.currency = SelectEl(self.driver, ItemLocators.CURRENCY_PROP)
        self.course = SelectEl(self.driver, ItemLocators.COURSE_PROP)
        self.pricev = SelectEl(self.driver, ItemLocators.PRICEV_PROP)
        self.percent = SelectEl(self.driver, ItemLocators.PERCENT_PROP)
        self.count = TextInputEl(self.driver, ItemLocators.COUNT_PROP)
        self.notes = TextAreaEl(self.driver, ItemLocators.NOTES_PROP)
        self.qr = ButtonEl(self.driver, ItemLocators.QR)
        self.save = ButtonEl(self.driver, ItemLocators.SAVE)
        self.delete = ButtonEl(self.driver, ItemLocators.DELETE)

    def is_load_item(self):
        """Проверка загрузки товара"""

        return self.is_base_load() and self.image.is_displayed()\
                and self.category.is_displayed()\
                and self.article.is_displayed()\
                and self.factory.is_displayed()\
                and self.provider.is_displayed()\
                and self.country.is_displayed()\
                and self.collection.is_displayed()\
                and self.size.is_displayed()\
                and self.name.is_displayed()\
                and self.price.is_displayed()\
                and self.currency.is_displayed()\
                and self.course.is_displayed()\
                and self.pricev.is_displayed()\
                and self.percent.is_displayed()\
                and self.count.is_displayed()\
                and self.notes.is_displayed()\


class AddItemPage(BasePage):
    """Страница создания товара"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = TextInputEl(self.driver, AddItemLocators.NAME)
        self.category = SelectEl(self.driver, AddItemLocators.CATEGORY)
        self.image = InputFileEl(self.driver, AddItemLocators.IMAGE)
        self.factory = TextInputEl(self.driver, AddItemLocators.FACTORY)
        self.provider = TextInputEl(self.driver, AddItemLocators.PROVIDER)
        self.country = SelectEl(self.driver, AddItemLocators.COUNTRY)
        self.collection = TextInputEl(self.driver, AddItemLocators.COLLECTION)
        self.size = TextInputEl(self.driver, AddItemLocators.SIZE)
        self.price = TextInputEl(self.driver, AddItemLocators.PRICE)
        self.currency = SelectEl(self.driver, AddItemLocators.CURRENCY)
        self.course = SelectEl(self.driver, AddItemLocators.COURSE)
        self.pricev = SelectEl(self.driver, AddItemLocators.PRICEV)
        self.percent = TextInputEl(self.driver, AddItemLocators.PERCENT)
        self.count = TextInputEl(self.driver, AddItemLocators.COUNT)
        self.notes = TextAreaEl(self.driver, AddItemLocators.NOTES)
        self.save = ButtonEl(self.driver, AddItemLocators.SAVE)

    
