import qrcode, os

def MakeQR(URL):
    """Входной параметр - URL, функция возвращает ссылку на QR-код-картинку.
    Название картинки берется с последнего слеша в URL
    127.0.0.1/item/1  --->>> QRs\1.png"""
    filename = f"{URL[URL.rfind('/')+1:]}.png"
    img = qrcode.make(URL)
    dir_to_save = 'QRs\\'
    if not os.path.exists(dir_to_save):
        os.mkdir(dir_to_save)
    file_to_save = dir_to_save + filename
    img.save(file_to_save)
    return(file_to_save)