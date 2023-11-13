import os
import pathlib
from pathlib import Path
from zipfile import ZipFile



filepath = Path(os.getcwd(), "foto")# объединяет имя корневой папки и вот тово что в конце

def zip_arhive(zip_name):# функция разорхивации
    with ZipFile(zip_name, "r") as my_zip:
        path_zip = Path(zip_name)
        for item in my_zip.infolist():
            if(item.is_dir()):# проверяет является ли фаил в архиве папкой
                my_zip.extractall()#разархивирует в текушую папку
                break
            else:
                my_zip.extractall(path=path_zip.stem)#разархивирует в указаную папку
                break

def folder_in_file(name): # функция пробегается по папкам и файлам если папка то можно вызвать рекрсию если фаил то переходим к архивации
    for file_or_folder in name: #цыкл во вложенной папке
        if Path(file_or_folder).is_dir():
            root_folder_in = os.getcwd()# адрес текущего вложенного подкоталога
            folder_name_in = os.path.join(os.getcwd(), file_or_folder)#обединение адреса для входа
            os.chdir(folder_name_in)#меняем на директорию во вложенном подкаталоге
            file_in_folder_in = os.listdir()  # список папок или файлов в текущей поддиректории
            if pathlib.PurePath(file_or_folder).suffix == ".zip":
                zip_arhive(file_or_folder)

            #здесь проверка на зип и джпег

            os.chdir(root_folder_in)  # смена на корневую директорию

            print(root_folder_in)
        elif Path(file_or_folder).is_file():
            if pathlib.PurePath(file_or_folder).suffix == ".zip":
                zip_arhive(file_or_folder)

# с именем паки Временно позже удалить и строку ниже
os.chdir(filepath)  # смена текущей директории

folder_in_path = os.listdir()  # возвращает список папок в корневой директории

root_folder = os.getcwd() # корневой каталог

for folder in folder_in_path:# цыкл проходится по директории в которой запущен скрипт
    folder_name = os.path.join(os.getcwd(), folder)# адрес текущего подкаталога
    os.chdir(folder_name) # смена директории с текущей на ту что сейчас в цикле
    file_in_folder = os.listdir()# список папок или файлов в текущей директории
    folder_in_file(file_in_folder)

    os.chdir(root_folder)# смена на корневую директорию

