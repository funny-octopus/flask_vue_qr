import qrcode, os

def MakeQR(URL):
#def MakeQR(str:URL)->str:
    """Входной параметр - URL, функция возвращает ссылку на QR-код-картинку.
    Название картинки берется с последнего слеша в URL
    127.0.0.1/item/1  --->>> QRs\1.png"""
    # входной параметр id
    # url лучше находит так:
    # basedir = os.path.abspath(os.path.dirname(__file__))
    # dir_ro_save = os.path.join(basedir, 'app', 'static', 'qrs') <- надо перепроверить, вроде так можно
    # проверять наверное не надо, каталог создадим сразу, он там и будет навсегда
    filename = f"{URL[URL.rfind('/')+1:]}.png"
    img = qrcode.make(URL)
    dir_to_save = 'QRs\\'
    if not os.path.exists(dir_to_save):
        os.mkdir(dir_to_save)
    file_to_save = dir_to_save + filename
    # строку сверху лучше написать так:
    # file_to_save = os.path.join(dir_to_save, filename)
    img.save(file_to_save)
    return(file_to_save)

