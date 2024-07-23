class Account():

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

    def deposit(self):
        pass

    def withdraw(self):
        pass
    
class TimeZone():
    pass

    def get_offset_time_stamp(self):
        pass