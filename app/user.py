class User:
    def __init__(self, name, wallet,password):
            self._name = name
            self._wallet = wallet
            self._password = password
    def get_info_name(self):
        return self._name
    def get_info_wallet(self):
        return self._wallet