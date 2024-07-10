class BankAccount:
    rate = 1.2

print(BankAccount.__dict__)
"""
{'__module__': '__main__', 
'rate': 1.2, '__dict__': <attribute '__dict__' of 'BankAccount' objects>, 
'__weakref__': <attribute '__weakref__' of 'BankAccount' objects>, '__doc__': None}
"""

print(BankAccount.rate) # 1.2

acct1 = BankAccount()
acct2 = BankAccount()

print(acct1.__dict__) # {}
print(acct1.rate) # 1.2

print(acct2.__dict__) # {}
print(acct2.rate) # 1.2

print(acct2 is acct1) # False

BankAccount.account_type = 'savings'
print(acct2.account_type) # savings
print(acct2.account_type) # savings

acct1.rate = 0.8 # now we created an instance attribute
print(acct1.__dict__) 
"""
{'rate': 0.8}
"""
print(acct2.rate) # 1.2 - still gets the rate from the class attribute

setattr(acct2, 'rate', 0.5) # created an instance attribute for hte second instance                                                                                                                         
print(acct2.__dict__)             
"""
{'rate': 0.5}
"""
 # when adding and instance attribute to one of the instances, it will not be reflected in the class or other instances 

print(type(BankAccount.__dict__)) # mappingproxy - cannot be muted unless using setattr
print(type(acct1.__dict__)) # dict - can be muted via dict method

