import random
import string

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

        if self.check_account_type(new_account) == False:
            return False

        if "name" not in new_account.__dict__.keys():
            return False

        if new_account.name in (acc.name for acc in self.accounts):
            return False

        self.accounts.append(new_account)
        return True

    def transfer(self, origin, dest, amount):
        
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """

        if type(origin) is not str \
            or type(dest) is not str:
            return False
        
        if not all(acc.name in (origin, dest) for acc in self.accounts):
            return False
        
        origin = next((acc for acc in self.accounts if acc.name == origin), None)
        dest = next((acc for acc in self.accounts if acc.name == dest), None)

        if self.check_account_corrupted(origin) == False \
            or self.check_account_corrupted(dest) == False \
                or amount < 0 \
                or origin.value < amount:
            return False
        
        if origin.name is dest.name:
            return True
        
        origin.transfer(-amount)
        dest.transfer(amount)
        return True

    def fix_account(self, name):
        """ fix account associated to name if corrupted. Since the 'add'
            method MUST ONLY control the Account type and name repetition,
            corrputed accounts can get into the Bank. When they try to 
            transfer or get transferred, an error occurs. Calling fix_account
            should fix whatever problem they have.
            
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        if name not in [acc.name for acc in self.accounts]:
            return False

        account = next((acc for acc in self.accounts if acc.name == name), None)

        # Cannot fix a non Account type
        if self.check_account_type(account) == False:
            return False
        
        # Cannot fix what is not corrupted
        if self.check_account_corrupted(account) == True:
            return True

        if not hasattr(account, "id") \
            or type(account.id) is not int:
            Account.ID_COUNT += 1
            self.id = Account.ID_COUNT

        if not hasattr(account, "value") \
            or type(account.value) is not str:
            self.value = 0

        # Do the number of attributes check at the end, since we might have added
        # some more.
        attributes = account.__dict__.keys()
        for att in attributes:
            if att.startswith("b"):
                delattr(att)
        
        # Add zip if no attribute starting with zip or addr.
        if any(not att.startswith(("zip", "addr")) for att in attributes):
            setattr(account, "zip", "E3 3PR")

        # Add a new attribute if number of attributes is odd
        if len(attributes) % 2 != 0:
            while True:
                new_attr = self.get_random_string(10)
                if not hasattr(account, str(new_attr)):
                    setattr(account, "new_attr", "filler attribute lmfao")
                    break
        
        return True
                    

    def get_random_string(self, length):
        # With combination of lower and upper case
        result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
        return result_str

    def check_account_type(self, new_account) -> bool:
        return type(new_account) == Account

    def check_account_corrupted(self, new_account) -> bool:
        attributes = new_account.__dict__
        
        # length must be even
        if len(attributes.keys()) % 2 != 0:
            return False
        
        # no attributes allowed to begin by 'b', 'zip' or 'addr'
        for att in attributes.keys():
            if att.startswith("b"):
                return False
        
        if not any(not att.startswith(("zip", "addr")) for att in attributes.keys()):
            return False
        
        # must contain name, id and value attributes
        needed = ["name", "id", "value"]
        if not all(att in attributes.keys() for att in needed):
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

    def check_account_repeated(self, new_account) -> bool:
        if new_account.name in self.accounts:
            return False

