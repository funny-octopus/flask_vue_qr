import qrcode, os
from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime
# pip install lxml, pillow

def MakeQR(URL:str)->str:
    """Входной параметр - URL, функция возвращает ссылку на QR-код-картинку.
    Название картинки берется с последнего слеша в URL
    https://127.0.0.1/item/1  --->>> QRs\1.png"""
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = f"{URL[URL.rfind('/')+1:]}.png"
    img = qrcode.make(URL)
    dir_to_save = os.path.join(BASE_DIR, 'app', 'static', 'qrs')
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
    dt = datetime.now()
    d = str(dt.day)
    if len(d) == 1:
        d = '0' + d
    m = str(dt.month)
    if len(m) == 1:
        m = '0' + m
    y = str(dt.year)
    url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
    params = {
        'date_req': f'{d}/{m}/{y}'
    }
    request = requests.get(url, params)
    soup = bs(request.content, 'xml')
    find_usd = soup.find(ID='R01235').Value.string
    find_eur = soup.find(ID='R01239').Value.string
    return(find_usd, find_eur)


if __name__ == '__main__':
    print(get_currency())
    # MakeQR('http://127.0.0.1:5000/item/34888')