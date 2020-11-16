import pymysql.cursors
import config


connection = pymysql.connect(host=config.host,
                             user=config.user,
                             password=config.password,
                             db=config.db)
                             #cursorclass=pymysql.cursors.DictCursor)
                        


mycursor = connection.cursor() 


def execute(*args, **kwargs):
    return mycursor.execute(*args, **kwargs)


def commit(*args, **kwargs):
    return connection.commit(*args, **kwargs)


def get_first_id():
    row = mycursor.fetchone()
    if row:
        return str(row[0])


def get_all_cars():
    sql_command = 'SELECT * FROM Cars'
    mycursor.execute(sql_command)
    return mycursor.fetchall()


def get_idcolor(color_name):
    mycursor.execute("SELECT idColor FROM Color WHERE ColorName='%s'" % (color_name))
    return get_first_id()


def get_idModel(model_name):
    mycursor.execute("SELECT idModels FROM Models WHERE ModelName='%s'" % (model_name))
    return get_first_id()


def get_idBody_type(type_name):
    mycursor.execute("SELECT idBody_type FROM Body_type WHERE TypeName='%s'" % (type_name))
    return get_first_id()


def get_idClients(passport_data):
    mycursor.execute("SELECT idClients FROM Clients WHERE passport_data='%s'" % (passport_data))
    return get_first_id()


def get_idform_payment(payment_name):
    mycursor.execute("SELECT idForm_of_payment FROM Form_of_payment WHERE PaymentName='%s'" % (payment_name))
    return get_first_id()


def get_colorname(id_color):
    mycursor.execute("SELECT ColorName FROM Color WHERE idColor=%d" % (id_color))
    return get_first_id()


def get_body_type(id_body_type):
    mycursor.execute("SELECT TypeName FROM Body_type WHERE idBody_type=%d" % (id_body_type))
    return get_first_id()


def get_model_name(id_model):
    mycursor.execute("SELECT ModelName FROM Models WHERE idModels=%d" % (id_model))
    return get_first_id()


def get_payment_name(id_form_payment):
    mycursor.execute("SELECT PaymentName FROM Form_of_payment WHERE idForm_of_payment=%d" % (id_form_payment))
    return get_first_id()


def get_client_firstname(id_client):
    mycursor.execute("SELECT Firstname FROM Clients WHERE idClients=%d" % (id_client))
    return get_first_id()


def get_customer_firstname(id_customer):
    mycursor.execute("SELECT Firstname FROM Customers WHERE idCustomers=%d" % (id_customer))
    return get_first_id()


def check_availability(car_data):
    sql_command = 'SELECT idOrders FROM Orders WHERE Cars_idCars=%s' % car_data[0]
    mycursor.execute(sql_command)
    return get_first_id()


def get_idcar(id_car):
    mycursor.execute('SELECT idOrders FROM Orders WHERE Cars_idCars="%s"' % (id_car))
    return get_first_id()


def get_all_orders():
    sql_command = 'SELECT * FROM Orders'
    mycursor.execute(sql_command)
    return mycursor.fetchall()


def search_color_in_db(color):
    if not(color == ''):
        return get_idcolor(color)
    else:
        return ''


def search_model_in_db(model):
    if not(model == ''):
        return get_idModel(model)
    else:
        return ''


def search_body_type_in_db(body_type):
    if not(body_type == ''):
        return get_idBody_type(body_type)
    else:
        return ''


def look_for_cars(values):
    sql_command = "SELECT * FROM Cars WHERE "
    mycursor.execute(sql_command + values)
    return mycursor.fetchall()


def delete_car(id_car):
    sql_command = 'DELETE FROM Cars WHERE idCars=%s' % (id_car)
    mycursor.execute(sql_command)
    connection.commit()


def change_cardata(clauses, id_car):
    sql_command = 'UPDATE Cars SET %s WHERE idCars=%s'
    mycursor.execute(sql_command % (clauses, int(id_car)))
    connection.commit()


def get_model_from_tCars(id_car):
    mycursor.execute("SELECT Model_idModel FROM Cars WHERE idCars='%s'" % (id_car))
    return get_first_id()


def add_car(car_values):
    sql_command = 'INSERT INTO Cars(Transmition, Mileage, PTC, Price,\
                                    Year_of_issue, Engine_capacity, Color_idColor,\
                                    Body_type_idBody_type, Model_idModel) \
                                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s\
                                    )'
    mycursor.execute(sql_command,car_values)
    connection.commit()


def add_client(passport_data, customer_firstName, customer_lastName, phone):
    sql_command = "INSERT INTO Clients(Firstname, Lastname, Passport_data, Phone_num) VALUES(%s, %s, %s, %s)"
    client_values = (customer_firstName, customer_lastName, passport_data, phone)
    mycursor.execute(sql_command, client_values)
    connection.commit()


def make_order(order_data):
    sql_command = "INSERT INTO Orders(Data_of_sale, Cars_idCars, \
                                      Clients_idClients, Customers_idCustomers, \
                                      Form_of_payment_idForm_of_payment) VALUES(%s, %s, %s, %s, %s)"
    mycursor.execute(sql_command, order_data)
    connection.commit()