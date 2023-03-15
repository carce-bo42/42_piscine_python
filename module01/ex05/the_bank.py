
class Account(object):
    
    ID_COUNT = 1

    def __init__(self, name, **kwargs):

        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name

        if not hasattr(self, 'value'):
            self.value = 0

        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")
        
    def transfer(self, amount):
        self.value += amount

# in the_bank.py
class Bank(object):

    """The bank"""

    def __init__(self):
        self.accounts = []
    
    def add(self, new_account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        # ... Your code ...
        self.accounts.append(new_account)

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """

    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """

    def check_account_type(self, new_account) -> bool:
        return new_account.__instancecheck__(Account)

    def check_account_corrupted(self, new_account) -> bool:
        attributes = dir(new_account)

        # length must be even
        if len(attributes) % 2 is not 0:
            return False
        
        # no attributes allowed to begin by 'b', 'zip' or 'addr'
        for att in attributes:
            if att.startswith("b") or att.startswith("zip") or att.startswith("addr"):
                return False
        
        # must contain name, id and value attributes
        needed = ["name", "id", "value"]
        if not all(att in attributes for att in needed):
            return False
        
        # name must be str
        if type(new_account.name) is not str:
            return False
        
        # id must be int
        if type(new_account.id) is not int:
            return False
        
        # value must be int or float
        if type(new_account.value) is not int \
            and type(new_account.value) is not float:
            return False

        # All OK 
        return True