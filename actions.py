import db


def get_cars_data():
    """ creates a dict, which includes cars from the base, to display it on the Car's tab """
    cars = db.get_all_cars()
    cars_list = []
    for car in cars:
        cars_list.append(display_car(car))
    cars_dict = {i: cars_list[i] for i in range(len(cars_list))}
    return cars_dict



def between_markers(text, begin, end):
    """ returns text, which is between given markers, begin - marker of begining, end - marker of ending"""
    if begin in text:
        begin_index = text.find(begin) + len(begin)
    else:
        begin_index = 0

    if end in text:
        end_index = text.find(end)
    else:
        end_index = len(text)
    return text[begin_index: end_index]


def display_car(car_data):
    """ returns normal data of each car, car_data - one line of one car from database"""
    modified_data = between_markers(str(car_data), '(', ')')
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


def get_orders_data():
    """ creates a dict, which includes cars from the base, to display it on the Car's tab """
    orders = db.get_all_orders()
    orders_list = []
    for order in orders:
        orders_list.append(modify_orders_data(order))
    orders_dict = {i: orders_list[i] for i in range(len(orders_list))}
    return orders_dict


def modify_orders_data(order_data):
    """ returns normal view orders, order_data - line of each order from the base """
    modified_data = between_markers(str(order_data), '(', ')')
    values = str(modified_data).split(',')
    idCar, idClient, idCustomer, idform_payment = values[-4:]
    idModel = db.get_model_from_tCars(idCar)
    models_name = db.get_model_name(int(idModel))
    client_firstName = db.get_client_firstname(int(idClient))
    customer_firstName = db.get_customer_firstname(int(idCustomer))
    payment_name = db.get_payment_name(int(idform_payment))

    values = values[:-4] + [models_name, client_firstName, customer_firstName, payment_name]
    return values


def add_car_tobase(transmition, mileage, PTC, price,
                   year_issue, engine_capacity, color,
                   body_type, model):
    idColor = db.get_idcolor(color)
    idBody_type = db.get_idBody_type(body_type)
    idModel = db.get_idModel(model)
    db.add_car([transmition, mileage, PTC, price,
                   year_issue, engine_capacity, idColor,
                   idBody_type, idModel])
    


def modify_clients_data(client_data):
    """ returns normal view clients, client_data - line of each client from the base """
    modified_data = between_markers(str(client_data), '(', ')')
    values = str(modified_data).split(',')
    return values


def get_clients_data():
    clients = db.get_all_clients()
    clients_list = []
    for client in clients:
        clients_list.append(modify_clients_data(client))
    clients_dict = { i: clients_list[i] for i in range(len(clients_list))}
    return clients_dict

def convert_tuple_tolist(data):
    """ returns list, takes tuple of tuples and converts it to list """
    ls = []
    for i in data:
        ls += list(i)
    return ls
   





if __name__ == '__main__':
    print(db.get_all_clients())
