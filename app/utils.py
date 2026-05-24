import os,random


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
    wallet = random.randint(1000000, 9999999)
    with open("DB.txt", "a") as file:
        file.write(f"{wallet}|{name}|{password}\n")
    clear_screen()
def login(data_dict):
    try:
        wallet = input("LOGIN\n\nEnter your wallet number: ")
        clear_screen()
        user_password = input("LOGIN\n\nEnter your password: ")
        info = data_dict[wallet]
        name = info[1]
        password = info[2]
        if user_password == password:
            return True, name, wallet, password
        else:
            return False, None, None,None
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
def main_page():