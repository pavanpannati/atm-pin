import pickle
class atm:
    __name='pavan'
    def __init__(self):
        self.name=atm.__name
        self.pin=1880
        self.balance=20000
    
    
with open('atm_pin.txt','wb') as a:
    p1=atm()
  
    pickle.dump([p1],a)

