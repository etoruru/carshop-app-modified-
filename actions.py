import db


def get_cars_data():
    cars = db.get_all_cars()
    cars_list = []
    index_cars_list = []
    for i in cars:
        index_cars_list.append(display_car(i)[0])
        cars_list.append(display_car(i)[1:])
    cars_dict = {i: cars_list[i] for i in range(len(cars_list))}
    return cars_dict





def between_markers(text, begin, end):
    """ returns text, which is between given markersmbegin - marker of begining, end - marker of ending"""
    if begin in text:
        begin_index = text.find(begin) + len(begin)
    else:
        begin_index = 0

    if end in text:
        end_index = text.find(end)
    else:
        end_index = len(text)
    return text[begin_index: end_index]


key = ['№ ', "Коробка передач ", "Пробег ",
           "№РТС ", "Цена ", "Год выпуска ",
           "Объем двигателя ", "Цвет ", "Тип кузова ",
           "Модель "]

def display_car(car_data):
    """ returns normal data of each car, car_data - one line of one car from database"""
    modified_data = between_markers(str(car_data), '(',')')
    values = str(modified_data).split(',')
    idColor, idBody_type, idModel = values[-3:]
    color_name = db.get_colorname(int(idColor))
    body_type = db.get_body_type(int(idBody_type))
    model_name = db.get_model_name(int(idModel))
    values = values[:-3] + [color_name, body_type, model_name]
    return  values


def create_clauses(idModel, idBody_type, transmition,
                   idColor, mileage, engineCapacity,
                   year, price):
    set_clauses = []
    car_dict = create_dict(idModel, idBody_type, transmition,
                           idColor, mileage, engineCapacity,
                           year, price)
    for key in car_dict.keys():
        if not(car_dict.get(key) == None or car_dict.get(key) == ''):
            set_clauses.append(key + "=" + "'" + car_dict.get(key) + "'")
    return ', '.join(set_clauses)


def modify_str(order_data):
    modified_data = between_markers(str(order_data), '(',')')
    values = str(modified_data).split(',')
    idCar, idClient, idCustomer, idform_payment = values[-4:]
    idModel = db.get_model_from_tCars(idCar)
    models_name = db.get_model_name(int(idModel))
    client_firstName = db.get_client_firstname(int(idClient))
    customer_firstName = db.get_customer_firstname(int(idCustomer))
    payment_name = db.get_payment_name(int(idform_payment))

    values = values[:-4] + [models_name, client_firstName, customer_firstName, payment_name] + ['\n']
    key = ['№: ', "Год продажи: ", "Марка: ",
           "Фамилия клиента: ", "Фамилия продавца: ", "Форма оплаты: "]
    return transform_str_to_friendly_form(key, values)


if __name__ == '__main__':
    print(get_cars_data()[0])
