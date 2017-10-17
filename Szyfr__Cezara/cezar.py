alfabet = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
import os
import math
klucze = open("key.txt.txt", "r").read().split()
# klucze do szyfru afinicznego.
keyA = int(klucze[0])
keyB = int(klucze[1])
# Sprawdzamy poprawność klucza a.
isKeyGood = True if math.gcd(keyA, 26)==1 else False

def odwrotnoscModulo(a, b, s0=1, s1=0):
    return s0 if b==0 else odwrotnoscModulo(b, a%b, s1, s0-s1*(a//b))
print(odwrotnoscModulo(3,26))

clear = lambda: os.system('clrscr')
# napis = ""
def error(litera):
    print("[Litera spoza alfabetu:\t", litera, "]")
    return "_"

def menu(wybor):
    funkcje[wybor]()

def cezar():
    a = open('plain.txt', 'r').read()
    x = 0
    napis = ""
    while x < a.__len__():
        napis += alfabet[(ord(a[x])-65 + keyA) % 26] if a[x] in alfabet else error(a[x])
        x += 1
    b = open('crypto.txt', 'w')
    b.write(napis)
    b.close()
def decryptCezar():
    a = open('crypto.txt', 'r').read()
    x = 0
    napis = ""
    while x < a.__len__():
        napis += alfabet[(ord(a[x])-65 -keyA ) % 26] if a[x] in alfabet else error(a[x])
        x += 1
    b = open('plain.txt', 'w')
    b.write(napis)
    b.close()
def afiniczny():
    a = open('plain.txt', 'r').read()
    x=0
    napis=""
    while x < a.__len__():
        napis += alfabet[(c * (ord(a[x])-65) + d) % 26]
        x+=1
    b = open('crypto.txt', 'w')
    b.write(napis)
    b.close()

def decryptAfiniczny():
    a = open('crypto.txt', 'r').read()
    x=0
    napis=""
    aPrim=round(odwrotnoscModulo(keyA,26))
    print(c_prim)
    while x < a.__len__():
        napis+= alfabet[((ord(a[x])-65-keyB)*aPrim)%26]
        x+=1
    b = open('plain.txt', 'w')
    b.write(napis)
    b.close()

def szyfruj():
    print('szyfruj')
def odszyfruj():
    ""
def analizaCezar():
    a = ord(open('plain.txt', 'r').read()[0]) -65
    b = ord(open('crypto.txt', 'r').read()[0]) - 65
    print("Przesuniecie szyfru Cezara to: ", (b-a) %26)

def kryptoanaliza():
    ""

funkcje = {
    '-c-e' : cezar,
    '-c-d' : decryptCezar,
    '-a-e' : afiniczny,
    '-a-d' : decryptAfiniczny,
    '-j-c' : analizaCezar,
    '-k' : kryptoanaliza
}
if isKeyGood:
    print(
        "Wybierz jedna z opcji: \n-c (szyfr Cezara),\n-a (szyfr afiniczny),\n______________________\n\n          +\n______________________\n-e (szyfrowanie),\n-d (odszyfrowywanie),\nJEDYNA DODATKOWA OPCJA:\n-j-c (kryptoanaliza szyfru Cezara z tekstem jawnym)\n-w: wyjście")
    wybor = ""
    while wybor!="-w":
        print('menu')
        wybor = input("prosze, dokonaj wyboru")
        menu(wybor) if wybor in funkcje else print("Błędne polecenie, należy wybrać rodzaj szyfrowania oraz zadaie - np. dla szyfrowania Cezara: -c-e")
else:
    print("Błędny klucz, NWD(", keyA, ", 26) != 1")
