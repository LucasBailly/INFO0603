# Créé par vala0004, le 01/12/2021 en Python 3.7
# Créé par vala0004, le 30/11/2021 en Python 3.7
from math import log
from random import random,randint
from arithmetiqueDansZEtd import *
from Binaire603 import Binaire603

from CodeurCA import CodeurCA
class ChiffreurRSA(CodeurCA):
    """"""
    def __init__(self, cleP, cleS):
        faire un générateur de clé
        assert isPrime(cleP), "La clé publique doit etre première gros blaireau"
        assert isPrime(cleS), "La clé privée doit etre première gros blaireau"

        self.cleP = cleP
        self.cleS = cleS

    def __str__(self):
        return f"Chiffreur RSA de {self.cleP}"
    def __repr__(self):
        return f"ChiffreurVigenere({self.lb})"

