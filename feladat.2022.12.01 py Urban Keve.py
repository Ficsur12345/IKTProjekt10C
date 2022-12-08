'''
vezeteknev = input("Vezetéknév:")
keresztnev = input("Keresztnév:")
nev1 = vezeteknev+keresztnev
nev2 = keresztnev+vezeteknev
print(nev1)
print(nev2)

#2
szam = int(input("Kérek egy számot:"))
szam0 = szam-1
szam1 = szam+1
print(szam0)
print(szam1)

#3
szam1 = int(input("Kérek egy számot:"))
szam2 = int(input("Kérek egy másik számot:"))
print (szam1+szam2)
print (szam1-szam2)
print (szam1*szam2)
print (szam1/szam2)

#8
import random
num1 = int(input("Input First number "))
num2 = int(input("Input Second number "))

for i in range(10):
  print(random.uniform(num1, num2), end = "\t")

#9
import random
print(random.sample([i for i in range(1,100) if i%2==0], 20))
'''