import random as rd

def uppList(l):
        res = []
        for e in l:
                res.append(e.upper())
        return res

alphabetLow = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
specialChar = ['&', 'é', '#', '{', '(', '[', '-', 'è', '_', 'ç', 'à', '@', ')', ']', '=', '+', '}', '?', ';', '!', 'ù']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
alphabetUp = uppList(alphabetLow)
symbols = alphabetLow + alphabetUp + specialChar + numbers
n=""

nbSymbols = input("How many symbols ? : ")

for i in range(int(nbSymbols)):
        n += symbols[rd.randint(0,len(symbols)-1)]
print("Here is your password : " + n)
