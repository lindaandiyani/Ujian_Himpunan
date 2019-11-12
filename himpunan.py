# # angka = list(range(101))
# # # print(angka)

Angka = list(range(1,20))
Angka = set(Angka)
# print(Angka)
A= set(filter(lambda x: x%2==0,Angka))
print('A= ',A)
B =set(filter(lambda x: x%2!=0,Angka))
print('B= ',B)
C = set(range(-9,0))
print('C= ',C)
def prima(x):
    a= False
    if x > 1:
        if x == 2:
            a= True
        else :
            for i in range(2,x):
                if x %i == 0:
                    a= False
                    break
                else:
                    a= True
    else:
        a= False
    return a


D = set (filter(prima,range(20)))
print('D= ',D)
E = (Angka.difference(D))
print ('E= ',E)

#  Soal A
a= print('soal a = ',(((A.union(B)).union(C)).union(D)).union(E)) 
# Soal B
b =print('soal b = ',(A.intersection(B)).union(D.intersection(E))) #menghasilkan himpunan kosong
# Soal C
c=print('soal c = ',(A.union(B)).intersection(D.union(E)))    #(a ub)n(d u E)
# Soal D
d = print('soal d = ',(A.union(B)).difference((D.union(E)))) #enghasilkan himpunan kosong
# Soal E
e = print('soal e = ',((A.union(B)).union(C))-(A.intersection(E)))
