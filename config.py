# window parameters
icon_name = 'car.ico'
size = (1050, 600)
title = 'Car Shop App'

path_img = 'images/'

# toolbar icons 
file_img = 'file.png'
save_img = 'save.png'
home_img = 'home.png'
search_img = 'search.png'
print_img = 'print.png'

ID_BUTTON = 100

# database connection
host = 'localhost'
user ='nadya'
password = 'Myfriend_16'
db = 'cars_db'

# data for start page
cars_index = ['№ ', 'ID', "Коробка передач ", "Пробег ",
              "№РТС ", "Цена ", "Год выпуска ",
              "Объем двигателя ", "Цвет ", "Тип кузова ","Модель "]
cars = {}

orders_index = ['№: ','ID', "Год продажи: ", "Марка: ",
                "Фамилия клиента: ", "Фамилия продавца: ", "Форма оплаты: "]
clients_index = ['№','ID', 'Фамилия', 'Имя', 'Серия, номер паспорта', 'Телефон']


# data for aboutbox
program_name = 'CarSearching'
version = '1.0'
copyright = '(C) 2020 Nadezhda Shatalina'
web_site = 'https://github.com/etoruru'
developer = 'Nadezhda Shatalina'
doc_writer = 'Nadezhda Shatalina'
description = """CarSearching это автоматизированная информационная система,
предназначенная для упрощения работы с базой данных. Возможности включают добавление, изменение, удаление элементов,
расширенные возможности поиска и многое другое."""

