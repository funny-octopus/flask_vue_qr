import time 
from config import Config


conf = Config()


class TestAuthUI:
    """Тестирование функционала"""

    # url = "https://funnyoctopus.xyz/auth/login"
    url = conf.base_url + "auth/login"
    login = conf.login
    password = conf.password

    def test_login(self, driver, auth_page, main_page):
        """Тестирование авторизации"""

        driver.get(self.url)
        assert auth_page.is_load() is True

        auth_page.auth(self.login, self.password)
        assert main_page.is_load() is True

    def test_logout(self, login, driver, auth_page, main_page):
        """Тестирование выхода"""

        main_page.logout()
        assert auth_page.is_load() is True


class TestMainUI:
    """Тестирование отображения главной страницы"""

    def test_category_view(self, login, driver, main_page):
        """Тестирование отображения категории"""

        main_page.go_to_category("Плитка")
        assert main_page.is_load_category() is True

    def test_item_view(self, login, driver, main_page, item_page):
        """Тестирование отображения товара"""

        main_page.go_to_category("Плитка")
        # main_page.go_to_item("Плитка для теста1")
        main_page.go_to_item()
        assert (item_page.is_load_item() is True), ""


class TestFilterUI:
    """Тестирование функционала фильра в категории"""

    def test_search_field(self, login, driver, main_page):
        """Тестирование строки поиска"""

        main_page.go_to_category("Плитка")
        main_page.search_field.type_in("0011")
        assert (main_page.category_item.count == 1), "Должен отобразиться один элемент"

    def test_factory_filter(self, login, driver, main_page):
        """Проверка фильтра по фабрике"""

        main_page.go_to_category("Плитка")
        main_page.select_factory.select(text="Завод плитки для теста")
        assert (main_page.category_item.count == 2), "Должно отобразиться два элемента"
        assert "Плитка для теста1" in main_page.category_items.text_str, "Отобразился не тот элемент"
        assert "Плитка для теста2" in main_page.category_items.text_str, "Отобразился не тот элемент"
        assert len(main_page.select_collection.options) == 3
        assert "Все" in main_page.select_collection.options_text_list
        assert "Коллекция для теста" in main_page.select_collection.options_text_list
        assert "Коллекция для теста2" in main_page.select_collection.options_text_list
        assert len(main_page.select_provider.options) == 2
        assert "Все" in main_page.select_provider.options_text_list
        assert "Поставщик для теста" in main_page.select_provider.options_text_list
        
    def test_collection_filter(self, login, driver, main_page):
        """Проверка фильтра по коллекции"""

        main_page.go_to_category("Плитка")
        main_page.select_collection.select(text="Коллекция для теста")
        assert (main_page.category_item.count == 1), "Должен отобразиться один элемент"
        assert "Плитка для теста1" in main_page.category_item.text, "Отобразился не тот элемент"
        assert len(main_page.select_factory.options) == 2
        assert "Все" in main_page.select_factory.options_text_list
        assert "Завод плитки для теста" in main_page.select_factory.options_text_list
        assert len(main_page.select_provider.options) == 2
        assert "Все" in main_page.select_provider.options_text_list
        assert "Поставщик для теста" in main_page.select_provider.options_text_list

    def test_provider_filter(self, login, driver, main_page):
        """Проверка фильтра по поставщику"""

        main_page.go_to_category("Плитка")
        main_page.select_provider.select(text="Поставщик для теста")
        assert (main_page.category_item.count == 2), "Должно отобразиться два элемента"
        assert "Плитка для теста1" in main_page.category_items.text_str, "Отобразился не тот элемент"
        assert "Плитка для теста2" in main_page.category_items.text_str, "Отобразился не тот элемент"
        assert len(main_page.select_collection.options) == 3
        assert "Все" in main_page.select_collection.options_text_list
        assert "Коллекция для теста" in main_page.select_collection.options_text_list
        assert "Коллекция для теста2" in main_page.select_collection.options_text_list
        assert len(main_page.select_factory.options) == 2
        assert "Все" in main_page.select_factory.options_text_list
        assert "Завод плитки для теста" in main_page.select_factory.options_text_list

    def test_two_filters(self, login, driver, main_page):
        """Проверка нескольких фильтров"""

        main_page.go_to_category("Плитка")
        main_page.select_provider.select(text="Поставщик для теста")
        main_page.select_collection.select(text="Коллекция для теста")
        assert (main_page.category_item.count == 1), "Должен отобразиться один элемент"
        assert "Плитка для теста1" in main_page.category_items.text_str, "Отобразился не тот элемент"
        assert len(main_page.select_factory.options) == 2
        assert "Все" in main_page.select_factory.options_text_list
        assert "Завод плитки для теста" in main_page.select_factory.options_text_list
        assert len(main_page.select_collection.options) == 3
        assert "Все" in main_page.select_collection.options_text_list
        assert "Коллекция для теста" in main_page.select_collection.options_text_list
        assert "Коллекция для теста2" in main_page.select_collection.options_text_list


class TestItem:
    """Проверка товара"""

    def test_item_create(self, login, driver, main_page, item_page, add_item_page):
        """Проверка создания товара"""
         
        main_page.go_to_page("Добавить товар")
        add_item_page.name.type_in("test NAME")
        add_item_page.category.select(index=1)
        add_item_page.factory.type_in("test FACTORY")
        add_item_page.provider.type_in("test PROVIDER")
        add_item_page.country.select(index=2)
        add_item_page.collection.type_in("test COLLECTION")
        add_item_page.size.type_in("test SIZE")
        add_item_page.price.type_in("9999")
        add_item_page.currency.select(index=2)
        add_item_page.course.select(index=2)
        add_item_page.pricev.select(index=1)
        add_item_page.percent.type_in("99")
        add_item_page.count.type_in("99")
        add_item_page.notes.type_in("99")
        add_item_page.save.push()
        add_item_page.go_to_page("Каталог")
        main_page.go_to_category("Плитка")
        main_page.search_field.type_in("test NAME")
        assert (main_page.category_item.count == 1), "Должен отобразиться один элемент"
        main_page.go_to_item("test NAME")
        item_page.delete.push()
        item_page.alert.accept()
        time.sleep(1)
        assert main_page.is_load() is True

