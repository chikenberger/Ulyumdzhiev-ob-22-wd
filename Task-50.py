class Bank:
    def __init__(self):
        self.clients = {}

    def create_client(self, name):
        if name not in self.clients:
            self.clients[name] = {}
            print(f"Клиент {name} создан")
        else:
            print("Ошибка: клиент с таким именем уже существует")

    def open_account(self, client_name, account_number, initial_balance=0):
        if client_name in self.clients:
            if account_number not in self.clients[client_name]:
                self.clients[client_name][account_number] = initial_balance
                print(f"Открыт счет {account_number} для клиента {client_name}")
            else:
                print("Ошибка: счет с таким номером уже существует")
        else:
            print("Ошибка: клиент с таким именем не найден")

    def make_transfer(self, client_name, from_account, to_account, amount):
        if from_account in self.clients[client_name] and to_account in self.clients[client_name]:
            if self.clients[client_name][from_account] >= amount:
                self.clients[client_name][from_account] -= amount
                self.clients[client_name][to_account] += amount
                print(f"Перевод на сумму {amount} выполнен успешно")
            else:
                print("Ошибка: недостаточно средств на счете для перевода")
        else:
            print("Ошибка: счет отправителя или получателя не существует")



bank = Bank()

bank.create_client("Иванов")
bank.open_account("Иванов", "12345", 1000)
bank.open_account("Иванов", "67890", 500)

bank.make_transfer("Иванов", "12345", "67890", 300)
