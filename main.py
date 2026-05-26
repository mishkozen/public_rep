from app.utils import clear_screen, welcome_page, registration, read_info_db, main_page, login, deposit, withdraw,update_database,show_history_main
from app.wallet import Wallet
from app.user import User

running = False

while not running:
    welcome_cycle = False
    while not welcome_cycle:
        option = welcome_page()
        if option == "1" or option == "2" or option == "3":
            welcome_cycle = True

    first_cycle = False
    while not first_cycle:
        main_cycle = True
        match option:
            case "1":
                data_from_db = read_info_db()
                checking,name,wallet,password,balance = login(data_from_db)
                if checking:
                    user_logged = User(name,wallet,password)
                    user_wallet = Wallet(wallet,balance)
                    first_cycle = True
                    main_cycle = False
                else:
                    continue
            case "2":
                registration()
                running = True
                first_cycle = True

            case "3":
                running = True
                first_cycle = True



    while not main_cycle:
        option = main_page(user_logged.get_info_name(),user_wallet.get_info_balance())
        new_trun = False
        match option:
            case "1":
                amount,new_trun = deposit(user_wallet.get_info_balance(),data_from_db,user_logged.get_info_wallet())
                if amount != True:
                    user_wallet.deposit(amount)
                    update_database(data_from_db,user_wallet.show_history(),user_logged.get_info_wallet(),new_trun)
                    user_wallet.clear_history()
                else:
                    continue
            case "2":
                amount, address,new_trun =  withdraw(user_wallet.get_info_balance(),data_from_db,user_logged.get_info_wallet())
                if amount != True:
                    user_wallet.withdraw(amount,address)
                    update_database(data_from_db,user_wallet.show_history(),user_logged.get_info_wallet(),new_trun)
                    user_wallet.clear_history()
                else:
                    continue
            case "3":
                show_history_main(data_from_db,user_logged.get_info_wallet())
            case "4":
                main_cycle = True
                running = True
                clear_screen()
