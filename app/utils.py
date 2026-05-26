import os,random,json


def clear_screen():
    os.system('cls' if os.name == ' nt' else 'clear')
def welcome_page():
    option = input("Welcome!\n\n1.Login\n2.Registration\n3.Exit\nChoose an option: ")
    clear_screen()
    return option
def registration():
    name = input("REGISTRATION\n\nEnter your name: ")
    clear_screen()
    password = input("REGISTRATION\n\nEnter your password: ")
    wallet = str(random.randint(1000000, 9999999))
    balance = 0
    with open("DB.json", "r") as file:
       data = json.load(file)
    data[wallet] = {
            "password": password,
            "name": name,
            "balance": balance,
            "transactions": []
    }

    with open("DB.json", "w") as file:
        json.dump(data,file,indent=4)
    clear_screen()
    print("Relaunch program and login :)")

def login(data_dict):
    try:
        running = False
        while not running:
            wallet = input("LOGIN\n\nEnter your wallet number: ")
            clear_screen()
            if wallet in data_dict:
                running = True
        running = False
        while not running:
            user_password = input("LOGIN\n\nEnter your password: ")
            clear_screen()
            if data_dict[wallet]["password"] == user_password:
                running = True

        name = data_dict[wallet]["name"]
        password = data_dict[wallet]["password"]
        balance = int(data_dict[wallet]["balance"])
        if user_password == password:
            return True, name, wallet, password, balance
        else:
            return False, None, None, None, None
    except TypeError:
            print("Error")

def read_info_db():
    with open("DB.json","r") as file:
        data_dict = json.load(file)
    return data_dict
def main_page(name,balance):
    option = input(f"Hello {name}!             Balance: {balance}$\n\n1.Deposit\n2.Withdraw\n3.History of payments\n4.Exit\n\nChoose an option: ")
    return option
def deposit(balance, data_dict, address):
    clear_screen()
    running = False
    while not running:
        try:
            amount = int(input(f"DEPOSIT            Balance: {balance}$\n\nEnter how much you wanna top up your balance: "))
            running = True
        except ValueError:
            clear_screen()
            continue
    clear_screen()
    question = input(f"DEPOSIT            Balance: {balance}$\n\nAre you sure? Y/N: ")
    if question.lower() == "y":
        address = str(address)
        current = int(data_dict[address]["balance"])
        data_dict[address]["balance"] = str(current + amount)
        return amount,True
    else:
        return True, False
def update_database(data_dict,transactions,user_wallet,new_transaction):
    if new_transaction == True:
        data_dict[user_wallet]["transactions"].extend(transactions)
    with open("DB.json", "w") as file:
        json.dump(data_dict, file, indent=4)
def withdraw(balance,data_dict,wallet):
    clear_screen()
    running = False
    while not running:
        try:
            amount = int(input(f"WITHDRAW            Balance: {balance}$\n\nEnter how much you wanna pop up your balance: "))
            if balance >= amount:
                running = True
            else:
                continue
        except ValueError:
            clear_screen()
            continue
    clear_screen()
    running = False
    while not running:
        address = input(f"WITHDRAW            Balance: {balance}$\n\nEnter recipient wallet number: ")
        if address in data_dict:
            running = True
        else:
            clear_screen()
            print("SUCH WALLET DOESN'T EXIST")
    clear_screen()
    question =  input(f"WITHDRAW            Balance: {balance}$\n\nAre you sure? Y/N: ")
    if question.lower() == "y":
        address = str(address)
        current = int(data_dict[wallet]["balance"])
        data_dict[wallet]["balance"] = str(current - amount)
        current = int(data_dict[address]["balance"])
        data_dict[address]["balance"] = str(current + amount)
        return amount,address,True
    else:
        return True,None,False
def show_history_main(data_dict,user_wallet):
    clear_screen()
    print("HISTORY")
    trunsactions_data = data_dict[user_wallet]["transactions"]
    for item in trunsactions_data:
        print(item)
    input("Enter to stop program")