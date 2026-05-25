import os,random,ast


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
    with open("DB.txt", "a") as file:
        file.write(f"{wallet}|{name}|{password}|{balance}| \n")
    clear_screen()
    print("Relaunch program and login :)")

def login(data_dict):
    try:
        wallet = input("LOGIN\n\nEnter your wallet number: ")
        clear_screen()
        user_password = input("LOGIN\n\nEnter your password: ")
        info = data_dict[wallet]
        name = info[1]
        password = info[2]
        balance = int(info[3])
        if user_password == password:
            return True, name, wallet, password, balance
        else:
            return False, None, None, None, None
    except TypeError:
            print("SUCH WALLET DOESN'T EXIST")

def read_info_db():
    with open("DB.txt","r") as file:
        data_dict = {}
        for line in file:
            clean_line = line.strip()
            if clean_line:
                parts = clean_line.split('|')
                data_dict[parts[0]] = parts
    return data_dict
def main_page(name,balance):
    option = input(f"Hello {name}!             Balance: {balance}$\n\n1.Deposit\n2.Withdraw\n3.History of payments\n4.Exit\n\nChoose an option: ")
    return option
def deposit(balance, data_dict, address):
    clear_screen()
    try:
        amount = int(input(f"DEPOSIT            Balance: {balance}$\n\nEnter how much you wanna top up your balance: "))
    except ValueError:
        return True
    clear_screen()
    question = input(f"DEPOSIT            Balance: {balance}$\n\nAre you sure? Y/N: ")
    if question.lower() == "y":
        address = str(address)
        try:
            current = int(data_dict[address][3])
        except Exception:
            current = 0
        data_dict[address][3] = str(current + amount)
        return amount,True
    else:
        return True, False
def update_database(data_dict,transactions,user_wallet,new_trun):
    if new_trun == True:
        transactions_data = data_dict[user_wallet][4]
        if transactions_data == "" or transactions_data is None:
            new_transactions = []
        else:
            new_transactions = ast.literal_eval(transactions_data)
        new_transactions.append(transactions)
    with open("DB.txt", "w") as file:


        for address, values in data_dict.items():

            wallet = values[0]
            name = values[1]
            password = values[2]
            balance = values[3]

            if user_wallet == wallet and new_trun == True:
                file.write(f"{wallet}|{name}|{password}|{balance}|{new_transactions}\n")
            else:
                file.write(f"{wallet}|{name}|{password}|{balance}| \n")
def withdraw(balance,data_dict,wallet):
    clear_screen()
    amount = int(input(f"WITHDRAW            Balance: {balance}$\n\nEnter how much you wanna send: "))
    clear_screen()
    address = input(f"WITHDRAW            Balance: {balance}$\n\nEnter recipient wallet number: ")
    clear_screen()
    question =  input(f"WITHDRAW            Balance: {balance}$\n\nAre you sure? Y/N: ")
    if question.lower() == "y":
        address = str(address)
        current = int(data_dict[wallet][3])
        data_dict[wallet][3] = str(current - amount)
        current = int(data_dict[address][3])
        data_dict[address][3] = str(current + amount)
        return amount,address,True
    else:
        return True,None,False
def show_history_main(data_dict,user_wallet):
    clear_screen()
    print("HISTORY")
    trunsactions_data = ast.literal_eval(data_dict[user_wallet][4])
    for item in trunsactions_data:
        print(item)
    input("Enter to stop program")