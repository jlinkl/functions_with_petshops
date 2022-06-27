# WRITE YOUR FUNCTIONS HERE


def get_pet_shop_name(shop):
    return shop["name"]

def get_total_cash(shop):
    return shop["admin"]["total_cash"]

def add_or_remove_cash(shop, cash):
    shop["admin"]["total_cash"] += cash

def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

def increase_pets_sold(shop, sold):
    shop["admin"]["pets_sold"] += sold

def get_stock_count(shop):
    return len(shop["pets"])

def get_pets_by_breed(shop, pet_breed):
    found =[]
    for pet in shop["pets"]:
        if pet["breed"] == pet_breed:
            found.append(pet["breed"])
    return found

def find_pet_by_name(shop, pet_name):
    for pet in shop["pets"]:
        if pet["name"] == pet_name:
            return pet

def remove_pet_by_name(shop, pet_name):
    count = 0
    for pet in shop["pets"]:
        if pet["name"] == pet_name:
            shop["pets"].pop(count)
        count += 1

def add_pet_to_stock(shop, pet):
    shop["pets"].append(pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, money):
    customer["cash"] -= money

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

def customer_can_afford_pet(customer, pet):
    if customer["cash"] >= pet["price"]:
        return True
    else:
        return False

def sell_pet_to_customer(shop, pet, customer):
    if pet != None:
        if (customer_can_afford_pet(customer, pet)):
            remove_customer_cash(customer, pet["price"])
            add_pet_to_customer(customer, pet)
            remove_pet_by_name(shop, pet)
            increase_pets_sold(shop, 1)
            add_or_remove_cash(shop, pet["price"])