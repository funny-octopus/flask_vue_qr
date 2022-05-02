import time
from typing import Iterable, List
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


class BaseEl(object):
    """Базовый класс элементов"""

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    @property
    def count(self):
        """Возвращает количество элементов на странице"""
        return len(self.driver.find_elements(*self.locator))

    @property
    def text(self):
        """Возвращает текст элемента"""
        return self.get_element().text

    def get_element(self):
        """Получить элемент"""
        return self.driver.find_element(*self.locator)

    def get_elements(self) -> Iterable:
        """Получить список элементов"""
        return self.driver.find_elements(*self.locator)

    def is_displayed(self) -> bool:
        """Отображается ли элемент"""
        return self.get_element().is_displayed()

    def scroll_into_view(self):
        """Скролл к элемента"""
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_element())


class SpanEl(BaseEl):
    """Элемент <span>"""
    
    pass


class DivEl(BaseEl):
    """Элемент <div>"""
    pass


class TextInputEl(BaseEl):
    """Элемент <input>"""

    def type_in(self, text: str):
        """
        Ввод текста в поле
        :param text: вводимый текст
        """
        el = self.get_element()
        el.send_keys(text)


class ButtonEl(BaseEl):
    """Кнопка"""

    def push(self):
        """Нажать на кнопку"""
        el = self.get_element()
        self.scroll_into_view()
        time.sleep(1)
        el.click()


class LinkEl(BaseEl):
    """Ссылка"""

    def click(self):
        """Клик на ссылку"""
        el = self.get_element()
        el.click()


class ImageEl(BaseEl):
    """Изображение"""
    pass


class SelectEl(BaseEl):
    """<select>"""

    def select(self, option: str = '', index: int = '', text: str = ''):
        """
        Выбор пункта select
        :param option: строка опции
        :param index: позиция в списке
        :param text: текст
        """
        # assert (option and not index) and not text, "Необходимо задать, один параметр"

        el = Select(self.get_element())

        if option:
            el.select_by_value(option)
        elif index:
            el.select_by_index(index)
        else:
            el.select_by_visible_text(text)

    @property
    def options(self):
        return Select(self.get_element()).options
    
    @property
    def options_text_list(self):
        return [x.text for x in self.options]


class TextAreaEl(TextInputEl):
    """<textarea>"""

    pass


class ElList:
    """Список элементов"""

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def item(self, contains_text: str):
        """
        Возвращает элемент по вхождению текста
        :param contains_text: текс, по которому ищем
        """
        els = self.driver.find_elements(*self.locator)
        for el in els:
            if contains_text in el.text:
                return el
        return None


    @property
    def text_list(self) -> List[str]:
        els = self.driver.find_elements(*self.locator)
        return [x.text for x in els]

    @property
    def text_str(self) -> str:
        els = self.driver.find_elements(*self.locator)
        return '; '.join(self.text_list)


class InputFileEl(BaseEl):
    """<input type=file>"""
    pass
