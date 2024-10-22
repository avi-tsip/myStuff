import inspect
import pytz
from datetime import datetime, timezone

class Account():

    INTEREST_RATE = 0.5

    def __init__(self, account_number, first_name, last_name, tz_offset) -> None:
        self._account_number = account_number
        self._first_name = first_name
        self._last_name = last_name
        self._tz_offset = tz_offset
        self._balance = 0

    @property
    def name(self):
        return self._first_name + " " + self._last_name
    
    @name.setter
    def name(self, first_name_value, last_name_value):
        self._first_name = first_name_value
        self._last_name = last_name_value

    @property
    def tz_offset(self):
        return TimeZone.get_offset_time_stamp()

    @tz_offset.setter
    def tz_offset(self, value):
        self._tz_offset = value

    @property
    def balance(self):
        return self._balance

    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise f'The account balance must be above 0'
        else:
            self._balance = value

    def deposit(self, deposit_amount):
        self._balance = self._balance + deposit_amount
        self.balance(self._balance)
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)[1][3]
        if calframe == 'calc_interest_rate':
            return self.generate_conf_number(AccountActions.Interest)
        else:
            return self.generate_conf_number(AccountActions.Deposit)
        
    def withdraw(self, withdraw_amount):
        if self._balance - withdraw_amount < 0:
            print(f"Account number: {self._account_number} balance can't be negative!") 
            return self.generate_conf_number(AccountActions.Decline)
        else:
            self._balance = self._balance - withdraw_amount
            self.balance(self._balance)
            return self.generate_conf_number(AccountActions.Withdraw)

    def calc_interest_rate(self):
        interest_rate = self._balance * Account.INTEREST_RATE
        self.deposit(interest_rate)


    def generate_conf_number(self, type):
        return f'{type}-{self._account_number}-{TimeZone.time_stamp_by_timezone()}-{Counter.get_transaction_number()}'
    
    def get_conf_info(self):
        pass


class AccountActions():

    Withdraw = 'W'
    Deposit = 'D'
    Interest = 'I'
    Decline = 'X'

class TimeZone():
    
    def __init__(self, tz) -> None:
        self._tz = 'Europe/London'

    @property
    def time_zone(self, value):
        return self._tz
    
    @timezone.setter
    def time_zone(self, value):
        self._tz = value

    @property
    def time_stamp_by_timezone(self):
        tz_offset = pytz.timezone(self._tz) 
        return datetime.now(tz_offset).strftime("%Y%m%d%H%m%S")

class Counter():
    
    def get_transaction_number(self):
        with open("counter", "r+") as file:
            counter_value = (file.read())
            file.seek(0)
            file.write(counter_value + 1)
            return counter_value
