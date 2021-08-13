import pymysql.cursors
import config


connection = pymysql.connect(host=config.host,
                             user=config.user,
                             password=config.password,
                             db=config.db)
                             #cursorclass=pymysql.cursors.DictCursor)
                        


mycursor = connection.cursor() 


def execute(*args, **kwargs):
    """ override func 'execute' from module pymysql
        as arguement takes sting with sql-request """
    return mycursor.execute(*args, **kwargs)


def commit(*args, **kwargs):
    """ override func 'commit' from module pymysql """
    return connection.commit(*args, **kwargs)


def get_first_id():
    """ gets id of elem from table, returns id: str """
    row = mycursor.fetchone()
    if row:
        return str(row[0])


def get_all_cars():
    """ gets all elemets from table Cars, returns list of tuples """
    sql_command = 'SELECT * FROM Cars'
    mycursor.execute(sql_command)
    return mycursor.fetchall()


def get_idcolor(color_name):
    """ gets idcolor by its name,color_name: str,
        returns idcolor: str  """
    mycursor.execute("SELECT idColor FROM Color WHERE ColorName='%s'" % (color_name))
    return get_first_id()


def get_idModel(model_name):
    """ gets idmodel by its name, model_name: str
        returns id: str  """
    mycursor.execute("SELECT idModels FROM Models WHERE ModelName='%s'" % (model_name))
    return get_first_id()


def get_idBody_type(type_name):
    """ gets idbody_type by its name, type_name: str,
        returns id: str  """
    mycursor.execute("SELECT idBody_type FROM Body_type WHERE TypeName='%s'" % (type_name))
    return get_first_id()


def get_idClients(passport_data):
    """ gets idclients by its name, passpoert_data: str,
        returns id: str  """
    mycursor.execute("SELECT idClients FROM Clients WHERE passport_data='%s'" % (passport_data))
    return get_first_id()


def get_idform_payment(payment_name):
    """ gets idform_payment by its name, payment_name: str,
        returns id: str  """
    mycursor.execute("SELECT idForm_of_payment FROM Form_of_payment WHERE PaymentName='%s'" % (payment_name))
    return get_first_id()


def get_colorname(id_color):
    """ get color by its id, id_color: int,
        returns name: str """
    mycursor.execute("SELECT ColorName FROM Color WHERE idColor=%d" % (id_color))
    return get_first_id()


def get_body_type(id_body_type):
    """ get body type by its id, id_body_type: int,
        returns name: str """
    mycursor.execute("SELECT TypeName FROM Body_type WHERE idBody_type=%d" % (id_body_type))
    return get_first_id()


def get_model_name(id_model):
    """ get model name by its id, id_model: int,
        returns name: str """
    mycursor.execute("SELECT ModelName FROM Models WHERE idModels=%d" % (id_model))
    return get_first_id()


def get_payment_name(id_form_payment):
    """ get payment name by its id, id_form_payment: int,
        returns name: str """
    mycursor.execute("SELECT PaymentName FROM Form_of_payment WHERE idForm_of_payment=%d" % (id_form_payment))
    return get_first_id()


def get_client_firstname(id_client):
    """ get client first name by its id, id_client: int,
        returns name: str """
    mycursor.execute("SELECT Firstname FROM Clients WHERE idClients=%d" % (id_client))
    return get_first_id()


def get_customer_firstname(id_customer):
    """ get customer first by its id, id_customer: int,
        returns name: str """
    mycursor.execute("SELECT Firstname FROM Customers WHERE idCustomers=%d" % (id_customer))
    return get_first_id()


def check_availability(car_data):
    """ gets id of orders from table 'Orders' which has such a car's id,
        takes as arguement car_data: str, returns id: str """
    sql_command = 'SELECT idOrders FROM Orders WHERE Cars_idCars=%s' % car_data[0]
    mycursor.execute(sql_command)
    return get_first_id()


def get_idcar(id_car):
    """ gets order's id  from table 'Orders' by car's id, id_car: int,
        returns id: str """
    mycursor.execute('SELECT idOrders FROM Orders WHERE Cars_idCars="%s"' % (id_car))
    return get_first_id()


def get_all_orders():
    """ returns  all orders from the table: list of tuple """
    sql_command = 'SELECT * FROM Orders'
    mycursor.execute(sql_command)
    return mycursor.fetchall()


def get_all_clients():
    """ returns  all clients from the table: list of tuple """
    sql_command = 'SELECT * FROM Clients'
    mycursor.execute(sql_command)
    return mycursor.fetchall()

def get_all_colors():
    """ returns all colors from the table  'Color' """
    sql_command = "SELECT ColorName FROM Color"
    mycursor.execute(sql_command)
    return mycursor.fetchall()

def get_all_models():
    """ returns all models from the table 'Model' """
    sql_command = "SELECT ModelName FROM Models"
    mycursor.execute(sql_command)
    return mycursor.fetchall()

def get_all_bodytype():
    """ returns all body type from the table 'Body type' """
    sql_command = "SELECT TypeName FROM Body_type"
    mycursor.execute(sql_command)
    return mycursor.fetchall()


def search_color_in_db(color):
    """ searches car's color in the base, if it is found in the base, function will return its id, else will return empty line """
    if not(color == ''):
        return get_idcolor(color)
    else:
        return ''


def search_model_in_db(model):
    """ searches car's model in the base, if it is found in the base, function will return its id, else will return empty line """
    if not(model == ''):
        return get_idModel(model)
    else:
        return ''


def search_body_type_in_db(body_type):
    """ searches car's body type in the base, if it is found in the base, function will return its id, else will return empty line """
    if not(body_type == ''):
        return get_idBody_type(body_type)
    else:
        return ''


def look_for_cars(values):
    """ searches cars with certain conditions in the base, takes values - conditions """
    sql_command = "SELECT * FROM Cars WHERE "
    mycursor.execute(sql_command + values)
    return mycursor.fetchall()


def delete_car(id_car):
    """ deletes car from the base, takes car's id """
    sql_command = 'DELETE FROM Cars WHERE idCars=%s' % (id_car)
    mycursor.execute(sql_command)
    connection.commit()


def change_cardata(clauses, id_car):
    """ changes car's data in the base, takes clauses - new data, id_car - id of car, which you want to change """
    sql_command = 'UPDATE Cars SET %s WHERE idCars=%s'
    mycursor.execute(sql_command % (clauses, int(id_car)))
    connection.commit()


def get_model_from_tCars(id_car):
    """ returns id of a car whose number is passed by the function parameter """
    mycursor.execute("SELECT Model_idModel FROM Cars WHERE idCars='%s'" % (id_car))
    return get_first_id()


def add_car(car_values):
    """ adds a car to the base, takes car_values: list - characteristics of a car """
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


def add_color(color):
    """ adds color to the Color's table in the base """
    sql_command = "INSERT INTO Color(ColorName) VALUES (%s)"
    mycursor.execute(sql_command, color)
    connection.commit()


def add_body_type(body_type):
    """ adds body type to the Body type table in the base """
    sql_command = "INSERT INTO Body_type(TypeName) VALUES (%s)"
    mycursor.execute(sql_command, body_type)
    connection.commit()


def add_model(model):
    """ adds model to the Model's table in the base """
    sql_command = " INSERT INTO Models(ModelName) VALUES (%s)"
    mycursor.execute(sql_command, model)
    connection.commit()


    

