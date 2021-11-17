# банковский счет
from datetime import datetime
import pytz

WHITE = '\033[00m'
GREEN = '\033[0;92m'
RED = '\033[1;31m'

class Account:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance # user не должен иметь шанс менять balance напрямую типа a.balance += 1000000
        # значение баланса должно меняться только в рез-те прихода или расхода,
        # поэтому этот атрибут должен быть приватным _
        self._history = [] # то же самое

    @staticmethod
    def _get_current_time():
        return pytz.utc.localize(datetime.utcnow())
        # здесь экземпляр класса никак не используется,
        # поэтому статический метод

    def deposit(self, amount):
        self._balance += amount
        self.show_balance()
        self._history.append([amount,
                             self._get_current_time()])

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f'You spent {amount} units')
            self.show_balance()
            self._history.append([-amount,
                                 self._get_current_time()])
        else:
            print('Not enough money')
            self.show_balance()

    def show_balance(self):
        print(f'Balance {self._balance}')

    def show_history(self):
        for amount, date in self._history:
            if amount > 0:
                transaction = 'deposited'
                color = GREEN
            else:
                transaction = 'withdrawed'
                color = RED
            print(f'{color} {amount} {WHITE} {transaction} on {date.astimezone()}')



a = Account('marina', 0)

a.show_balance()
a.deposit(100)



