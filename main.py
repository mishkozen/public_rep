from app.utils import clear_screen, welcome_page, registration, read_info_db
from app.wallet import Wallet
from app.user import User

running = False
data_from_db = read_info_db()
while not running:
    option = welcome_page()
    first_cycle = false
    while not first_cycle:
        match option:
            case "1":
                checking,name,wallet,password = login(data_from_db)
                if checking:
                    user = User(name,wallet,password)
                    user_wallet = Wallet(wallet)
                    first_cycle = True
                else:
                    continue
            case "2":
                registration()
                first_cycle = True
            case "3": running = True
