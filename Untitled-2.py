class Transoprtlidzeklis():
    def __init__(self,modelis,krasa,motoratilpums,atrumkarba):
        self.modelis = modelis
        self.krasa = krasa
        self.motoratilpums = motoratilpums
        self.atrumkarba = atrumkarba

    def dati(self):
        print(f"modelis: {self.modelis}")
        print(f"krasa:{self.krasa}")
        print(f"motor tilpums:{self.atrumkarba}")
        print(f"atrumkarba:{self.atrumkarba}")
auto = Transoprtlidzeklis("outlander","melna","10","manuala")
