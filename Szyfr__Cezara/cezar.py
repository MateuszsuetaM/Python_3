alfabet = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
import os
import math
klucze = open("key.txt", "r").read().split()
# klucze do szyfru afinicznego i przesuniecia Cezara (keyA), w pliku powinny być rozdzielone spacją
keyA = int(klucze[0])
keyB = int(klucze[1])
# Sprawdzamy poprawność klucza a
isKeyGood = True if math.gcd(keyA, 26)==1 else False

def odwrotnoscModulo(a, b, s0=1, s1=0):
    return s0 if b==0 else odwrotnoscModulo(b, a%b, s1, s0-s1*(a//b))
def error(litera):
    print("[Litera spoza alfabetu:\t", litera, "]")
    return ""

def menu(wybor):
    funkcje[wybor]()

def cezar():
    plikJawny = open('plain.txt', 'r').read()
    x = 0
    napis = ""
    while x < plikJawny.__len__():
        napis += alfabet[(ord(plikJawny[x])-65 + keyA) % 26] if plikJawny[x] in alfabet else error(plikJawny[x])
        x += 1
    b = open('crypto.txt', 'w').write(napis)
def decryptCezar():
    plikCrypto = open('crypto.txt', 'r').read()
    x = 0
    napis = ""
    while x < plikCrypto.__len__():
        napis += alfabet[(ord(plikCrypto[x])-65 -keyA ) % 26] if plikCrypto[x] in alfabet else error(plikCrypto[x])
        x += 1
    plikJawny = open('plain.txt', 'w').write(napis)
def afiniczny():
    plikJawny = open('plain.txt', 'r').read()
    x=0
    napis=""
    while x < plikJawny.__len__():
        napis += alfabet[(keyA * (ord(plikJawny[x])-65) + keyB) % 26] if plikJawny[x] in alfabet else ""
        x+=1
    plikCrypto = open('crypto.txt', 'w').write(napis)

def decryptAfiniczny():
    plikCrypto = open('crypto.txt', 'r').read()
    x=0
    napis=""
    aPrim=odwrotnoscModulo(keyA,26)
    while x < plikCrypto.__len__():
        napis+= alfabet[((ord(plikCrypto[x])-65-keyB)*aPrim)%26] if plikCrypto[x] in alfabet else ""
        x+=1
    plikJawny = open('plain.txt', 'w').write(napis)

def analizaCezar():
    plikJawny = ord(open('plain.txt', 'r').read()[0]) -65
    plikCrypto = ord(open('crypto.txt', 'r').read()[0]) - 65
    print("Przesuniecie szyfru Cezara to: ", (plikCrypto-plikJawny) %26)


funkcje = {
    '-c-e' : cezar,
    '-c-d' : decryptCezar,
    '-a-e' : afiniczny,
    '-a-d' : decryptAfiniczny,
    '-j-c' : analizaCezar
    }
if isKeyGood:
    print(
        "Wybierz jedna z opcji: \n-c (szyfr Cezara),\n-a (szyfr afiniczny),\n______________________\n\n          +\n______________________\n-e (szyfrowanie),\n-d (odszyfrowywanie),\nJEDYNA DODATKOWA OPCJA:\n-j-c (kryptoanaliza szyfru Cezara z tekstem jawnym)\n-w: wyjście")
    wybor = ""
    while wybor!="-w":
        wybor = input("prosze, dokonaj wyboru")
        menu(wybor) if wybor in funkcje else print("Błędne polecenie, należy wybrać rodzaj szyfrowania oraz zadaie - np. dla szyfrowania Cezara: -c-e")
else:
    print("Błędny klucz, NWD(", keyA, ", 26) != 1")
