###### 1
# %%
# 1.a
n = int(input())
a = [i for i in range(n)]

suma=0
for i in range(n): #w przypadku pythona trzeba pamiętać że listę iterujemy od zera
    suma+=a[i]
print(suma)

"""
n operacji == Θ(n)

a - lista liczb
n - dlugosc listy a

suma <- 0
dla i <- 1 do n wykonaj
    suma <- suma+a[i]
"""
# %%
# 1.b
n = int(input())
a = [i for i in range(n)]

iloczyn = 1
for i in range(n): #w przypadku pythona trzeba pamiętać że listę iterujemy od zera
    iloczyn*=a[i]
print(suma)

"""
n operacji == Θ(n)

a - lista liczb
n - dlugosc listy a

iloczyn <- 1
dla i <- 1 do n wykonaj
    iloczyn <- iloczyn*a[i]
"""
# %%
# 1.c
n = int(input())
a = [i for i in range(n)]

suma=0
for i in range(n): #w przypadku pythona trzeba pamiętać że listę iterujemy od zera
    suma+=a[i]
srednia = suma / n
print(srednia)

"""
n+1 operacji == Θ(n)

a - lista liczb
n - dlugosc listy a

suma <- 0
dla i <- 1 do n wykonaj
    suma <- suma+a[i]
srednia = suma / n
"""
# %%
# 1.d
n = int(input())
a = [i for i in range(n)]

suma=0
ilosc=0
for i in range(n): #w przypadku pythona trzeba pamiętać że listę iterujemy od zera
    if a[i]>0:
        suma+=a[i]
        ilosc+=1
srednia = suma/ilosc
print(srednia)

"""
n operacji == Θ(n)

a - lista liczb
n - dlugosc listy a

suma <- 0
ilosc <- 0
dla i <- 1 do n wykonaj
jesli a[i] większa od 0 to
    suma <- suma+a[i]
ilosc <- ilosc + 1
srednia <- suma/ilosc
"""

# %%
# 1.e
n = int(input())
a = [i for i in range(n)]

suma=0
for k in range(n): #w przypadku pythona trzeba pamiętać że listę iterujemy od zera
    iloczyn = 1
    for i in range(k):
        iloczyn*=a[i]
    suma+=iloczyn
print(suma)

"""
(n^2+n)/2 operacji == Θ(n^2)

a - lista liczb
n - dlugosc listy a

suma <- 0
dla k <- 1 do n wykonaj
    iloczyn <- 1
    dla i <- 1 do k wykonaj
        iloczyn <- iloczyn*a[i]
    suma <- suma+iloczyn
"""

# %%
# 1.f
n = int(input())
a = [i for i in range(n)]

suma=0
for k in range(n): #w przypadku pythona trzeba pamiętać że listę iterujemy od zera
    iloczyn = 1
    for i in range(k, n):
        iloczyn*=a[i]
    suma+=iloczyn
print(suma)

"""
(1n/2)*n operacji == Θ(n^2)

a - lista liczb
n - dlugosc listy a

suma <- 0
dla k <- 1 do n wykonaj
    iloczyn <- 1
    dla i <- k do n wykonaj
        iloczyn <- iloczyn*a[i]
    suma <- suma+iloczyn
"""

###### 2
# %%
# 2.b
def ZAGATKA(n):
    ilosc=0
    while True:
        ilosc+=1
        if n%2 == 0:
            n//=2
        else:
            if n == 1:
                break
            else:
                n=n*3+1
    return ilosc

print(ZAGATKA(int(input())))

"""
ZAGATKA(n):
    ilosc <- 0
    dopóki Prawda wykonuj
        ilosc <- ilosc+1
        jeżeli n modulo 2 porównywalne z 0 to
            n <- n/2
        w innym wypadku to
            jeżeli n porównywalne z 1 to
                zakończ pętlę
            w innym wypadku to
                n <- n*3+1
    zwróć ilosc
"""

# %%

