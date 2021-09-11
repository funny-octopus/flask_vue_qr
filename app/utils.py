import qrcode, os
from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime
# pip install lxml, pillow
import xlsxwriter
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOMEN = 'http://127.0.0.1:5000'


def save_images(abspath:str) -> None:
    """Принимает путь до файла, и сохраняет его в двух размерах,
    добавляя префикс в названии"""
    dirname, filename = os.path.split(abspath)
    filename_sm = 'sm_' + filename
    filename_big = 'big_' + filename
    img = Image.open(abspath)
    img.thumbnail(size=(300, 256))
    img.save(os.path.join(dirname, filename_big))
    img.thumbnail(size=(64, 64))
    img.save(os.path.join(dirname, filename_sm))


def MakeQR(URL:str)->str:
    """Входной параметр - URL, функция возвращает ссылку на QR-код-картинку.
    Название картинки берется с последнего слеша в URL
    https://127.0.0.1/item/1  --->>> QRs\1.png"""

    filename = f"{URL[URL.rfind('/')+1:]}.png"
    img = qrcode.make(URL)
    dir_to_save = os.path.join(BASE_DIR, 'static', 'qrs')
    if not os.path.exists(dir_to_save):
        os.mkdir(dir_to_save)
    file_to_save = os.path.join(dir_to_save, filename)
    img.save(file_to_save)
    return(file_to_save)


def get_currency()->tuple:
    '''
    Возвращает кортеж из двух элементов
    первый: курс доллара на сегодняшний день от ЦБ РФ
    второй: курс евро --//--
    '''
    url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
    request = requests.get(url)
    soup = bs(request.content, 'xml')
    find_usd = soup.find(ID='R01235').Value.string
    find_eur = soup.find(ID='R01239').Value.string
    return(find_usd, find_eur)


def create_xls(array:list)->str:
    '''
    Принимает список кортежей [(1, 'Плитка белая'), (2, 'Стекловата колючая'), (3, 'Бетонная смесь')]
    Возвращает адрес файла QRs.xls
    '''
    path_xls = os.path.join(BASE_DIR, 'static', 'qrs', 'QRs.xlsx')
    workbook = xlsxwriter.Workbook(path_xls)
    worksheet = workbook.add_worksheet()

    worksheet.set_column('A:A', 30)
    offset = 1
    for i in array:
        worksheet.write('A'+str(offset), i[1])
        path_QR = MakeQR(DOMEN + '/item/' + str(i[0]))
        worksheet.insert_image('B'+str(offset), path_QR, {'x_scale': 0.7, 'y_scale': 0.7})
        offset += 14

    workbook.close()
    return(path_xls)


if __name__ == '__main__':
    # print(get_currency())
    print(create_xls([(1, 'Плитка белая'), (2, 'Стекловата колючая'), (3, 'Бетонная смесь')]))
    # MakeQR('http://127.0.0.1:5000/item/7777')
