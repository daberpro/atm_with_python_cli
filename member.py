from card_credit import Card 

class Member(Card):
    def __init__(self,id,pin_member = 100578,saldo_member = 100000):
        super().__init__(pin_member,saldo_member)
        self.id = id

    def getPinInfo(self):
        return self.pin

    def getSaldoInfo(self):
        return self.saldo

    def getMemberId(self):
        return self.id

    def setDebet(self,nominal):
        self.saldo -= nominal

    def setSimpan(self,nominal):
        self.saldo += nominal
