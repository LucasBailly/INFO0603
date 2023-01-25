# Créé par vala0004, le 01/12/2021 en Python 3.7
# Créé par vala0004, le 30/11/2021 en Python 3.7
from math import log
from random import random,randint
from arithmetiqueDansZEtd import *
from Binaire603 import Binaire603

from CodeurCA import CodeurCA
class ChiffreurVigenere(CodeurCA):
    """"""
    def __init__(self ,cle=['a', 'b', 'c']):
        self.lb = cle

    def __str__(self):
        return f"Chiffreur par décalage de {self.lb}"
    def __repr__(self):
        return f"ChiffreurVigenere({self.lb})"


    def binCode(self,monBinD:Binaire603)->Binaire603:
        """
        >>> ChiffreurVigenere(Binaire603([1, 2, 7])).binCode(Binaire603([ 0x02, 0x04, 0x12, 0x07]))
        Binaire603([ 0x03, 0x06, 0x19, 0x08])
        """
        position=0
        monBinC=[]
        for monB in monBinD:
            monBinC.append(monB + self.lb[position])
            position = (position+1)%len(self.lb)
        return Binaire603(monBinC)



    def binDecode(self,monBinC:Binaire603)->Binaire603:
        """
        >>> ChiffreurVigenere(Binaire603([1, 2, 7])).binDecode(Binaire603([ 0x03, 0x06, 0x19, 0x08]))
        Binaire603([ 0x02, 0x04, 0x12, 0x07])
        """
        position=0
        monBinD=[]
        for monB in monBinC:
            monBinD.append(monB - self.lb[position])
            position = (position+1)%len(self.lb)
        return Binaire603(monBinD)

    def demo():
        monCodeur=ChiffreurVigenere(Binaire603([1, 2, 7]))
        for k in range(3):
            monBin=Binaire603([ 0x03, 0x06, 0x19, 0x08])
            print("Bin:",monBin)
            monBinCr=monCodeur.binCode(monBin)
            print("Bin Codée:",monBinCr)
            print("monBinCr décodé est égal à Monbin ?",monCodeur.binDecode(monBinCr)==monBin)

        montext='Bonjour les amis !'
        lb=Binaire603(montext)
        chif=ChiffreurVigenere(Binaire603([1, 2, 7]))
        lbc=chif.binCode(lb)
        lbd=chif.binDecode(lbc)
        print(f"{chif} a codé le texte '{montext}' en '{lbc.toString()}' et a décodé en '{lbd.toString()}' ")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    ChiffreurVigenere.demo()