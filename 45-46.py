import math
import random


def simple_calc():
    try:
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))
        result = first_number / second_number
        print(result)
        return result
    except ValueError:
        print("not a number")
    except ZeroDivisionError:
        print("can not divide by zero")
    finally:
        print("Over")

# simple_calc()

#----------------------------------------------

def value_n_index_errors():
    list1 = [10,20,30,40,50,60,70,80,90,99]
    try:
        index = int(input("Enter index: "))
        result = list1[index]
        print(result)
        return result
    except ValueError:
        print("not a number")
    except IndexError:
        print("index out of range")
    finally:
        print("Over")

# value_n_index_errors()

#----------------------------------------------

def sales_input():
    sales_list = []
    try:
        sales = input("Enter sales divided by space: ")
        for sale in sales.split():
            sales_list.append(float(sale))
        result = sum(sales_list)
        print(result)
        return result
    except ValueError:
        print("not a number")
    finally:
        print("Over")

# sales_input()

#----------------------------------------------

def square_root():
    try:
        root = float(input("Enter root: "))
        if root < 0:
            raise Exception("Root can not be negative")
        result = math.sqrt(root)
        print(result)
        return result
    except ValueError:
        print("not a number")
    except Exception as error:
        print(error)
    finally:
        print("Over")

# square_root()

#----------------------------------------------

def scu_info():
    products = {}
    try:
        example = "EXAMPLE!!!!! Name,price(1.5),quantity(10)"
        print(example)
        scu = input("Enter products divided by COMAS!!!!!!!!!!!: ")
        parts = scu.split(",")
        if len(parts) != 3:
            raise Exception(example)
        name = parts[0].strip()
        price = float(parts[1])
        quantity = int(parts[2])
        products[name] = {
            "price": price,
            "quantity": quantity
        }
        print(products)
        return products
    except ValueError:
        print("Invalid price or quantity")
    except Exception as error:
        print(error)
    finally:
        print("Over")

# scu_info()

#----------------------------------------------

def connect_to_server():
    if random.choice([True, False]):
        return "Connection has established successfully"
    else:
        raise ConnectionError("Connection has not established yet")
try:
    result = connect_to_server()
    print(result)
except ConnectionError:
    print("Connection failed")
finally:
    print("Over")



