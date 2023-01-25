from math import log
from random import random,randint
from arithmetiqueDansZEtd import *
from Binaire603 import Binaire603

from CodeurCA import CodeurCA
class ChiffreurAffine(CodeurCA):

    def __init__(self, a, b):
        a_tmp = ElementDeZnZ(a,256)
        assert a_tmp.estInversible(), "a doit être inversible"
        self.a = a_tmp
        self.b = ElementDeZnZ(b,256)

    def __str__(self):
        return f"Chiffreur affine (a={self.a}, b={self.b})"
    def __repr__(self):
        return f"ChiffreurAffine({self.a},{self.b})"

    def binCode(self,monBinD:Binaire603)->Binaire603:
        """
        >>> ChiffreurAffine(3,5).binCode(Binaire603([ 0x02, 0x04, 0x12, 0x07]))
        Binaire603([ 0x0b, 0x11, 0x3b, 0x1a])
        >>> ChiffreurAffine(3,5).binDecode(Binaire603("Ceci est un test")).toString()
        'j ÊÌĉ z%ĉÐ#ĉ% z%'
        """
        return Binaire603([x *self.a + self.b for x in monBinD])

    def binDecode(self,monBinC:Binaire603)->Binaire603:
        """
        >>> ChiffreurAffine(3,5).binDecode(Binaire603([ 0x0b, 0x11, 0x3b, 0x1a]))
        Binaire603([ 0x02, 0x04, 0x12, 0x07])
        """
        return Binaire603([(y-self.b)//self.a for y in monBinC])