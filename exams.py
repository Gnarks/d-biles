def syracus(n):
    print(n, end=" ")
    if n == 1:
        return 1
    if n % 2 == 0:
        return syracus(n//2)
    else:
        return syracus(3*n+1)


def temps_vol(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + temps_vol(n/2)
    else:
        return 1 + temps_vol((3*n)+1)


def hauteur_vol(n):
    if n == 1:
        return 4
    if n % 2 == 0:
        return hauteur_vol(n//2)
    else:
        max = hauteur_vol(3*n+1)
        return 3*n+1 if 3*n+1 > max else max


def split(t):
    return t[:len(t)//2], t[len(t)//2:]


def merge(t1, t2):
    if len(t1) == 0:
        return t2
    elif len(t2) == 0:
        return t1
    elif t1[-1] > t2[-1]:
        last = t1.pop()
        new = merge(t1, t2)
        new.append(last)
        return new
    else:
        last = t2.pop()
        new = merge(t1, t2)
        new.append(last)
        return new


def merge_sort(t):

    if len(t) > 1:
        t1, t2 = split(t)
        merge_sort(t1)
        merge_sort(t2)

        return merge(t1, t2)
    else:
        return t


def decompress(chaine):
    result = ""
    i = 0
    while i < len(chaine):
        count = ""
        while i < len(chaine) and chaine[i] in "123456789":
            count += chaine[i]
            i += 1

        if len(count) > 0:
            result += int(count)*chaine[i]
        else:
            result += chaine[i]
        i += 1
    return result


print(decompress("3a5b2cg"))


def f(n, m):
    if n <= 1 or m <= 1:
        print(n + m,end=" ")
    else:
        print(n + m,end=" ")
        for i in range(n):
            f(n, m / 2)
            
class Personne():
    
    amis = []
    def __init__(self,name,amis=[]):
        self.name = name
        self.amis = amis
    def ajouterami(self,ami):
        if ami!= self and ami not  in self.amis:
            self.amis.append(ami)
            
    def ajouteramisdami(self):
        amistoadd =[]
        
        for ami in self.amis:
            for amidami in ami.amis:
                if amidami != self and amidami not in self.amis:
                    amistoadd.append(amidami)
        for ami in amistoadd:
            self.amis.append(ami)
            
non = Personne("non")
oui = Personne("oui",[non])
deux = Personne("deux")
un = Personne("un",[oui,deux])
add = Personne("add",[un])

add.ajouteramisdami()

for ami in add.amis:
    print(ami.name)