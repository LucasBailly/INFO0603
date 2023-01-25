import random
class fFeistel(fBijIbjectsCA):

    def __init__(self, nb_tours=6, k=81, f=fBijDecallage):
        this.lk = random.randint(0,k)       #liste de clés k' générées aléatoirementsà partir de k

    def __call__(self,octet):
        l,r = octet//16, octet%16
        for i in range(self.nb_tours):
            l
